import random
import time
computador = random.randint(0, 5) #esse comando faz o computador "pensar" em um número
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # O jogador tenta advinhar o número
print('PROCESSANDO...')
time.sleep(2)
if jogador == computador:
    print('Parabens! Você conseguiu me vencer')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}!')



