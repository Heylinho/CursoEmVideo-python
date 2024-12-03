texto = str(input('Escreva uma frase que tenha letra ->A<-: ')).strip()

texto = texto.lower()

print('Quantas vezes aparece a letra "A": {}'.format(texto.count('a')))

print('Em qual a posição aparece a primeira letra "A": {}'.format(texto.find('a')))

print('Em qual a posição aparece a ultima letra "A": {}'.format(texto.rfind('a')))