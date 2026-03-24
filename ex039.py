from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano 
alis = idade - 18  
print('Quem nasceu em {} tem {} em {}'.format(ano, idade, atual))
if idade > 18:
    alistamento = atual - alis
    print('Você ja deveria ter se alistado há {} anos'.format(alis))
    print('Seu alistamento foi em {} '.format(alistamento))
elif idade < 18:
    resta = 18 - idade
    ano_alistamento = atual - alis
    print('Ainda falta {} anos para seu alistamente militar.'.format(resta))
    print('Seu alistamento será em {} anos'.format(ano_alistamento))
else:  
    print('Você tem que se alistar IMEDIATAMENTE.')