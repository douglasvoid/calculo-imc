print('##### CÁLCULO DE IMC #####')
peso = float(input('Digite seu peso: '))
altura = float(input('Digiten sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('O seu IMC está em {:.1f}, você está abaixo do peso!\nSe alimente mais'.format(imc))
elif imc < 25:
    print('O seu IMC está em {:.1f}, você está no peso ideal!\nParabéns!'.format(imc))
elif imc < 30:
    print('O seu IMC está em {:.1f}, você está em sobrepreso!\nSugiro que comece uma dieta e faça exercícios'.format(imc))
elif imc < 40:
    print('O seu IMC está em {:.1f}, você está Obeso!\nSugiro que faça uma dieta mais rigida e frequente academia'.format(imc))
elif imc > 40:
    print('O seu IMC está em {:.1f}, você está em Obesidade mórbida!!!\nNão sei o que sugerir'.format(imc))