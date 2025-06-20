nome = input('Digite seu nome: ')
idade = input(f'Digite sua idade {nome}: ')
dados = f'Nome: {nome}, Idade: {idade}'
nome_invertido = (nome[::-1])

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome_invertido}.')
   
    if ' ' in nome:
        print('Seu nome tem espaço.')

    else:
        print('Seu nome não tem espaços.')

    print('Seu nome tem', len(nome),'letras!')
    print(f'A primeira letra do seu nome é: {nome[0]}.')
    print(f'A ultima letra do seu nome é: {nome[-1]}.')

else:
    print('Desculpe,você deixou um dos campos vazios.')


