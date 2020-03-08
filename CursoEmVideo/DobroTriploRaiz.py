print('==== Dobro  - Triplo - Raiz Quadrada ====')
import math

numeroDigitado = float(input('Digite um número: '))
msg = 'Número digitado {:.2f}\nDobro: {:.2f}\nTriplo: {:.2f}\nRaiz quadrada: {:.2f}'
raiz = math.sqrt(numeroDigitado)
print(msg.format(numeroDigitado, (numeroDigitado * 2), (numeroDigitado * 3), raiz))
