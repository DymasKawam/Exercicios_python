palavra = str(input('Digite uma palavra: ')).strip().upper()
separado = palavra.split()
junto = ''.join(separado)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto [letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo.')
else:
    print('Não temos um palindromo.')