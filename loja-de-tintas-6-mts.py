# Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados.
# E que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# a. comprar apenas latas de 18 litros;
# b. comprar apenas galões de 3,6 litros;
# c. misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

metros = float(input('Metros quadrados a serem pintados: '))
litros = metros/6
latas = litros /18

if latas % 18 !=18:
    latas += 1
precoL = latas * 80
galoes = litros / 3.6
if galoes % 3.6 != 0:
    galoes += 1
precoG = galoes * 25

mistura_lata = int(litros / 18.0)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

print('Latas de 18 litros: %d' % latas, 'latas custando: %d Reais'% precoL )
print('Galões de 3.6 litros: %d' % galoes, 'galões custando: %d Reais' % precoG)
print('Mistura: %d latas e %d galões = %.2f Reais' % (
    mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))