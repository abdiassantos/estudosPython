#%%
##Leitura de Arquivos CSV de maneira comum.
import csv

with open('arquivosCSV/dados.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    cabecalho = True

    for row in csv_reader:
        if cabecalho:
            print(f'Nomes das Colunas: { ", ".join(row)}')
            cabecalho = False
        else:
            print(f'{", ".join(row)}')

#%%
##Lendo arquivo CSV diretamente pra um dicionário.
import csv

with open('arquivosCSV/dados.csv', 'r') as csv_arq:
    csv_dict = csv.DictReader(csv_arq)
    cabecalho = True

    for row in csv_dict:
        if cabecalho:
            print(f'Nome das Colunas: {", ".join(row)}')
            cabecalho = False
        print(f'{row["Year"]} - {row["Make"]} {row["Model"]} - {row["Length"]}')

#%
##Salvando dados em um arquivo CSV
import csv

with open('arquivosCSV/dados_escrita.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter = ';')
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


#%%
##Escrevendo em um arquivo CSV diretamente de um dicionário
import csv

with open ('arquivosCSV/dados_escrita_dict.csv', mode = 'w', encoding = 'utf-8', newline = '') as csv_file:
    fieldnames = [ 'nome', 'depto', 'mes_aniv']
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerow({'nome': 'João Silva', 'depto': 'Contabilidade', 'mes_aniv':'novembro'})
    writer.writerow({'nome': 'Catarina Andrade', 'depto': 'Informática', 'mes_aniv': 'março'})