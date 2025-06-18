'''
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(Quantidade)
> - Direita
< - Esquerda
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.3457666767567:0=+10,.2f}')
print(f'o hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
