lista = []
repetidos = []

for i in range (10):
    valores = int(input('Valores: '))
    lista.append(valores)

while True:
    if lista == []:
        break
        
    aux = lista[0]
    del lista[0]
    
    for j in lista:
        if aux == j:
            repetidos.append(aux)
            break
print(repetidos)