import pygame
from pygame.locals import *
from math import sin, cos, radians

clock = pygame.time.Clock()

FPS = 60
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

width = 600
height = 400

fenetre = pygame.display.set_mode((width, height))
pygame.display.set_caption("F1")

#le début du jeu
game_start = False

#jeu en pause
pause = False

#les commandes
setting = False


font = pygame.font.SysFont("arialblack", 30)

TEXT_COL = (255, 255, 255)
color_text = (0, 0, 0)
#images pour les boutons
image0 = pygame.image.load("images/circuit_Barcelone.png").convert_alpha()
image1 = pygame.image.load("images/circuit_Brésil.png").convert_alpha()
image2 = pygame.image.load("images/circuit_las_vegas.png").convert_alpha()
image3 = pygame.image.load("images/circuit_Italie.png").convert_alpha()

resume_button = pygame.image.load("images/resume.jpg").convert_alpha()
setting_button = pygame.image.load("images/commande.jpg").convert_alpha()
quit_button = pygame.image.load("images/quit_button.jpg").convert_alpha()




#création des objets de type bouton
barcelone_circuit = Button(304, 5, image0, 0.15)
Brésil_circuit = Button(5, 230, image1, 0.15)
Las_Vegas_circuit = Button(5, 5, image2, 0.15)
Italie_circuit = Button(307, 230, image3, 0.15)

#création de boutons pour le menu pause
boutton_resume = Button(200, 50, resume_button, 2)
boutton_quit = Button(200, 300, quit_button, 0.5)
boutton_setting = Button(200, 175, setting_button, 2)

def draw_text(text, font, text_col,x, y):
    image = font.render(text, True, text_col)
    fenetre.blit(image, (x, y))

def menu_pause(text, font, color_text, x, y):
    resume = font.render(text, True, color_text)
    fenetre.blit(resume, (x, y))

    
def las_vegas():

    pause = False
    
    boutton_resume = Button(200, 50, pygame.image.load("images/resume.jpg").convert_alpha(), 2)
    boutton_quit = Button(200, 300, pygame.image.load("images/quit_button.jpg").convert_alpha(), 0.5)
    boutton_setting = Button(200, 175, pygame.image.load("images/commande.jpg").convert_alpha(), 2)

    fond = pygame.image.load("images/circuit_las_vegas.png").convert()
    fond = pygame.transform.scale_by(fond, 9)
    car = pygame.image.load("redbullf1.png").convert_alpha()
    car = pygame.transform.scale_by(car, 0.2)

    #image affiché
    rotcar = car
    #rectangle qui a les dimensions et les coordonnées de l'image
    rotcarrect = pygame.Surface.get_rect(rotcar)
    rotcarrect.center = (300, 200)
    print(rotcarrect.topleft)
    print(rotcarrect.bottomright)
    x, y = -14360, -2800
    vitesse = 0 

    pygame.key.set_repeat(10)
    angle = 40
    rotcar = pygame.transform.rotate(car, angle)
    rotcarrect = pygame.Surface.get_rect(rotcar)
    rotcarrect.center = (300, 200)
    continuer = True
    while continuer:

        xmin, xmax = int(-x + 280), int(-x + 321)
        ymin, ymax = int(-y + 175), int(-y + 225)

        if pause:
            rotcar.fill((52, 78, 91))
            fond.fill((52, 78, 91))
            boutton_resume.draw(fond)
            boutton_quit.draw(fond)
            boutton_setting.draw(fond)
            print("enfin!!")
        else:
            menu_pause("Option", font, color_text, 5, 5)

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
                    angle -= 1.5
                    rotcar = pygame.transform.rotate(car, angle)
                    rotcarrect = pygame.Surface.get_rect(rotcar)
                    rotcarrect.center = (300, 200)
                if event.key == pygame.K_LEFT:
                    angle += 1.5
                    rotcar = pygame.transform.rotate(car, angle)
                    rotcarrect = pygame.Surface.get_rect(rotcar)
                    rotcarrect.center = (300, 200)
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    
        if vitesse < -10:
            vitesse = -10
        if vitesse > 3:
            vitesse = 3
        vitesserotated = (cos(radians(angle)) * 0 - sin(radians(angle)) * vitesse, sin(radians(angle)) * 0 + cos(radians(angle)) * vitesse)
        x, y = x + vitesserotated[0], y - vitesserotated[1]


        for iligne in range(xmin, xmax):
            for icolonne in range(ymin, ymax):
                if fond.get_at((iligne, icolonne)) == (230, 230, 230): 
                    vitesse +=0.001
                    if vitesse > 0:
                        vitesse = 0 
        
        fenetre.blit(fond, (x, y))
        fenetre.blit(rotcar, rotcarrect.topleft)
        
        pygame.display.flip()


def barcelone():
    fenetre = pygame.display.set_mode((width, height))
    fond = pygame.image.load("images/circuit_Barcelone.png").convert()
    fond = pygame.transform.scale_by(fond, 7)
    car = pygame.image.load("redbullf1.png").convert_alpha()
    car = pygame.transform.scale_by(car, 0.2)
    #image affiché
    rotcar = car
    #rectangle qui a les dimensions et les coordonnées de l'image
    rotcarrect = pygame.Surface.get_rect(rotcar)
    rotcarrect.center = (300, 200)
    print(rotcarrect.topleft)
    print(rotcarrect.bottomright)
    x, y = -8845, -5250
    vitesse = 0 
    angle = 90
    rotcar = pygame.transform.rotate(car, angle)
    rotcarrect = pygame.Surface.get_rect(rotcar)
    rotcarrect.center = (300, 200)
    pygame.key.set_repeat(10)
    continuer = True
    while continuer:

        xmin, xmax = int(-x + 280), int(-x + 321)
        ymin, ymax = int(-y + 175), int(-y + 225)

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
                    angle -= 1.5
                    rotcar = pygame.transform.rotate(car, angle)
                    rotcarrect = pygame.Surface.get_rect(rotcar)
                    rotcarrect.center = (300, 200)
                if event.key == pygame.K_LEFT:
                    angle += 1.5
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
                if fond.get_at((iligne, icolonne)) == (230, 230, 230): 
                    vitesse +=0.5
                    if vitesse > 0:
                        vitesse = 0    


        fenetre.blit(fond, (x, y))
        fenetre.blit(rotcar, rotcarrect.topleft)
        pygame.display.flip()

def brésil():
    fenetre = pygame.display.set_mode((width, height))
    fond = pygame.image.load("images/circuit_Brésil.png").convert()
    fond = pygame.transform.scale_by(fond, 6)
    car = pygame.image.load("redbullf1.png").convert_alpha()
    car = pygame.transform.scale_by(car, 0.2)
    #image affiché
    rotcar = car
    #rectangle qui a les dimensions et les coordonnées de l'image
    rotcarrect = pygame.Surface.get_rect(rotcar)
    rotcarrect.center = (300, 200)
    print(rotcarrect.topleft)
    print(rotcarrect.bottomright)
    x, y = -3500, -1385
    vitesse = 0 

    pygame.key.set_repeat(10)
    angle = 110
    rotcar = pygame.transform.rotate(car, angle)
    rotcarrect = pygame.Surface.get_rect(rotcar)
    rotcarrect.center = (300, 200)
    continuer = True
    while continuer:

        xmin, xmax = int(-x + 280), int(-x + 321)
        ymin, ymax = int(-y + 175), int(-y + 225)

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
                    angle -= 1.5
                    rotcar = pygame.transform.rotate(car, angle)
                    rotcarrect = pygame.Surface.get_rect(rotcar)
                    rotcarrect.center = (300, 200)
                if event.key == pygame.K_LEFT:
                    angle += 1.5
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
                if fond.get_at((iligne, icolonne)) == (230, 230, 230): 
                    vitesse +=0.5
                    if vitesse > 0:
                        vitesse = 0    


        fenetre.blit(fond, (x, y))
        fenetre.blit(rotcar, rotcarrect.topleft)
        pygame.display.flip()

def italie():
    fenetre = pygame.display.set_mode((width, height))
    fond = pygame.image.load("images/circuit_Italie.png").convert()
    fond = pygame.transform.scale_by(fond, 6)
    car = pygame.image.load("redbullf1.png").convert_alpha()
    car = pygame.transform.scale_by(car, 0.2)
    #image affiché
    rotcar = car
    #rectangle qui a les dimensions et les coordonnées de l'image
    rotcarrect = pygame.Surface.get_rect(rotcar)
    rotcarrect.center = (300, 200)
    print(rotcarrect.topleft)
    print(rotcarrect.bottomright)
    x, y = -7650, -1500
    vitesse = 0 

    pygame.key.set_repeat(10)
    angle = 90
    rotcar = pygame.transform.rotate(car, angle)
    rotcarrect = pygame.Surface.get_rect(rotcar)
    rotcarrect.center = (300, 200)
    continuer = True
    while continuer:

        xmin, xmax = int(-x + 280), int(-x + 321)
        ymin, ymax = int(-y + 175), int(-y + 225)

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
                    angle -= 1.5
                    rotcar = pygame.transform.rotate(car, angle)
                    rotcarrect = pygame.Surface.get_rect(rotcar)
                    rotcarrect.center = (300, 200)
                if event.key == pygame.K_LEFT:
                    angle += 1.5
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
                if fond.get_at((iligne, icolonne)) == (230, 230, 230): 
                    vitesse +=0.5
                    if vitesse > 0:
                        vitesse = 0    


        fenetre.blit(fond, (x, y))
        fenetre.blit(rotcar, rotcarrect.topleft)
        pygame.display.flip()

continuer = True
# Boucle principale

while continuer:   
    
    fenetre.fill((52, 78, 91))

    if game_start:
        barcelone_circuit.draw(fenetre)
        Brésil_circuit.draw(fenetre)
        Las_Vegas_circuit.draw(fenetre) 
        Italie_circuit.draw(fenetre)
        
    else:
        draw_text("Press SPACE to start", font, TEXT_COL, 120, 188)

    
    if pause:
        fenetre.fill((52, 78, 91))
        boutton_resume.draw(fenetre)
        boutton_quit.draw(fenetre)
        boutton_setting.draw(fenetre)
    else:
        menu_pause("Option", font, color_text, 5, 5)

    if setting:
        fenetre.fill((52, 78, 91))
        boutton_resume.draw(fenetre)
        touche = pygame.image.load("images/image_fleche.png").convert()
        touche = pygame.transform.scale_by(touche, 0.75)
        fenetre.blit(touche, (200, 200))

        

 #regarde si le bouton a été cliquée
    if Las_Vegas_circuit.clicked:
        las_vegas()
    if barcelone_circuit.clicked:
        barcelone()
    if Brésil_circuit.clicked:
        brésil()
    if Italie_circuit.clicked:
        italie()

    if boutton_resume.clicked:
        pause = False
        setting = False
    if boutton_quit.clicked:
        pygame.quit()
    if boutton_setting.clicked:
        
        setting = True


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_start = True 
            if event.key == pygame.K_ESCAPE:
                pause = True
        if event.type == pygame.QUIT :
            pygame.quit()
            continuer = False

        
    pygame.display.update()    
    pygame.display.flip()