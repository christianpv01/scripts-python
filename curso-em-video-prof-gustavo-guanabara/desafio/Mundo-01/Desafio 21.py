#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
from audioplayer import AudioPlayer
from time import sleep

arquivo_mp3 = 'desafio/Desafio 21.mp3'
player = AudioPlayer(arquivo_mp3)
player.play()

sleep(7)
