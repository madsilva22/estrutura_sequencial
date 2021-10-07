print('Calculo da Esfera \n')

raio = float(input('Digite o tamanho do Raio: '))

comprimento = 2 * 3.14 * raio

area = 3.14 * (raio ** 2)
volume = 3/4 * 3.14 *(raio ** 3)

print(comprimento)
print(area)
print(volume)

print('O comprimento da esfera é de: {} \n, a área do objeto é {} e o seu volume é {}'. format(comprimento, area, volume))