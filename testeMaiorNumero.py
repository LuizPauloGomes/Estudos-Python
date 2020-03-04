print('== Maior número digitado ==')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
msg = 'O maior número digitado foi {}'
if(n1 > n2):
   if(n1 > n3):
       print(msg.format(n1))
else(n2 > n3):
    print(msg.format(n2))
else:
    print(msg.format(n3))
