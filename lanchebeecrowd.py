valor, quantidade = map(int, input().split())

if valor == 1:
    preco = 4.00
elif valor == 2:
    preco = 4.50
elif valor == 3:
    preco = 5.00
elif valor == 4:
    preco = 2.00
elif valor == 5:
    preco = 1.50
else:
    preco = 0

print(f'Total: R$ {preco * quantidade:.2f}')


    
