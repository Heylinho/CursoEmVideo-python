import math

n1 = float(input('Escreva a altura da sua parede: '))
n2 = float(input('Escreva a largura da sua parede: '))

area = n1 * n2
tinta = 2

pintura = math.ceil(area // tinta)

print('Sabendo que cada lata de tinta pinta 2m²')
print(f'Para pintar sua parede que tem {area} m², você vai precisar de {pintura} latas de tinta!')
