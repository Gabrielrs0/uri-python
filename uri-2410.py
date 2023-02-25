n = int(input())
dicionario ={}
lista = []
cont = 0
while n:
    registro = int(input())
    lista.append(registro)
    n -=1
for i in lista:
    if i in dicionario:
        continue
    else:
        dicionario[i] = 1
        cont += 1
print(cont)