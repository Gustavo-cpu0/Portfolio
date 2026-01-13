🟦 Projeto 1 — Análise de Vendas com CSV, SQL e Python
📄 Descrição

Projeto de análise de dados fictícios de vendas, onde os dados são:

Criados e manipulados com Pandas

Persistidos em SQLite

Consultados via SQL

Visualizados em gráfico

Simula um cenário comum de análise de dados em empresas.

🛠️ Tecnologias utilizadas

Python

Pandas

SQLite

SQL

Matplotlib

📊 Funcionalidades

Criação de dataset fictício de vendas

Leitura e limpeza de dados com Pandas

Armazenamento em banco SQLite

Consulta SQL (GROUP BY, SUM)

Geração de gráfico de faturamento por produto

▶️ Como executar
pip install pandas matplotlib
python analise_vendas.py

📂 Arquivos gerados

vendas.csv

analise_vendas.db

grafico_vendas.png

💡 Conceitos demonstrados

Análise de dados

Integração Python + SQL

Manipulação de DataFrames

Visualização de dados

🟩 Projeto 2 — API REST de Inventário (Flask + SQLite)
📄 Descrição

API REST simples para consulta de produtos em estoque, simulando um sistema de inventário básico.

Ideal para demonstrar conhecimentos iniciais em backend.

🛠️ Tecnologias utilizadas

Python

Flask

SQLite

🔌 Endpoints
Método	Endpoint	Descrição
GET	/produtos	Retorna lista de produtos
▶️ Como executar
pip install flask
python api_inventario.py


A API ficará disponível em:

http://127.0.0.1:5000/produtos

💡 Conceitos demonstrados

Criação de API REST

Integração Flask + banco de dados

Manipulação de dados persistentes

Estrutura básica de backend

🟨 Projeto 3 — Analisador de Logs de Suporte
📄 Descrição

Script para análise automática de logs de servidor, focado em identificar e resumir erros.

Simula um cenário real de suporte técnico e infraestrutura.

🛠️ Tecnologias utilizadas

Python

Regex (re)

Collections (Counter)

📋 Funcionalidades

Leitura de arquivo de log

Identificação de mensagens de erro

Contagem por tipo de erro

Geração de relatório técnico em texto

▶️ Como executar
python analisador_logs.py

📂 Arquivos gerados

server.log

relatorio_suporte.txt

💡 Conceitos demonstrados

Automação de tarefas

Análise de logs

Uso de expressões regulares

Suporte e monitoramento de sistemas