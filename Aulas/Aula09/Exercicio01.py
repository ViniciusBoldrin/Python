nome = str(input('Escreva seu nome: ')).strip()
print('Analisando...')

print('Seu nome em maiusculo e: {}' .format(nome.upper()))
print('Seu nome em minusculo e: {}' .format(nome.lower()))
print('Seu nome tem {} letras!' .format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras!' .format(nome.find(' ')))




