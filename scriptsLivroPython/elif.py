imposto = float(input("Imposto: "))

if imposto < 10:
    print("Médio!")
elif imposto < 27.5:
    print("Alto")
else:
    print("Muito Alto")