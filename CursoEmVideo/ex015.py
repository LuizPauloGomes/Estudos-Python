print('==== Aluguel de Carros')
diaria = float(60)
precoKm = float(0.15)
diasAlugado = int(input('Dias com carro alugado: '))
kmRodado = float(input('Quantos KM rodado: '))
valorPorDia = diasAlugado * diaria
valorTotalKm = kmRodado * precoKm
valorTotalAluguel = valorPorDia + valorTotalKm
print('Você alugou o carro por {} dias e rodou {:.2f}KM'.format(diasAlugado, kmRodado))
print('Custo total por dia R${:.2f}\nCusto total por KM rodado {:.2f}'.format(valorPorDia, valorTotalKm))
print('Total a pagar R${:.2F}'.format(valorTotalAluguel))
