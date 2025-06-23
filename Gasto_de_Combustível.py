tempo_viagem = int(input())
velocidade_media = int(input())
distancia = velocidade_media * tempo_viagem
gasolina_necessaria = distancia / 12
print(f'{gasolina_necessaria:.3f}')

