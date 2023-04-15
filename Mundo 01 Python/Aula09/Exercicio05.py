fra = str(input('Digite uma frase: ')).strip().upper()

print('A letra "A" aparece {} na frase!' .format(fra.count('A')))
print('A primeira posicao da letra "A" eh: {}' .format(fra.find('A')+1))
print('A ultima posicao da letra "A" eh: {}' .format(fra.rfind('A')+1))