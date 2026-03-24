carro = int(input('Qual é a velocidade atual do carro?: '))
if carro > 80:
    print('Você excedeu o limite permitido que é de 80Km/h')
    multa = (carro - 80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(float(multa)))
print('Tenha uma ótima viagem')