velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h ')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar um multa de R${multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')