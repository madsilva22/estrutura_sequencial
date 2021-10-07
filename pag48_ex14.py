print('Idade da pessoa em Anos, Meses, Dias e Semanas \n')

nascto = int(input('Digite o Ano de Nascimento: \n'))
ano_atual = int(input('Digite o ano Corrente: \n'))

ano = ano_atual - nascto
meses = ano*12
dias = ano*365
semanas = ano*52

print('Sua Idade em Anos: ', ano)
print('Sua Idade em Meses: ', meses)
print('Sua Idade em Semanas: ', semanas)
print('Sua Idade em Dias', dias)