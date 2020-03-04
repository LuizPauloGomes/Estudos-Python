''' ==== Minha Resolução ===
from math import sqrt
cateto1 = float(input('Digite a medita do 1º cateto: '))
cateto2 = float(input('Digite a medida do 2° cateto: '))
hipote = sqrt((cateto1 **2) + (cateto2 **2))
print('1° CATETO {}\n2ºCATETO {}\nHIPOTENUSA {:.2f}'. format(cateto1, cateto2, hipote))'''
from math import hypot
cateto1 = float(input('Digite a medida do 1° cateto: '))
cateto2 = float(input('Digite a medida do 2º cateto: '))
hipote = hypot(cateto1, cateto2)
print('O valor da hipotenusa é {:.2f}'.format(hipote))
