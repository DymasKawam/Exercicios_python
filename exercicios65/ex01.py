while True:
    quantMin = int(input('Digite a quantidade mínima do produto: '))
    quantMax = int(input('Digite a quantidade maxima do produto: '))

    if quantMax < quantMin: 
        print('erro! quantidade maximo menor que minima.')
        continue
    if quantMin < 0:
        print('Erro! Quantidade minina menor que 0.')
        continue
    media = int((quantMax + quantMin) / 2)

    print(f'a média do estoque é: {media}')
    break