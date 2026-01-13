import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# 1. Criar dados fictícios para o exemplo
data = {
    'ID': [1, 2, 3, 4, 5],
    'Produto': ['Teclado', 'Mouse', 'Monitor', 'Teclado', 'Mouse'],
    'Categoria': ['Periféricos', 'Periféricos', 'Hardware', 'Periféricos', 'Periféricos'],
    'Preco': [150.00, 80.00, 1200.00, 150.00, 80.00],
    'Data': ['2025-01-01', '2025-01-02', '2025-01-02', '2025-01-03', '2025-01-03']
}
df = pd.DataFrame(data)
df.to_csv('vendas.csv', index=False)

# 2. Carregar e Limpar com Pandas
df_vendas = pd.read_csv('vendas.csv')
df_vendas['Data'] = pd.to_datetime(df_vendas['Data'])

# 3. Salvar no SQLite
conn = sqlite3.connect('analise_vendas.db')
df_vendas.to_sql('vendas', conn, if_exists='replace', index=False)

# 4. Consulta SQL: Total de vendas por produto
query = "SELECT Produto, SUM(Preco) as Total FROM vendas GROUP BY Produto"
df_resultado = pd.read_sql(query, conn)

print("Resultado da Consulta SQL:")
print(df_resultado)

# 5. Gerar Gráfico
df_resultado.plot(kind='bar', x='Produto', y='Total', color='skyblue')
plt.title('Total de Vendas por Produto')
plt.ylabel('Receita (R$)')
plt.savefig('grafico_vendas.png')
print("\nGráfico 'grafico_vendas.png' gerado com sucesso!")

conn.close()