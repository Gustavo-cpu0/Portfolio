import re
from collections import Counter

# Simulando um arquivo de log
log_content = """
2026-01-03 10:00:01 INFO User logged in
2026-01-03 10:05:20 ERROR Database connection failed
2026-01-03 10:10:45 WARNING Disk space low
2026-01-03 10:15:12 ERROR Timeout reached
2026-01-03 10:20:00 INFO Report generated
2026-01-03 10:25:30 ERROR Database connection failed
"""

with open('server.log', 'w') as f:
    f.write(log_content)

def analisar_logs(file_path):
    print(f"--- Analisando: {file_path} ---")
    
    with open(file_path, 'r') as file:
        logs = file.read()
        
    # Encontrar todos os erros (Padrão: ERROR seguido da mensagem)
    erros = re.findall(r'ERROR (.*)', logs)
    contagem = Counter(erros)
    
    print(f"Total de erros encontrados: {len(erros)}\n")
    print("Resumo por tipo de erro:")
    for erro, total in contagem.items():
        print(f"- {erro}: {total}x")
        
    # Salvar relatório
    with open('relatorio_suporte.txt', 'w') as rel:
        rel.write("RELATORIO TECNICO DE LOGS\n")
        rel.write(f"Total de falhas: {len(erros)}\n")
        for erro, total in contagem.items():
            rel.write(f"{erro}: {total}\n")

if __name__ == "__main__":
    analisar_logs('server.log')