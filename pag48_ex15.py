print('João e Suas Contas!!! \n\n')

salario = float(input('Digite seu Sálario, João:'))
conta1 = float(input('Agora digite sua conta atrasada:'))
conta2 = float(input('Tem mais uma conta atrasada , né! Vai, digita logo o valor da outra conta: '))

conta1 = conta1 * 1.02
conta2 = conta2 * 1.02

liquido = salario -(conta1 + conta2)

print('Conta 1 com multa de 2% :', conta1)
print('Conta 2 com multa de 2% :', conta2)

print('Seu salário liquido é de :', liquido)