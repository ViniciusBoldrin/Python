#Calculando seno e cosseno
import math

ang = float(input('Digite o angulo para ser calculado sen e cos: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(' O seno é: {:.2f}\n O cosseno é: {:.2f}\n A tangente é: {:.2f}' .format(sen ,cos ,tan))