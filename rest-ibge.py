import requests
import json
import csv

dados = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/')
estados = json.loads(dados.text)

regioes = {}

for estado in estados:
    regiao = estado['regiao']['nome']
    if regiao in regioes:
        regioes[regiao] = regioes[regiao] + 1
    else: 
        regioes[regiao] = 1

with open('csv/estados.csv', 'w', newline= '', encoding='utf-8') as csvfile:
    fieldnames = ['Regiao', 'Qtd. Estados']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter= '|')
    writer.writeheader()
    for regiao in regioes:
        writer.writerow({'Regiao': regiao, 'Qtd. Estados': regioes[regiao]})