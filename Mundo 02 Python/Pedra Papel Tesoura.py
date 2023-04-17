import time
import random

print('\033[4;30;44mBem vindo ao jogo Pedra, Papel, Tesoura!!\033[m')
print('\033[1;36m=-=\033[m' * 20)

time.sleep(1)

print('1 - Pedra 🪨')
print('2 - Papel 📰')
print('3 - Tesoura ✂️')

print('\033[1;36m=-=\033[m' * 20)

ep = int(input('Escolha sua jogada: '))

if ep == 1:
    print('Voce escolheu PEDRA!')
elif ep == 2:
    print('Voce escolheu PAPEL!')
elif ep == 3:
    print('Voce escolheu TESOURA!')

time.sleep(1)

ec = random.randint(1, 3)

if ec == 1:
    print('O computador escolheu PEDRA!')
elif ec == 2:
    print('O computador escolheu PAPEL!')
elif ec == 3:
    print('O computador escolheu TESOURA!')

time.sleep(1)

if ep == ec:
    print('\033[1;33mEmpate!\033[m')
elif ep == 1 and ec == 3:
    print('\033[1;32mVoce ganhou!\033[m')
elif ep == 2 and ec == 1:
    print('\033[1;32mVoce ganhou!\033[m')
elif ep == 3 and ec == 2:
    print('\033[1;32mVoce ganhou!\033[m')
else:
    print('\033[1;31mVoce perdeu!\033[m')