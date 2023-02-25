D, N = map(int, input().split())
his = [0]*D

while N != 0 and D != 0:
    sol_v = False
    s = N
    while N:
        alunos = [int(x) for x in input().split()]
        for i in range(len(alunos)):
            if alunos[i] == 1:
                his[i] += 1
        for j in his:
            if j == s:
                sol_v = True
        N -= 1
    if sol_v:
        print('yes')
    else: 
        print('no')
             
    D, N = map(int, input().split())
    his = [0]*D