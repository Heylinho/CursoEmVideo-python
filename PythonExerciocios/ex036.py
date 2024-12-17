numero = int(input('Escreva um número inteiro: '))

escolha = int(input('Escolha a conversão: [1 - Binário / 2 - Octal / 3 - Hexadecimal]: '))

if escolha == 1:
    binario = bin(numero)[2:]
    print(binario)
elif escolha == 2:
    octal = oct(numero)[2:]
    print(octal)
elif escolha == 3:
    hexadecimal = hex(numero)[2:]
    print(hexadecimal)
else:
    print('Opção inválida.')
