import pygame

print('Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.')

pygame.init()
pygame.mixer.music.load('')
pygame.mixer.music.play()
pygame.event.wait()
