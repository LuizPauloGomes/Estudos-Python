print('Programa Para Analisar Nome')

nome = str(input('Digite seu Nome: ')).strip()#.strip, para eleiminar os espaços antes e depois do nome.

print('Seu nome é {} '.format(nome))
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu primeiro nome é {} e contém {} letras'.format(nome.split()[0], len(nome.split()[0]))) #Capturando primeiro elemento da string e contando as letras do mesmo.
separa = nome.replace(' ', '') #Retirando os espaço da string para contar as letras.
print('Nome sem espaço é {}\nTotal de letras {}'.format(separa, len(separa)))
