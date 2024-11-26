import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
print('O Angulo de {} tem o seno: {:.2f}'.format(angulo,seno))
cos = math.cos(math.radians(angulo))
print('O Angulo de {} tem o cosseno: {:.2f}'.format(angulo,cos))
tan = math.tan(math.radians(angulo))
print('O Angulo de {} tem o rangente: {:.2f}'.format(angulo,tan))
