# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato.
# faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e.calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.


shora = float(input('Quanto você ganha por hora: '))
hmes = float(input('Quantas horas você trabalha por mês: '))

s_bruto = shora * hmes
imp_renda = (11 * s_bruto) / 100
inss = (8 * s_bruto) / 100
sindi = (5 * s_bruto) / 100
s_liquido = s_bruto - imp_renda - inss - sindi

print(f'Salário Bruto: {s_bruto:.2f} Reais')
print(f'Desconto Imposto de Renda: {imp_renda:.2f} Reais')
print(f'Desconto INSS: {inss:.2f} Reais')
print(f'Desconto Sindicato: {sindi:.2f} Reais')
print(f'Salario Liquido: {s_liquido:.2f} Reais')