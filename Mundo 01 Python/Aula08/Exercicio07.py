#Importando um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load('FireBoss.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

