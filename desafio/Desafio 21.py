#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
from audioplayer import AudioPlayer
import time

arquivo_mp3 = 'desafio/technoloyia-technologia-tecnologia.mp3'
player = AudioPlayer(arquivo_mp3)
player.play()

time.sleep(7)
