import random

##Gera um número aleatório e associa a uma variável.
numero = random.randint(1, 10)
print(numero)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

##Escolhe dentro de uma lista um valor aleatório os valores da lista.
print(random.choice(numeros))

##Embaralha a lista e seleciona aleatoriamente um valor dentro dela.
random.shuffle(numeros)
print("{}".format(numeros))
print(random.choice(numeros))


##Retorna um valor aleatório entre o intervalo 0.0 e 1.0
print("{}".format(random.random()))