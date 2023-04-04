a = int(input('Digite algo para ser analisado: '))

print('Segue a analise do que voce digitou: ' ,type(a))
print('Voce soh digitou espaco? ' ,a.isspace())
print('Eh um numero: ' ,a.isnumeric())
print('Eh alfabetico?: ' ,a.isalpha())
print('Eh alfanumerico?: ' ,a.isalnum())
print('Esta em maiuscula?: ' ,a.isupper())
print('Esta em minuscula?: ' ,a.islower())
print('Esta captalizado?: ' ,a.istitle())


