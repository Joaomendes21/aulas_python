try:
    numero = input('Digite um numero:')
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O numero {numero_int} que você digitou é par.')
    else:
        print(f'O numero {numero_int} que você digitou é impar.')
except:
    print("Isso não é um número inteiro.")
