print('\033[1;32m=-\033[m' * 40)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso / altura ** 2

if IMC < 18.5:
    print('\033[1;31mVoce esta abaixo do peso!\033[m')
elif IMC >= 18.5 and IMC <= 25:
    print('\033[1;32mVoce esta no peso ideal!\033[m')
elif IMC >= 25 and IMC <= 30:
    print('\033[1;31mVoce esta com sobrepeso!\033[m')
elif IMC >= 30 and IMC <= 40:
    print('\033[1;31mVoce esta com obesidade!\033[m')
elif IMC > 40:
    print('\033[1;31mVoce esta com obesidade morbida!\033[m')