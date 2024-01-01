import math
angulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente =math.tan(math.radians(angulo))
print(f' O âgulo de {angulo} tem o SENO de {seno:.2f} \n '
      f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f} \n '
      f'O ângulo de {angulo} tem a tangente de {tangente:.2f}')