##LISTAS
lista = []
print(type(lista))

lista.append("Python")
lista.append("Java")
lista.append("Javascript")
lista.append("PHP")

print(lista)

#Inverte os dados da lista.
lista.reverse()
print(lista)

##Insere no local indicado e move para a direita todos os outros termos da lista.
lista.insert(0, "Android")
print(lista)

##Remove o último elemento da lista e retorna ele.
lista.pop()
print(lista)

##Conta a ocorrência de um determinado objeto da lista.
print(lista.count("Python"))

##Remove um determinado elemento da lista.
lista.remove("PHP")
print(lista)

##Adicionando outros tipos de dados a uma lista Str.
lista2 = []
lista.append(lista2)
lista2.append(1)
lista2.append(2)
lista.append(3)
lista.append(11)
print(lista)




##------------------------------------
##TUPLAS
tupla = ("Python", "Java", "Android", 12, [1, 2, 3], (1, 2))
print(type(tupla))

print(tupla[5])

##Contar a ocorrência de um objeto dentro da tupla.
print(tupla.count("Python"))

##Adicionar valor a uma lista que existe dentro da tupla.
tupla[4].append(4)
print(tupla)

##------------------------------------
##DICIONÁRIOS
##Criando Dicionário e gerando a chave e o valor para cada chave.
dic = {"chave1": "valor1", 2: "valor2", (1, 2): "valor3"}

##Retorna o tipo da estrutura de dados.
print(type(dic))

##Retorna todos os métodos que podemos utilizar junto ao tipo de dados.
print(dir(dic))

##Retorna todos os itens com suas chaves e valores.
print(dic.items())

##Retorna todas as chaves do dicionário.
print(dic.keys())

##Remove o valor determinado pela chave.
dic.pop("chave1")
print(dic)

##Remove o valor do último item do nosso dicionário.
dic.popitem()
print(dic)

##Limpa todo o dicionário.
dic.clear()
print(dic)