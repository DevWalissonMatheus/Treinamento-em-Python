# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

metros = float(input('Insira a quantidade em metros quadrados a serem pintados: '))
litros = metros/3

preçoL = 80
capacidadeL = 18

latas = litros / capacidadeL
total = latas * preçoL

print(f'Você usará {latas:.0f} latas de tinta')
print(f'O preço total é: {total:.2f} Reais')