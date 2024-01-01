salario = float(input('Qual o salário do funcionário? R$'))
aumentovalor = float(input('Digite o valor da porcentagem que você quer aumentar o salário do funcionário: '))
aumento = aumentovalor / 100
novosalario = salario + (salario * aumento )
print(f'Um funcionário que ganhava R${salario}, com {aumentovalor}% de aumento, passa a receber R${novosalario:.2f}')