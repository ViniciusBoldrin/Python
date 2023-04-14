salario = float(input('Digite seu salario: '))

if salario >= 1250:
    aumento = salario * 1.1
    print(f'Seu salario com o aumento agora eh: {aumento}')
else:
    aumento2 = salario * 1.15
    print(f'Seu salario com o aumento agora eh: {aumento2}')