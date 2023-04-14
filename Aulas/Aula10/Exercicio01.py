import random

sorteio = random.randint(1, 5)
print('-=-' * 20)
escolha = int(input('Tente adivinhar um numero de 1 a 5: '))
print('-=-' * 20)

if sorteio == escolha:
    print('\033[0;32;40mParabens!! Voce acertou!\033[m')
else:
    print(f'\033[0;31;40mEh.. nao foi dessa vez amigo :// Eu pensei no número {sorteio}\033[m')


