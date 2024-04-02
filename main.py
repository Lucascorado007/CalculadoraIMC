
print('')
print('----Calculadora IMC------')
print('')

name = input('insira seu nome:')
peso = int(input('insira seu peso:'))
altura = float(input('insira sua altura:'))

imc = peso /  (altura ** 2)
print(f'IMC: {imc}')

if imc < 18.5:
    print(f'{name} você está abaixo do peso')

elif imc < 24.9:
    print(f'{name} você está no peso ideal (parabens!)')

elif imc < 29.9:
    print(f'{name} você está levemente acima do peso!')

elif imc < 34.9:
    print(f'{name} você tem obesidade grau I!') 

elif imc < 39.9:
    print(f'{name} você tem obedidade grau II!')

elif imc > 40:
    print(f'{name} você tem obesiade III (Mórbida)')

else:
    print('valor incorreto!')
  
