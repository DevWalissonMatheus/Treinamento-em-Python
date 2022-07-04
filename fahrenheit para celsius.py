# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

print('Conversor de Fahrenheit para Celsius', end='\n\n')

fah = float(input('Digite a temperatura em Fahrenheit: \n'))
cal = (fah - 32) * 5 / 9

print(f'Temperatura em graus Celsius: {cal:.2f}')