import pygame
import random

#iniciar o pygame sempre com init
pygame.init()

#Definir a forma da tela do jogo
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo da forca")

#Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 40, 0)
verde = (0, 128, 0)

#Fonte para aparecer as palavras na tela
fonte = pygame.font.SysFont("roboto", 36)

executar = True
while executar:
    for rodar in pygame.rodar.get():


        pygame.quit()