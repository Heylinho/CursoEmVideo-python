termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10-1) * razao
for tab in range(termo,decimo + razao,razao):
    print('{}' .format(tab), end=' -> ')
