'''8) Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula:   V = 3.14159 * R * R * A  Onde as variáveis: V, R e A representam respectivamente o volume, o raio e a altura.  
'''
r = float(input('Raio: '))
a = float(input('Altura: '))
v = 3.14159 * r * r * a

print(f'O volume da lata de oleo é {v:.2f}')