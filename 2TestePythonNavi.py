# -*- coding: utf-8 -*-
import math
"""
Created on Sat Dec 19 12:51:38 2020

@author: sarah
"""

x = []
fac = 1

for i in range(1, 12): #i_max = 10; i=0 implicaria em erro nas funções matemáticas
    fac = fac * i
    if i % 2 == 0:
        par = round(((3**i)+(7*fac)),2)
        x.append(par)
    else:
        ln = math.log(i)
        impar = round(((2**i)+(4*ln)),2)
        x.append(impar)

  
print(x)
maior_valor = (max(x))
posicao = x.index(maior_valor)
media = round(sum(x) / float(len(x)),2)
print("O maior elemento do vetor é:", maior_valor, "sua posição é:", posicao)
print("A média dos elementos é:", media)