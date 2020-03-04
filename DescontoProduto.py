print('==== Desconto ====')
valorProduto = float(input('Valor do produto: R$'))
desconto = (5/100) * valorProduto
print('O produto esta na promoção com 5% de desconto.')
print('Desconto de R${:.2f}\nPreço final R${:.2f}'.format(desconto, valorProduto - desconto))
