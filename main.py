# TODO:  Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos 
# após o ponto decimal

valores = input().split()
velocidade_media = int(valores[0])
tempo_gasto = int(valores[1])

litros = (velocidade_media * tempo_gasto) / 12 

print("{:.3f}".format(litros))