n = str(input('Digite seu nome completo: ')).strip()

nome = n.split()

print(f'Seu primeiro nome: {nome[0]}')
print(f'Seu ultimo nome: {nome[len(nome)-1]}')