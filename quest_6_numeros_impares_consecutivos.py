m = int(input('Numero de linhas: '))
cont = 1
for i in range (m):
    l = []
    while len(l) != i+1:
        if cont % 2 != 0:
            impar = cont
            l.append(impar)
        cont+=1
    print(l)
l.clear()