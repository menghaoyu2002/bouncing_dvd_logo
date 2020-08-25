
import pygame
import sys
import random

pygame.init()
pygame.display.set_caption('DVD')

#colours
white = (255,255,255)
black = (0,0,0)
lightblue = (107,250,250)
yellow = (250, 250, 107)
orange = (242, 138, 19)
red = (242, 34, 19)
blue = (0, 30, 255)
pink = (242, 111, 196)
purple = (186, 38, 255)
colorlist = (white,black,lightblue,yellow)

#initial window size
size = (1000,600)

#all the other stuff i need to set beforehand
clock=pygame.time.Clock()
screen = pygame.display.set_mode((size),pygame.RESIZABLE)
fps=120

#different colours versions of the original dvd image
dvd = pygame.image.load('dvd.png')
dvd = pygame.transform.scale(dvd,(200,100))

lightbluedvd = dvd.copy()
lightbluedvd.fill(lightblue,special_flags=pygame.BLEND_ADD)

whitedvd = dvd.copy()
whitedvd.fill(white,special_flags=pygame.BLEND_ADD)

yellowdvd = dvd.copy()
yellowdvd.fill(yellow, special_flags=pygame.BLEND_ADD)

orangedvd = dvd.copy()
orangedvd.fill(orange, special_flags=pygame.BLEND_ADD)

reddvd = dvd.copy()
reddvd.fill(red, special_flags=pygame.BLEND_ADD)

pinkdvd = dvd.copy()
pinkdvd.fill(pink, special_flags=pygame.BLEND_ADD)

bluedvd = dvd.copy()
bluedvd.fill(blue, special_flags=pygame.BLEND_ADD)

purpledvd = dvd.copy()
purpledvd.fill(purple, special_flags=pygame.BLEND_ADD)

dvdlist = [yellowdvd,whitedvd,lightbluedvd,orangedvd,reddvd,pinkdvd,bluedvd,purpledvd]

#more stuff that needs to be set
x=0
y=0
deltax=2
deltay=2
chosendvd = whitedvd
previousdvd = 'undefined'
bounce = False

#main loop
run = True
while run:
    #color changing part
    if bounce:
        while previousdvd == chosendvd:
            chosendvd = random.choice(dvdlist)
            bounce = False
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False 
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.size),pygame.RESIZABLE)
 
    screen.fill(black)
    clock.tick(fps)

    #moves the dvd image and bounces it
    if x+200 >= screen.get_width():
        bounce=True
        deltax=-2
    if x == 0:
        bounce=True
        deltax=2
    if y+100 >= screen.get_height():
        bounce=True
        deltay=-2
    if y == 0:
        bounce=True
        deltay=2

    x+=deltax
    y+=deltay
    screen.blit(chosendvd,(x,y))
    previousdvd = chosendvd

    pygame.display.update()

pygame.quit()
#thats all