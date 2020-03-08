print('====Desafio 03====’')

num1 = input('Digite um número:')  # Capturar primeiro número.
num2 = input('Digite outro número:')  # Capturar segundo número.
soma = int(num1) + int(num2)  # O uso de int antes de num1 e num2, converte os números de string para inteiros.
msg = 'O resultado da soma entre {} e {} é {}'
print(msg.format(num1, num2, soma))  # Apresenta o resultado da SOMA.
