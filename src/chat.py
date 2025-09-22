import os
from search import search_prompt
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

def main():

    chain = search_prompt()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    # Inicializa embeddings e banco vetorial
    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))
    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )

    print("Chat iniciado. Digite sua pergunta (ou 'sair' para encerrar):")
    while True:
        pergunta = input("Pergunta: ")
        if pergunta.strip().lower() == "sair":
            break

        # 1. Vetorizar a pergunta
        pergunta_vector = embeddings.embed_query(pergunta)

        # 2. Buscar os 10 resultados mais relevantes (k=10) no banco vetorial
        docs = store.similarity_search_by_vector(pergunta_vector, k=10)
        contexto = "\n".join([doc.page_content for doc in docs])

        # 3. Montar o prompt e chamar a LLM
        prompt = search_prompt(question=pergunta).format(contexto=contexto, pergunta=pergunta)

        from langchain_openai import ChatOpenAI        
        llm = ChatOpenAI(model=os.getenv("OPENAI_CHAT_MODEL", "gpt-5-nano"))
        resposta = llm.invoke(prompt)

        # 4. Retornar a resposta ao usuário
        print("Resposta:", resposta.content if hasattr(resposta, "content") else resposta)

if __name__ == "__main__":
    main()