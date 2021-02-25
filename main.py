# MADE BY: Lisette Spalding
# FILE NAME: main.py
# DATE CREATED: 02/25/2021
# DATE LAST MODIFIED: 02/25/2021
# PYTHON VER. USED: 3.8

##### IMPORTS #####
import pygame as pg
from pygame.locals import *
import random
from colors import *
from math import sin,cos,pi, radians
####### FIN #######

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill("BLUE")

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

        # self.speedX = -5
        # self.speedY = -5

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY

        if self.rect.left > WIDTH:
            self.rect.left = 0

        if self.rect.right < 0:
            self.rect.right = WIDTH

        if self.rect.top > HEIGHT:
            self.rect.top = 0

        if self.rect.bottom < 0:
            self.rect.bottom = HEIGHT


    def move_coords(self, angle, raidus, coords):
        self.theta = raidans(angle)
        return coords[0] + raidus * cos(self.theta), coords[1] + raidus * sin(self.theta)



###### SETUP ######
WIDTH = 360
HEIGHT = 480
FPS = 30

title = "Template"
####### FIN #######

###### PYGAME START ######
pg.init() # Initializing Pygame Library
pg.mixer.init() # Sounds

# Initializing objects
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()

# Creating sprite groups
allSprites = pg.sprite.Group()
playersGroup =  pg.sprite.Group()

# Creating Game Objects
player = Player()

# Adding objects to sprite Groups
allSprites.add(player)
playersGroup.add(player)

########## FIN ###########

####### GAME LOOP ########
def main():
    self.angle = 0
    self.rect = pygame.Rect(*coords, 20, 20)
    self.angle += 1

    self.move_coords(self.angle, 200, )

    running = True
    while running:
        clock.tick(FPS) # Controlling the loop

        ##### Processing input ######
    for event in pg.event.get(): # Getting a list of events that have happened
        if event.type == pg.QUIT: # This activates if the event is a QUIT event
            running = False # Setting "running" to False
    ############ FIN ############

    ## Make updates
    allSprites.update()

    #### Rendering / Drawing ####
    screen.fill(PURPLE)
    allSprites.draw(screen)
    ############ FIN ############

    # Showing the screen
    pg.display.flip() # This is always the last thing that we do in this loop

    # Ending game for when the quit button is clicked
    pg.quit()
    ########## FIN ###########

main()