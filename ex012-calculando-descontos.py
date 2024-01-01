preço = float(input('Qual é o preço do produtor? R$'))
valordesconto = float(input('qual o valor do desconto?: '))
desconto = valordesconto / 100
novo = preço - (preço * desconto )
print(f'O produto que custava R${preço}, na promoção com desconto de {valordesconto}% vai custar R${novo}.')