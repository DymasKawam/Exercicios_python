a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a + b > c and c + a > b and c + b > a:
    if a == c == b:
        tipo = 'EQUILÁTERO' 
    elif a == c != b or c == b != a or b == a != c:
        tipo = "ISÓSCELES"
    elif a != c and a != b and b != c:
        tipo = 'ESCALENO'
    print('Os segmentos acimas sao capazes de fazer um triângulo {}'.format(tipo))    
else:
    print('Não será possivel fazer um triangulo.')