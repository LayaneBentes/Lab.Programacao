n = int(input('Informe o valor: '))

lista1 = []
lista2 = []

igual = True

for i in range (n):
    valor = int(input('valor da 1° lista: '))
    lista1.append(valor)

for i in range (n):
    valor = int(input('valor da 2° lista1: '))
    lista2.append(valor)

for i in range (n):
    if lista1[i] != lista2[i]:
        igual = False
        break

if igual == True:
    print('Sim')
else:
    print('Não')
