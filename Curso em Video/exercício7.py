'''
7) Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de conversão de  temperatura a ser utilizada é C = (F - 32) * 5 / 9, em que a variável F é a temperatura em graus Fahrenheit e a  variável C é a temperatura em graus Celsius.  '''

f = float(input('Temperatura em Fº: '))
c = (f - 32) * 5 / 9
print(f'A temperatura {f:.1f}Fº em Celsius é: {c:.1f}Cº')