soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
total_mulher = 0

for p in range(1, 5):
    print(f'==========={p}a PESSOA ============')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    if p ==1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
        
        
    
    soma_idade += idade

media_idade = soma_idade / 4
print(f'A média de idade do grupo é: {media_idade}')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_mais_velho}')

