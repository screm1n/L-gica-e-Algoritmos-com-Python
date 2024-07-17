print('Escolhe o que você deseja comprar:')
print('1 - Maça')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha?'))
quantidade = int(input('Quantas unidades?'))
if (produto == 1): # maça
    pagar = quantidade * 2.3
    print(f'Você comprou {quantidade} maças. Total à pagar: {pagar}')
elif (produto == 2): # laranja
    pagar = quantidade * 3.6
    print(f'Você comprou {quantidade} laranjas. Total à pagar: {pagar}')
elif (produto == 3): # bananas
    pagar = quantidade * 1.85
    print(f'Você comprou {quantidade} bananas. Total à pagar: {pagar}')