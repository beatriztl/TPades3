import pandas as pd
from collections import defaultdict
from grafoponderado import GrafoPonderado

tabela = pd.read_excel('votacoesVotos-2023.xlsx')
arquivo_votacoes = tabela[['idVotacao', 'voto', 'deputado_id', 'deputado_nome']]

#Criando o grafo das participações dos deputados
participacao = tabela['deputado_nome'].value_counts().sort_index()
arquivo_saida = 'participacao_deputados.txt'
participacao.to_csv(arquivo_saida, sep='\t', header=['Participações'], index_label='Deputado(a)')
print("\nArquivo de participação dos deputados criado: participacao_deputados.txt")

data = tabela.values.tolist()

grafo = GrafoPonderado()
grafo.grafo_resultado_votos_iguais(data)
print("Grafo de resultados iguais processado.\n")

