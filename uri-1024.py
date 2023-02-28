n = int(input())
while n > 0:
    m = input()
    novas = ''
    novas_2 = ''
    for i in m:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            asn = ord(i) + 3
            novas = novas + chr(asn)
        elif  ord(i) >= ord('a') and ord(i) <= ord('z'):
            asn = ord(i) + 3
            novas = novas + chr(asn)
        else:
            novas = novas + i
    passo_2 = novas[::-1]
    metade = len(passo_2)//2
    r = passo_2[:metade]
    r_2 = passo_2[metade:]
    for i in r_2:
        asn = ord(i) -1
        a = chr(asn)
        novas_2 =  novas_2+ a
    n -= 1
    print(r+ novas_2)