'''6) Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão de  temperatura a ser utilizada é F = (9 * C + 160) / 5, em que a variável F representa é a temperatura em graus  Fahrenheit e a variável C representa é a temperatura em graus Celsius.  '''

c = float(input('Tempera em Cº: '))
f = (9 * c+ 160) / 5

print(f'A temperatura em {c:.1f}Cº para fahrenheit é: {f:.1f}Fº ')