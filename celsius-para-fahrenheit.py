# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

print('Conversor de Celsius para Fahrenheit', end='\n\n')
cel = float(input('Digite a temperatura em Celsius: \n'))
cal = (cel * 9/5) + 32

print(f'A temperatura em Fahrenheit é: {cal:.2f}')