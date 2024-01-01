import random
primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]  #[] serve para fazer um lista
escolhido = random.choice(lista) #choice escolhe um

print(f'O aluno escolhido foi {escolhido}')
