'''
CONSTANTE = 'Variaveis' que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 60 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada
 
RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distancia onde o radar pega
velocidade_passou_radar1 = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = carro_passou_radar1 and velocidade_passou_radar1

if velocidade_passou_radar1: 
    print(f'Você passou do limite de velocidade que é (60) e a sua velocidade é: {velocidade}')
else:
    print('Você está dentro da faixa de velocidade.')

if carro_multado:
    print('Carro foi multado em radar 1')

a = int(input())
b = int(input())
PROD = a * b
print(f'PROD = {PROD}')