print('\033[1;36m*-*\033[m' * 20)
valor_1 = float(input('Digite um valor: '))
print('\033[1;36m*-*\033[m' * 20)
valor_2 = float(input('Digite outro valor: '))
print('\033[1;36m*-*\033[m' * 20)

if valor_1 > valor_2:
    print(f'O {valor_1} é maior que {valor_2}!')
elif valor_2 > valor_1:
    print(f'O {valor_2} é maior que {valor_1}! ')
elif valor_1 == valor_2:
    print('Os valores são iguais!')
    