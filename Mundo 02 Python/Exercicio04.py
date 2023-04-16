import datetime

nascimento = int(input('\033[4;30;40mDigite o ano do seu nascimento: \033[m'))

idade = datetime.date.today().year - nascimento

if idade < 18:
    anos_faltando = 18 - idade
    print(f'\033[1;32mFaltam {anos_faltando} anos para seu alistamento!\033[m')
elif idade == 18:
    print('\033[1;33mEsse é o ano do seu alistamento!\033[m')
elif idade > 18:
    anos_atrasado = idade - 18
    print(f'\033[1;31mVoce passou {anos_atrasado} anos do prazo de alistamento!\033[m')