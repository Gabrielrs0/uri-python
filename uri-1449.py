testes = int(input())
while testes:
    testes -= 1
    dicionario = {}
    lista = []
    musica_tra = []
    
    M, N = map(int, input().split())
    while M > 0:
        M -= 1
        key = input()
        value = input()
        dicionario[key] = value
    while N > 0:
        N -= 1
        N_linhas = input().split()
        lista.append(N_linhas)
    for i in lista:
        string = ''
        for j in range(len(i)):
            if j+1 == len(i):
                if i[j] in dicionario:
                   string = string + dicionario[i[j]]
                else:
                     string = string + i[j]
            else:
                if i[j] in dicionario:
                   string = string + dicionario[i[j]] + ' '
                else:
                     string = string + i[j] + ' '
                
        musica_tra.append(string)
    for i in musica_tra:
        print(i)
    print()