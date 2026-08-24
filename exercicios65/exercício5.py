'''
 Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem, utilizando um automóvel que faz  12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média.  Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE.  Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem com a  fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,  tempo gasto, a distância percorrida e a quantidade de litros utilizada na viagem. Dica: trabalhe com valores reais.  
'''

tempo = float(input('tempo gasto[exemplo 3.5 =  3 horas e 50 minutos. não colocar letras]: '))
veloMedia = float(input('Velocidade média[km/h, apenas números.]: '))

distancia = tempo * veloMedia
litros_usados = distancia / 12

print(f'''
Tempo: {tempo} hrs.
Velocidade Média: {veloMedia} km/h.
Distancia: {distancia:.2f} Km.
Litros usados: {litros_usados:.2f} L''')