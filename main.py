import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("birthday card")

img=pygame.image.load("bgone.jpg")
image=pygame.transform.scale(img,(600,600))
running=True
while running:
    font=pygame.font.SysFont("Arial",70)
    text1=font.render("HAPPY",True,("green"))
    text2=font.render("BIRTHDAY",True,("green"))
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(text1,(200,180))
    screen.blit(text2,(180,260))
    pygame.display.update()
    time.sleep(2)

