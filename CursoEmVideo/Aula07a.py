print('==== AULA O7-A ====')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
divi = n1 / n2
diviIntei = n1 // n2
restoDivi = n1 % n2
expone = n1 ** n2
print('A soma é {}\nA subtração é {}\nA multiplicação é {}\nA divisão é {:.2f}\nA divisão inteira é {}\nO '
      'módulo é {}\nO excponencial é {}'.format(soma, sub, mult, divi, diviIntei, restoDivi, expone))
# print('A divisão é {:.2f}, a divisão inteira é {}'.format(divi, diviIntei,))
# print('O módulo é {} e o excponencial é {}'.format(restoDivi, expone))
