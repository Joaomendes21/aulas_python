# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
nome = 'otavio'
print(nome[2])
print('a' in nome)
print('ota' in nome)
print(10 * '-')
print('ota' not in nome)
print(15 * '-')
nome = input('Digite seu nome:')
encontrar = input('Digite o que você quer encontrar:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}.')
else:
    print(f'{encontrar} não está em {nome}')
