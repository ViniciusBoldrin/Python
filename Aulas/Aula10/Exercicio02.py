velocidade = float(input('Digite a velocidade do carro: '))


if velocidade <= 80:
    print('Voce estava na velocidade permitida! Sua multa eh igual a: R$ 0,00')
else:
    multa = (velocidade-80) * 7
    print(f'Voce estava acima da velocidade e tera que pagar: R${multa}!!')