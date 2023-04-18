import time

print('\033[1;30;43mContagem regressiva para o ano novo!\033[m')

for c in range(10, 0, -1):
    time.sleep(1)
    print(c)

time.sleep(1)

for c in range(0, 1):
    print('\033[4;34;42mFELIZ ANO NOVO!!!\033[m')