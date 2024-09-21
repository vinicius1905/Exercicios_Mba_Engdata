import csv
import random

# Lista de nomes de aeronaves
aeronaves = ['F-22 Raptor', 'Boeing 747', 'Concorde', 'A380', 'Cessna 172', 'F-16 Fighting Falcon', 
             'SR-71 Blackbird', 'B-2 Spirit', 'Airbus A320', 'Embraer E-Jet', 'F-35 Lightning II', 
             'UH-1 Iroquois', 'Dassault Rafale', 'MiG-29', 'Sukhoi Su-27']

# Função para ler os nomes a partir de um arquivo CSV
def ler_nomes_csv(caminho_arquivo):
    nomes = []
    with open(caminho_arquivo, mode='r') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        for linha in leitor_csv:
            nomes.append(linha['Nome completo'])  # Supondo que a coluna se chame 'nome'
    return nomes

# Função para criar grupos de até 3 pessoas
def criar_grupos(nomes):
    random.shuffle(nomes)  # Embaralha a lista de nomes para garantir uma distribuição aleatória
    grupos = [nomes[i:i + 3] for i in range(0, len(nomes), 3)]
    return grupos

# Função para nomear os grupos com nomes de aeronaves
def nomear_grupos(grupos):
    grupos_nomeados = {}
    for i, grupo in enumerate(grupos):
        nome_aeronave = aeronaves[i % len(aeronaves)]  
        grupos_nomeados[nome_aeronave] = grupo
    return grupos_nomeados

caminho_arquivo = 'Gerar_grupo.csv'
nomes = ler_nomes_csv(caminho_arquivo)
grupos = criar_grupos(nomes)
grupos_nomeados = nomear_grupos(grupos)

# Exibe os grupos
for aeronave, grupo in grupos_nomeados.items():
    print(f"Grupo {aeronave}: {', '.join(grupo)}")