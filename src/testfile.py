import pygame
from pygame.locals import *
from math import sin, cos, radians

#créer la classe bouton
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        #chercher à savoir si on clique ou non
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

pygame.init()

clock = pygame.time.Clock()

FPS = 60
witdh = 600
height = 400

pause = False

color_text = (0, 0, 0)


resume_button = pygame.image.load("images/resume.jpg").convert_alpha()
setting_button = pygame.image.load("images/commande.jpg").convert_alpha()
quit_button = pygame.image.load("images/quit_button.jpg").convert_alpha()

boutton_resume = Button(200, 50, resume_button, 2)
boutton_quit = Button(200, 300, quit_button, 0.5)
boutton_setting = Button(200, 175, setting_button, 2)

def menu_pause(text, font, color_text, x, y):
    resume = font.render(text, True, color_text)
    fenetre.blit(resume, (x, y))

fenetre = pygame.display.set_mode((witdh, height))
fond = pygame.image.load("images/circuit_las_vegas.png").convert()
fond = pygame.transform.scale_by(fond, 10)
car = pygame.image.load("redbullf1.png").convert_alpha()
car = pygame.transform.scale_by(car, 0.2)
#image affiché
rotcar = car
#rectangle qui a les dimensions et les coordonnées de l'image
rotcarrect = pygame.Surface.get_rect(rotcar)
rotcarrect.center = (300, 200)
print(rotcarrect.topleft)
print(rotcarrect.bottomright)
x, y = -8850, -1100
vitesse = 0 

pygame.key.set_repeat(10)
angle = 0
continuer = True
while continuer:
   
    xmin, xmax = int(-x + 280), int(-x + 321)
    ymin, ymax = int(-y + 17), int(-y + 225)

    if pause:
        fenetre.fill((52, 78, 91))
        boutton_resume.draw(fenetre)
        boutton_quit.draw(fenetre)
        boutton_setting.draw(fenetre)
    else:
        menu_pause("Option", fond, color_text, 5, 5)
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            continuer = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vitesse -= 0.5
            if event.key == pygame.K_DOWN:
                vitesse += 0.5
            if event.key == pygame.K_RIGHT:
                angle -= 2
                rotcar = pygame.transform.rotate(car, angle)
                rotcarrect = pygame.Surface.get_rect(rotcar)
                rotcarrect.center = (300, 200)
            if event.key == pygame.K_LEFT:
                angle += 2
                rotcar = pygame.transform.rotate(car, angle)
                rotcarrect = pygame.Surface.get_rect(rotcar)
                rotcarrect.center = (300, 200)
    if vitesse < -10:
        vitesse = -10
    if vitesse > 10:
        vitesse = 10
    vitesserotated = (cos(radians(angle)) * 0 - sin(radians(angle)) * vitesse, sin(radians(angle)) * 0 + cos(radians(angle)) * vitesse)
    x, y = x + vitesserotated[0], y - vitesserotated[1]

    
    for iligne in range(xmin, xmax):
        for icolonne in range(ymin, ymax):
            if fond.get_at((iligne, icolonne)) == (0, 0, 0, 255): 
                vitesse +=0.5
                if vitesse > 0:
                    vitesse = 0    
                

    fenetre.blit(fond, (x, y))
    fenetre.blit(rotcar, rotcarrect.topleft)
    pygame.display.flip()


