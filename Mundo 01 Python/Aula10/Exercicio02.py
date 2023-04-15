velocidade = float(input('Digite a velocidade do carro: '))


if velocidade <= 80:
    print('\033[1;30;42mVoce estava na velocidade permitida! Sua multa eh igual a: R$ 0,00\033[m')
else:
    multa = (velocidade-80) * 7
    print(f'\033[1;30;41mVoce estava acima da velocidade e tera que pagar: R${multa}!!\033[m')