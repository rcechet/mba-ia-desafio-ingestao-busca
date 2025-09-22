# Desafio MBA Engenharia de Software com IA - Full Cycle

Descreva abaixo como executar a sua solução.

# Pré-requisitos:
  > Baixar os arquivos na pasta C:\FC\mba-ia-desafio-ingestao-busca;
  > Python3 instalado;
  > Pacotes do framework Langchain instalados;
  > Docker instalado;
  > Preencher a key da OPENAI_API_KEY no arquivo .env;
  > Se a pasta de arquivos tiver um outro nome, fornecer o caminho correto no arquivo .env - PDF_PATH;
  
1. Subir o banco de dados:
> docker compose up -d

2. Executação ingestão do PDF:
> python3 src/ingest.py

3. Iniciar chat:
> python3 src/chat.py

4. Será mostrado: "Chat iniciado. Digite sua pergunta (ou 'sair' para encerrar):"
> Pergunta: Quais sao as 5 empresas com maior faturamento
...
lista das 5 empresas
...
