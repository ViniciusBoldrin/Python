#Sorteando Aluno
import random

print('Digite o nome dos alunos!')

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

num = a1,a2,a3,a4
sort = random.choice(num)

print('O aluno sorteado foi: {}' .format(sort))