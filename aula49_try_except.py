'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

numero_str = input('Digite um numero para eu dobrar o valor:')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print(f' Isso não é um numero - {numero_str}')

# if numero_str.isdigit():
#    
# else:
#     



