print('\033[1;30;41mSitema da Escola Master!\033[m')
print('\033[0;30m=-=\033[m' * 20)
print(' Por favor digite suas notas abaixo.')

nota_1 = float(input('Digita sua nota na primeira prova de matemática: '))
nota_2 = float(input('Digite sua nota na segunda prova de matemática: '))


media = (nota_1 + nota_2) / 2

if media < 5:
    print(f'Infelizmente sua média foi \033[4m{media}\033[m, e voce foi \033[1;31;40mreprovado.\033[m')
elif media >= 5 and media <=6.9:
    print(f'Sua média foi \033[4m{media}\033[m, e voce está de \033[1;33;40mrecuperação!\033[m')
elif media >= 7:
    print(f'Sua média foi \033[4m{media}\033[m, e voce está \033[1;32;40maprovado!\033[m')
    
    