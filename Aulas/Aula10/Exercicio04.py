distancia = float(input('Qual a distancia da viagem? '))

if distancia <= 200:
    total200 = distancia * 0.50
    print(f'O valor a ser pago eh: {total200}')
else:
    total201 = distancia * 0.45
    print(f'O valor a ser pago eh: {total201}')