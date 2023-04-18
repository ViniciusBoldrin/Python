import time
soma = 0

print('Exibindo numeros de 1 a 500 impares, divisiveis por 3:')

for c in range(0, 500, 3):
    print(c)
    time.sleep(0.3)
    soma += c
    
print(soma)
print('FIM')
