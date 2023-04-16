print('\033[0;36m=\033[m' * 20)
numero = int(input('Digite um número inteiro: '))
print('\033[0;36m=\033[m' * 20)
escolha = int(input('\033[4;35mAgora escolha qual será a base de conversão: 1 - Binário ; 2 - Octal ; 3 - Hexadecimal: \033[m'))

if escolha == 1:
    numero_escolhido = bin(numero)
    print(f'\033[0;32m O seu número convertido para binário é: {numero_escolhido[2:]}!\033[m')
elif escolha == 2:
    numero_escolhido = oct(numero)
    print(f'\033[0;32m O seu número convertido para octal é: {numero_escolhido[2:]}!\033[m')
elif escolha == 3:
    numero_escolhido = hex(numero)
    print(f'\033[0;32m O seu número convertido para hexadecimal é: {numero_escolhido[2:]}!\033[m')
