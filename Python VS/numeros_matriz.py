from random import randint as rd

def recebeValores(a):
    for x in a:
        for y in a:
            a[x][y] = rd(1,100)

def mostraValor(a):
    for _ in a:
        print(_)



matriz= [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

recebeValores(matriz)



