'''import pygame
pygame.init()
pygame.mixer.music.load('toca.wav')
pygame.mixer.music.play()
pygame.event.wait()
==== NÃO FUNCIONOU ====
'''


'''from pydub import AudioSegment
from pydub.playback import play

som = AudioSegment.from_wav('toca.wav')
play(som)
==== NÃO FUNCIONOU ====
'''
'''
1)Baixar o arquivo get-pip.py (salve o arquivo em uma pasta)
2)Pelo CMD instalar o pip, navege até a pasta e digite, python get-pip.py
3)Instalar o modulo playsound (CMD: pip install playsound)
4)playsound('INDIQUE O CAMINHO DO ARQUIVO/musica01.wav')
5)Eu só consegui tomar musica em formato .wav
'''
from playsound import playsound
playsound('C:/Users/usuario/Desktop/PARA CLIENTES/an/musica01.wav')
#playsound('C:/Users/usuario/Desktop/PARA CLIENTES/an/musica02.wav')
