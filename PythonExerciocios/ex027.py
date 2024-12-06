km = int(input('Escreva quando KM estava o seu carro: '))

if km >= 80:
    print('Você ultrapassou o limite de 80Km! MULTADO!!!!')
    excesso = km - 80  
    multa = excesso * 7 
    print('Valor da multa: R${}'.format(multa)) 
else:
    print('Tá suave, irmão!')
