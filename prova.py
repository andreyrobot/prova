nome = input("Qula o nome do paciente?: ")
peso = float(input(f"Quanto o paciente {nome} pesa?: "))
altura = float(input(f"Qual a altura do paciente {nome}?: " ))

IMC = peso / (altura * altura)

if IMC <= 18.5:
    print(f"O paciente {nome} está abaixo do peso normal")
elif IMC >=18.5:
    print(f"O paciente {nome} está com uma peso normal/ideal")
elif IMC >= 25.0:
    print(f"O paciente {nome} está levemente acima do peso/sobrepeso")
elif IMC >= 30.0:
    print(f"O paciente {nome} está está com obsidade Grau 1")
elif IMC >= 35.0:
    print (f"O paciente {nome} está com obsidade Grau 2")
else:
    print (f"O paciente {nome} está com obsidade Grau 3")