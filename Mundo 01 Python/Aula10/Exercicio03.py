numero = int(input('Digite um numero inteiro: '))

if numero % 2 == 0:
    print('\033[0;30;44mSeu numero eh par!\033[m')
else:
    print('\033[0;30;43mSeu numero eh impar!\033[m')