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
    font1=pygame.font.SysFont("Arial",70)
    text1=font1.render("HAPPY",True,("green"))
    text2=font1.render("BIRTHDAY",True,("green"))
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(text1,(200,180))
    screen.blit(text2,(180,260))
    pygame.display.update()
    time.sleep(2)

    img2=pygame.image.load("bgtwo.jpg")
    font2=pygame.font.SysFont("Arial",40)
    text3=font2.render("wish you a happy future",True,("blue"))
    text4=font2.render("i wish you have a great day",True,("blue"))
    screen.fill((255,255,255))
    screen.blit(img2,(0,0))
    screen.blit(text3,(30,30))
    screen.blit(text4,(30,60))
    pygame.display.update()
    time.sleep(2)

    img3=pygame.image.load("bgthree.jpg")
    font3=pygame.font.SysFont("Arial",40)
    text5=font3.render("here is your cake",True,("red"))
    screen.fill((255,255,255))
    screen.blit(img3,(0,0))
    screen.blit(text5,(50,10))
    pygame.display.update()
    time.sleep(2)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            exit()

pygame.quit()

        
        


