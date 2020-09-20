from pygame import mixer, event

pygame.init()

mixer.music.load('exercises/watermelon.mp3')
mixer.music.play()
event.wait()