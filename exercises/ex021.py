import pygame
from pygame import mixer, event

pygame.init()

mixer.music.load('watermelon.mp3')
mixer.music.play()
event.wait()