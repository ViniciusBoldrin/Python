print('\033[1;32m=-\033[m' * 40)

preco_produto = float(input('Digite o preco do produto: '))

print('Formas de pagamento:')
print('1 - A vista. (10% de desconto)')
print('2 - A vista no cartao. (5% de desconto)')
print('3 - Em ate 2x no cartao.')
print('4 - Em 3x ou mais no cartao. (20% de juros)')

pagamento = int(input('Digite a forma de pagamento: '))

if pagamento == 1:
    print(f'O valor do produto ficou: \033[1;32mR$ {preco_produto * 0.9:.2f}!\033[m')
elif pagamento == 2:
    print(f'O valor do produto ficou: \033[1;32mR$ {preco_produto * 0.95:.2f}!\033[m')
elif pagamento == 3:
    print(f'O valor do produto ficou: \033[1;32mR$ {preco_produto:.2f}!\033[m')
elif pagamento == 4:
    print(f'O valor do produto ficou: \033[1;32mR$ {preco_produto * 1.2:.2f}!\033[m')