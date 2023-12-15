import pygame, sys 
from pygame.locals import *

WIDTH = 480
HIGHT = 270
FPS = 60

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Animation")
fpsclock = pygame.time.Clock()

# font = pygame.font.SysFont('consolas',30)
# txtsurface = font.render('Heloooooo', True,(0,255,0),(255,0,0))
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background,(WIDTH,HIGHT))
class demo():
    def __init__(self):
        self.x = 0
        self.y = 100
        self.surface = pygame.image.load('demoanh.png')
    def draw(self):
        DISPLAYSURF.blit(self.surface,(self.x,self.y)) 
        
    def update(self,moveleft,moveright):
        if moveleft == True:
            self.x -= 2
        if moveright == True:
            self.x +=2
        if self.x + 100 > WIDTH:
            self.x = WIDTH - 100
        if self.x < 0:
            self.x = 0
Demo = demo()
moveleft = False
moveright = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moveleft = False
                
            if event.key == K_RIGHT:
                moveright = False
            
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moveleft = True
            if event.key == K_RIGHT:
                moveright = True
            
    DISPLAYSURF.blit(background,(0,0))
    # DISPLAYSURF.blit(txtsurface, (100,100))
    # pygame.draw.line(DISPLAYSURF,(0,0,255),(0,0),(100,100),5)
    Demo.draw()
    Demo.update(moveleft,moveright)
    pygame.display.update()
    fpsclock.tick(FPS)