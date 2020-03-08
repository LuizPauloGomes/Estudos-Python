print('==== Conversor de Médida ====')
medida = float(input('Digite a médida em metros: '))
dm = medida * 10    # Decimetro
cm = medida * 100   # Centimetro
mm = medida * 1000  # milimetro
dam = medida / 10  # Decametro
hm = medida / 100  # Hectometro
km = medida / 1000  # Quilometro
print('Metro: {}m\nDecimetro: {}dm\nCentimentro: {}cm\nMilimetros: {}mm'.format(medida, dm, cm, mm))
print('Decametro: {}dam\nHectometro: {}hm\nQuilometro: {}km'.format(dam, hm, km))
