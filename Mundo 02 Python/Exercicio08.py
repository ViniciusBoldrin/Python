print('\033[1;32m=-\033[m' * 40)
reta_1 = float(input('Digite o valor da primeira reta: '))
reta_2 = float(input('Digite o valor da segunda reta: '))
reta_3 = float(input('Digite o valor da terceira reta: '))

if (reta_1 + reta_2 > reta_3) and (reta_1 + reta_3 > reta_2) and (reta_2 + reta_3 > reta_1):
    print('\033[1;32mCom essas retas, voce pode formar um triangulo!\033[m')
    if reta_1 == reta_2 == reta_3:
        print('\033[4;33mE com essas retas, ele eh um triangulo Equilatero!!\033[m')
    elif reta_1 == reta_2 or reta_1 == reta_3 or reta_3 == reta_2:
        print('\033[4;33mE com essas retas, ele eh um triangulo Isosceles!!\033[m')
    elif reta_1 != reta_2 != reta_3:
        print('\033[4;33mE com essas retas, ele eh um triangulo Escaleno!!\033[m')
else:
    print('\033[1;31mCom essas retas, nao eh possivel formar um triangulo!\033[m')