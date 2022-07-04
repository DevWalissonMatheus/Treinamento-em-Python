# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal. 
# Usando a seguinte fórmula: (72.7*altura) - 58

alt = float(input('Insira sua altura: '))
cal = (72.7*alt) - 58

print(f'Seu peso ideal é: {cal:.2f}')