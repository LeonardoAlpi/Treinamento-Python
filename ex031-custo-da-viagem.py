distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar sua viagem de {distancia:.1f}km')
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'E o preço da sua viagem será de R${preço}')
