def is_prime(num_1):

    if num_1 <= 1:
        return False
    elif num_1 <= 3:
        return True
    elif num_1 % 2 == 0 or num_1 % 3 == 0:
        return False

num_1 = int(input('Digite um número inteiro: '))

if is_prime(num_1):
    print(f'{num_1} é um núemro primo.')
else:
    print(f'{num_1} não é um número primo.')
    
    

