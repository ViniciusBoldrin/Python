alt = float(input('Qual a altura da parede?: '))
lar = float(input('Qual a largura da parede?: '))

are = alt*lar
tin = are/2

print('A area da sua parede é de: {}, e voce precisará de {} litros de tinta para pinta-la!' .format(are ,tin))