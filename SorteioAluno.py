'''====MINHA SOLUÇÃO EX 19 - 20====
from random import choice, sample
n1 = str(input('Aluno: '))
n2 = str(input('Aluno: '))
n3 = str(input('Aluno: '))
n4 = str(input('Aluno: '))
alunosDaSala = sample([n1, n2, n3, n4], k = 4)
print('Ordem de apresentação {}'.format(alunosDaSala))'''

print('====CORREÇÃO===')
from random import shuffle
n1 = str(input('Aluno: '))
n2 = str(input('Aluno: '))
n3 = str(input('Aluno: '))
n4 = str(input('Aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('Ordem da apresentação {}'.format(lista))
