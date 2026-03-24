'''from math import hypot
catA = float(input('Qual é o valor do cateto oposto?: '))
catB = float(input('Qual é o valor do cateto adjacente?: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(catA, catB))) '''
cat1 = float(input('Qual é o valor do cateto oposto?: '))
cat2 = float(input('Qual é o valor do cateto adjacente?: '))
hipot = (cat2 ** 2 + cat1 ** 2) **(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipot))