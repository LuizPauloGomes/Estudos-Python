print('==== Antecessor e Sucessor ====')
numeroDigitado = int(input('Digite um número: '))
# antecessor = numeroDigitado - 1
# sucessor = numeroDigitado + 1
msg = 'O antecessor de {} é {} e o sucessor é {}.'
print(msg.format(numeroDigitado, (numeroDigitado - 1), (numeroDigitado + 1)))
