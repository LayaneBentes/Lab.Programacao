
pai1 = input().split()
pai2 = input().split()

filho1 =[]
filho2 =[]

cont1 = pai1[0]
del pai1[0]
cont2 = pai2[0]
del pai2[0]

for i in range (int(cont1) - 1):
    filho1.append(pai1[0])
    if pai1[0] != pai1[1]:
        del pai1[0]
        break
    del pai1[0]

for i in range (int(cont2) - 1):
    filho2.append(pai2[0])
    if pai2[0] != pai2[1]:
        del pai2[0]
        break
    del pai2[0]

filho1 = filho1 + pai2
filho2 = filho2 + pai1
filho1.insert(0, str(len(filho1)))
filho2.insert(0, str(len(filho2)))

print(filho1)
print(filho2)