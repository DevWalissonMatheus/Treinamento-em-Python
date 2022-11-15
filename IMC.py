peso = float(input('Insira o seu peso: '))
altura = float(input('Insira sua altura: '))
imc = peso / altura**2

print('Seu IMC é: %.3f' %imc)

if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print('Magreza moderada')
elif imc < 18.5:
    print('Magreza leve')
elif imc < 25:
    print('Saudável')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade Grau I')
elif imc < 40:
    print('Obesidade Grau II (Severa)')
else:
    print('Obesidade Grau III (Mórbidade)')