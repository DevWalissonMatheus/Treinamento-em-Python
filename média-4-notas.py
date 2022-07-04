# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print('Programa para calcular a media de um aluno', end='\n\n')

nome = input('Entre com o nome do aluno: \n')

nota1 = float(input("Entre com a primeira nota: \n"))

nota2 = float(input("Entre com a segunda nota: \n"))

nota3 = float(input("Entre com a terceira nota: \n"))

nota4 = float(input("Entre com a quarta nota: \n"))


media = (nota1 + nota2 + nota3 + nota4) / 4
print('{0} teve media igual a: {1:4.2f}'.format(nome, media))