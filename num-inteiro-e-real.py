# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# a - o produto do dobro do primeiro com metade do segundo.
# b - a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.

numint1 = int(input('Digite o primeiro número inteiro: '))
numint2 = int(input('Digite o segundo número inteiro: '))
numreal = float(input('Digite um número real: '))

cal1 = (numint1 * 2) + numint2 / 2
cal2 = (numint1 * 3) + numreal
cal3 = numreal**3

print(f'O resultado do primeiro problema é: {cal1:.2f}')
print(f'O resultado do segundo problema é: {cal2:.2f}')
print(f'O resultado do terceiro problema é: {cal3:.2f}')