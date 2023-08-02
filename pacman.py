

import pygame
import random
x=50
y=50

background_colour = (0, 0, 0)
displayHeight = 800
displayWidth = 600
width = 50
height = 50
pixel = 64
vel = 5
gostx = 400
gosty = 300

pinkwidth = 70
bluewidth = 60
display_surface = pygame.display.set_mode((displayHeight, displayWidth ))

pygame.display.set_caption('Pacman')
  

image = pygame.image.load(r'man.png')
redghost = pygame.image.load(r'redghost.png')
pinkghost = pygame.image.load(r'pinkghost.png')
orangeghost = pygame.image.load(r'orangeghost.png')
blueghost = pygame.image.load(r'bluegost.png')
pygame.display.flip()
  


scaled_image = pygame.transform.scale(image, (width, height))
scaled_redghost = pygame.transform.scale(redghost, (width, height))
scaled_pinkghost = pygame.transform.scale(pinkghost, (pinkwidth, height))
scaled_orangeghost = pygame.transform.scale(orangeghost, (width, height))
scaled_blueghost = pygame.transform.scale(blueghost, (bluewidth, height))
running = True




while running:
    display_surface.fill(background_colour)
    display_surface.blit(scaled_redghost, (gostx, gosty))
    display_surface.blit(scaled_pinkghost, (gostx, gosty - 60))
    display_surface.blit(scaled_orangeghost, (gostx - 60, gosty))
    display_surface.blit(scaled_blueghost, (gostx - 90, gosty - 60))
    for event in pygame.event.get():
        
    
        if event.type == pygame.QUIT:
            running = False
    def player(x, y):
        display_surface.blit(scaled_image, (x, y))

    circle = pygame.draw.circle(display_surface, (254, 255, 247),
                      [400, 300], 15, 0)
    line = pygame.draw.line(display_surface, (0, 0, 100),
                 [100, 300],
                 [500, 300], 5),

    keys = pygame.key.get_pressed()


  
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < displayHeight - vel - 50:
        x += vel

    if keys[pygame.K_UP] and y > vel:
        y -= vel

    if keys[pygame.K_DOWN] and y < displayWidth - vel - 50:
        y += vel

    keys = pygame.key.get_pressed()


  
    if keys[pygame.K_a] and gostx > vel and gostx - 60 > vel and gostx - 90 > vel:
        gostx -= vel

    if keys[pygame.K_d] and gostx < displayHeight - vel - 50 and gostx - 60 < displayHeight - vel - 50 and gostx - 90 < displayHeight - vel - 50:
        gostx += vel

    if keys[pygame.K_w] and gosty > vel and gosty - 60 > vel:
        gosty -= vel

    if keys[pygame.K_s] and gosty < displayWidth - vel - 50 and gosty - 60 < displayWidth - vel - 50:
        gosty += vel


    display_surface.blit(scaled_image, (x, y))  
    pygame.display.update() 
    