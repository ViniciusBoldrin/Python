import random

sorteio = random.randint(1, 5)
escolha = int(input('Tente adivinhar um numero de 1 a 5: '))

if sorteio == escolha:
    print('Parabens!! Voce acertou!')
else:
    print('Eh.. nao foi dessa vez amigo ://')

