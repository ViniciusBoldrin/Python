print('\033[1;36;40mSistema de análise de categoria de nadadores.\033[m')
print('\033[1;36m~~~\033[m' * 50)

idade = int(input('Por favor, digite sua idade: '))

if idade <= 9:
    print('Sua categoria de nadador \033[4;30;44mMIRIM!\033[m')
elif idade >= 10 and idade <= 14:
    print('Sua categoria de nadador é \033[4;30;44mINFANTIL!\033[m')
elif idade >= 15 and idade <= 19:
    print('Sua categoria de nadador é \033[4;30;44mJUNIOR!\033[m')
elif idade == 20:
    print('Sua categoria de nadador é \033[4;30;44mSÊNIOR!\033[m')
elif idade >= 21:
    print('Sua categoria de nadador é \033[4;30;44mMASTER!\033[m')
    