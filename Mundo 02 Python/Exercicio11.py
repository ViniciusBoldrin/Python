soma = 0
cont = 0

for c in range(0, 6):
    num_1 = int(input('Digite um valor: '))
    if num_1 % 2 == 0:
        soma += num_1
        cont += num_1

print(f'Voce informou {cont} numeros e a soma deles eh: {soma}')

