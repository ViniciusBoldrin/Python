#Calculando Hipotenusa

import math

c1 = float(input('Digite o tamanho do cateto 1: '))
c2 = float(input('Digite o tamanho do cateto 2: '))

soma = (c1*c1+c2*c2)
h = math.sqrt(soma)

print('A hipotenusa é: {}' .format(h))