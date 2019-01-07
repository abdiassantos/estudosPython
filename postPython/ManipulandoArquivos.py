#%%
##Adicionando de forma 'BRUTA' o texto de dentro da variável Texto.
arq = open('arquivosTxt/list.txt', 'w')

texto = """
Lista de Alunos
---
João da Silva
José Lima
Maria das Dores
---
"""

arq.write(texto)
arq.close()

#%%
##Adicionando o texto usando métodos para tal.
arq = open('arquivosTxt/listAppend.txt', 'w')

texto = []
texto.append('Lista de Alunos Usando Append\n')
texto.append('---\n')
texto.append('João da Silva\n')
texto.append('José Lima\n')
texto.append('Maria das Dores\n')
texto.append('---')

arq.writelines(texto)
arq.close()

#%%
##Lendo informações dos arquivos TXT colocando todo o conteúdo em uma única
# variável.
arq = open('arquivosTxt/list.txt', 'r')

texto = arq.read()
print(texto)
arq.close()

#%%
##Lendo informações dos arquivos TXT Linha por linha para que sejam colocados
# cada linha em uma variável.
arq = open('arquivosTxt/listAppend.txt', 'r')

texto = arq.readlines()
for linha in texto:
    print(linha)

arq.close()

