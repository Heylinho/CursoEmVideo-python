a = int(input('Escreva NUM1: '))
b = int(input('Escreva NUM2: '))
c = int(input('Escreva NUM3: '))

if a > b and a > c:
    print('Num1 é maior numero entres os 3')
elif b > a and b > c:
    print('Num2 é maior numero entres os 3')
else:
    print('Num3 é maior numero entres os 3')
    
if a < b and a < c:
    print('Num1 é menor numero entres os 3')
elif b < a and b < c:
    print('Num2 é menor numero entres os 3')
else:
    print('Num3 é menor numero entres os 3')

