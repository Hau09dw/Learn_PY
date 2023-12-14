import pygame
import random

WIDTH = 600
HEIGHT = 600
FPS = 30 # khung hinh tren giay


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Du lieu tu nguoi choi
    # Cap nhat thong so cua game
    # Ve cac doi tuong ra man hinh game
    pygame.display.flip()
pygame.quit()
