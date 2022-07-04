# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal.
# Utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = int(input('Digite o número referente ao seu gênero (1) Para homem (2) Para mulher: \n'))

if sexo == 1:
    ah = float(input('Insira sua altura: '))
    cal1 = (72.7*ah) - 58
    print(f'Seu peso ideal é: {cal1:.2f} quilos')
elif sexo == 2:
    am = float(input('Insira sua altura: '))
    cal2 = (62.1*am) - 44.7
    print(f'Seu peso ideal é: {cal2:.2f} quilos')