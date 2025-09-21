import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600


screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("good luck card")

img=pygame.image.load("bgone.jpg")
image=pygame.transform.scale(img,(600,600))
running=True
while running:
    font=pygame.font.SysFont("Arial",70)
    text1=font.render("GOOD",True,("blue"))
    text2=font.render("LUCK",True,("blue"))
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(text1,(180,-10))
    screen.blit(text2,(180,60))
    pygame.display.update()
    time.sleep(2)