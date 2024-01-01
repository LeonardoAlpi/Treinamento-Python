largura  = float(input('Digite a largura da parede: '))
altura  = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem dimensão de {largura:.2f}x{altura:.2f} e sua área é de {area:.2f}m². '
      f'\n Para pintar essa parede, você precisará de {tinta:.2f}L de tinta .')