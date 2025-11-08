"""Desafio 2

Você é um analista de dados, e decidiu trocar de emprego.

Utilize a media, moda, mediana e o desvio padrão para decidir qual empresa faz sentido para você:

Justificar por que decidiu por essa empresa.

***Verifique isso através dos salários:***"""

import statistics as st

empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

empresas = {
    "Empresa 1": empresa1,
    "Empresa 2": empresa2,
    "Empresa 3": empresa3,
    "Empresa 4": empresa4
}

def calcula_stats(salarios):
    # Arrumando a lista para achar a Mediana (o do meio)
    salarios_ordenados = sorted(salarios)
    
    # Calculando na mão:
    media = sum(salarios) / len(salarios) 
    
    # Pegando o número do meio:
    posicao_meio = len(salarios) // 2 
    mediana = salarios_ordenados[posicao_meio]
    
    # Moda: (Se não repetir, não tem, mas vamos usar a função para ser certinho)
    try:
        moda = st.mode(salarios)
    except st.StatisticsError:
        moda = "Não tem (Nenhum se repete)"
        
    # Desvio Padrão (usa a função, porque fazer a conta é CHATO!)
    desvio_padrao = st.stdev(salarios)

    return {
        "Média": f"R$ {media:.2f}",
        "Mediana": f"R$ {mediana:.2f}",
        "Moda": moda,
        "Desvio Padrão": f"R$ {desvio_padrao:.2f}"
    }

print("--- RESULTADOS DOS CÁLCULOS ---")
for nome, salarios in empresas.items():
    print(f"\n**{nome}**")
    stats = calcula_stats(salarios)
    for chave, valor in stats.items():
        print(f"  - {chave}: {valor}")