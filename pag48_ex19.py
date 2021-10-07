print('Calculo de lampadas por metro quardado \n')

lado1 = int(input('Digite Lado 1:'))
lado2 = int(input('Digite lado 2: '))

area = lado1 * lado2
pwtotal = area * 18

print('A area total do comodo é de {}mts quadrados e a potencia total é de {}watts'.format(area, pwtotal))
