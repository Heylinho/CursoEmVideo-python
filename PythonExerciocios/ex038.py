ano = int(input('Em qual ano você nasceu: '))
idade = 2024 - ano

if ano < 18:
    print('Você não está pronto para alistar!')
elif ano == 18:
    print('Ta na hora de alistar')
else:
    print('Já passou na hora!')
