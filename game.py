import pygame
import random
import time
import sys

#Inicializar pygame
pygame.init()
w, h = 600, 300
screen = pygame.display.set_mode((w, h))
#Color
rosa = (255,150,255)
blanco = (255,255,255)
negro = (0,0,0)
#Fuente de TXT
font = pygame.font.Font("font_pixel_txt.ttf", 30)
#
def crear_text(txt):
    msj = font.render(txt,True,blanco)
    screen.blit(msj,(200,50))
#
def crear_botones(txt, pos):
    text  = font.render(txt,True,blanco)
    rect = text.get_rect(topleft=pos)
    screen.blit(text,rect)
    return rect
#
run = True
msj = "Me amas? :D"
button_no_pos = [350,250]
button_size = (80,40)
tiempo_inicial = None

#
while run:
    screen.fill(rosa)
    crear_text(msj)

    rect_si = crear_botones("Si",(180,250))

    rect_no = crear_botones("No",button_no_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect_si.collidepoint(event.pos):
                msj = "Yo tambiennn jiji"

                tiempo_inicial = time.time()
            elif rect_no.collidepoint(event.pos):
                msj = "Segura??? T.T"

    mouse_pos = pygame.mouse.get_pos()
    if rect_no.collidepoint(mouse_pos):
        button_no_pos[0] = random.randint(0,w -button_size[0])
        button_no_pos[1] = random.randint(150, h-button_size[1])

    if tiempo_inicial:
        if time.time() - tiempo_inicial > 3:
            run = False

    pygame.display.flip()

pygame.quit()
sys.exit()