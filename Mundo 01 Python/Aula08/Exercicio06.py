#Sorteando Alunos em lista
import random

nomes = print('Digite o nome dos alunos!')

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
a5 = input('Aluno 5: ')
a6 = input('Aluno 6: ')

num = a1,a2,a3,a4,a5,a6
sort = random.sample(num, k=6)

print('A ordem de sorteio foi: {}' .format(sort))