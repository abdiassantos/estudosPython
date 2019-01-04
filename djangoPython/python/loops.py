lang = "Python"

##Utilizando FOR
for l in lang:
    print("{}".format(l))

for n in range(10):
    print("{}".format(n))

##Utilizando o WHILE
controle = 10
while controle >= 0:
    print("Contagem regressiva: {}".format(controle))
    controle -= 1
    if controle < 0:
        print("Boooooommm!")
