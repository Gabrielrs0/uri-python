n = int(input())
lista = []
his = [0]*n
s = n
while n:
    num = int(input())
    lista.append(num)
    n -=1
for i in range(0,len(lista)):
    if lista[i] == 0:
        continue
    if lista[i] == 1 and i == 0:
        his[i] += 1
        his[i+1] +=1
        continue
    if lista[i] == 1 and i ==s-1:
        his[i] +=1
        his[i-1] +=1
        continue
    elif lista[i] == 1:
        his[i] += 1
        his[i-1] += 1
        his[i+1] +=1
for i in his:
    print(i)