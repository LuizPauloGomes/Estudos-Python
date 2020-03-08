print('==== Reajuste salarial ====')
salario = float(input('Salario atual: R$'))
reajuste = float(input('Porcentagem de aumento: '))
aumento = ((reajuste/100) * salario)
novoSalario = aumento + salario
print('Reajuste de {}%\nAumento de R${:.2f}\nNovo salario R${:.2f}'.format(reajuste, aumento, novoSalario))
