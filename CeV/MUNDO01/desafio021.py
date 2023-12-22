import pygame

pygame.init()

# Inicialize o mixer de áudio
pygame.mixer.init()

# Carregue o arquivo MP3
pygame.mixer.music.load('MUSICA.mp3')

# Inicie a reprodução
pygame.mixer.music.play()

# Aguarde a reprodução terminar (opcional)
pygame.mixer.music.set_endevent(pygame.USEREVENT)
pygame.event.wait()

