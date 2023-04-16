print('\033[0;34m-=-\033[m' * 20)
valor_casa = float(input('Digite o valor da casa: '))
print('\033[0;34m-=-\033[m' * 20)
valor_salario = float(input('Digite o valor do salário: '))
print('\033[0;34m-=-\033[m' * 20)
valor_anos = float(input('Digite em quantos anos irá pagar: '))
print('\033[0;34m-=-\033[m' * 20)

prestacao = valor_casa / (valor_anos * 12)
limite_prestacao = valor_salario * 0.3

if prestacao <= limite_prestacao:
    print(f'\033[1;32mO valor das prestaçoes são: {prestacao:.2f}\033[m')
else:
    print(f'\033[1;31mInfelizmente voce não tem o salário para comparar a casa.\033[m')
