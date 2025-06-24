cachorro_quente = 4.00
x_salada = 4.50
x_bacon = 5.00
torrada_simples = 2.00
refrigerante = 1.50

print('"Lanches disponiveis"')
print('1 - Cachorro quente: R$ 4.00')
print('2 - X-salada: R$ 4.50')
print('3 - X-bacon: R$ 5.00')
print('4 - Torrada simples: R$ 2.00')
print('5 - Refrigerante: R$ 1.50')

valor = int(input('Digite o numero do lanche escolhido:'))
quantidade = int(input('Qual a quantidade:'))

if valor == 1:
    print(f'Cachorro quente, QT:{quantidade}, Total: R$ {cachorro_quente * quantidade:.2f}')
elif valor == 2:
     print(f'X-salada, QT:{quantidade}, Total: R$ {x_salada * quantidade:.2f}')
elif valor == 3:
     print(f'X-bacon, QT:{quantidade}, Total: R$ {x_bacon * quantidade:.2f}')
elif valor == 4:
     print(f'Torrada simples, QT:{quantidade}, Total: R$ {torrada_simples * quantidade:.2f}')
elif valor == 5:
     print(f'Refrigerante, QT:{quantidade}, Total: R$ {refrigerante * quantidade:.2f}')
else:
     print('Você digitou um numero que não existe.')


    
