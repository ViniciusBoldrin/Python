ano = int(input('Digite uma ano para saber se ele eh bissexto: '))

if ano % 4 == 0:
    print(f'{ano} eh um ano bissexto!')
else:
    print(f'{ano} nao eh um ano bissexto!')