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
from math import *
####### FIN #######

###### SETUP ######
WIDTH = 360
HEIGHT = 480
FPS = 30

title = "Template"
####### FIN #######

class NPC(pg.sprite.Sprite):
    def __init__(self):
        super(NPC, self).__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(LIGHT_BLUE)

        self.rect = self.image.get_rect()

        ## Placement
        self.rect.center = (WIDTH/2, HEIGHT/2)
        # self.rect.topleft = (0, 0)
        ## Placement FIN

        # This is the "center" that the sprite will orbit
        self.centerX = self.rect.centerx
        self.centerY = self.rect.centery

        self.angle = 1 # Current angle in radians

        self.radius = 50 # How far away from the center to orbit, measured in pixels

        self.speed = .1 # How fast to orbit, in radians per frame

        ### Normal speed variables
        self.speedx = 5
        self.speedy = 5

    def update(self):
        """ To use: self.update()
        This function updates the movement of the sprite on the screen. """
        ###### !!! CIRCLE MOVEMENT !!! ######
        # if self.angle <= 6.25:
        #     self.rect.centerx = self.radius * sin(self.angle) + self.centerX
        #     self.rect.centery = self.radius * cos(self.angle) + self.centerY
        #
        #     self.angle += self.speed
        ###### !!! MOVEMENT FINISH !!! ######

        ### Constant Movement
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        ### Constant Movement FIN

        ##### !! SCREEEN BOUNCING !! #####
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speedx *= -1

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speedy *= -1
        ##### !! BOUNCING FINISH !! ######

        ##### !! SCREEEN WRAPPING !! #####
        # if self.rect.left > WIDTH:
        #     self.rect.left = 0
        #
        # if self.rect.right < 0:
        #     self.rect.right = WIDTH
        #
        # if self.rect.top > HEIGHT:
        #     self.rect.top = 0
        #
        # if self.rect.bottom < 0:
        #     self.rect.bottom = HEIGHT
        ##### !! WRAPPING FINISH !! #####

        ##### !! SCREEN WARPING !! #####
        # if self.rect.left > WIDTH:
        #     self.rect.top = HEIGHT
        #     self.rect.centerx = WIDTH/2
        #     self.speedx = 0
        #     self.speedy = -5
        #
        # if self.rect.bottom < 0:
        #     print(self.rect.right)
        #     self.rect.right = 0
        #     self.rect.centery = HEIGHT/2
        #     self.speedx = 5
        #     self.speedy = 0
        ##### !! WARPING FINISH !! #####

        ###### !!! SQUARE MOVEMENT !!! ######
        # if self.rect.right >= WIDTH-1:
        #     self.speedx = 0
        #     self.speedy = -5
        #
        # if self.rect.top <= 1:
        #     self.speedx = -5
        #     self.speedy = 0
        #
        # if self.rect.left <= 1:
        #     self.speedx = 0
        #     self.speedy = 5
        #
        # if self.rect.bottom >= HEIGHT-1 and self.rect.right != WIDTH:
        #     self.speedx = 5
        #     self.speedy = 0
        ###### !!! MOVEMENT FINISH !!! ######

        ##### !!! TRIANGLE MOVEMENT !!! #####
        # if self.rect.centerx >= WIDTH/2:
        #     self.speedx = 5
        #     self.speedy = -8
        # if self.rect.bottomleft[0] > WIDTH and self.rect.bottomleft[1] <= 0:
        #     self.rect.bottomright = (0,0)
        #     self.speedx = 5
        #     self.speedy = 8
        ###### !!! MOVEMENT FINISH !!! ######

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50, 50))
        self.image.fill(PURPLE)

        self.rect = self.image.get_rect()

        ## Placement
        self.rect.center = (WIDTH/2, HEIGHT/2)
        ## Placement FIN

        ### Normal speed variables
        self.speedx = 5
        self.speedy = 5

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

####### GAME LOOP ########

###### PYGAME START ######
pg.init()  # Initializing Pygame Library
pg.mixer.init()  # Sounds

# Initializing objects
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()

# Creating sprite groups
allSprites = pg.sprite.Group()
playersGroup = pg.sprite.Group()
npcGroup = pg.sprite.Group()

# Creating Game Objects
player = Player()
npc = NPC()

# Adding objects to sprite Groups
allSprites.add(player)
playersGroup.add(player)

npcGroup.add(npc)
allSprites.add(npc)

########## FIN ###########

running = True
while running:
    clock.tick(FPS) # Controlling the loop

    ##### Processing input ######
    for event in pg.event.get(): # Getting a list of events that have happened
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.speedx = -5
            elif event.key == pg.K_RIGHT:
                player.speedx = 5
            elif event.key == pg.K_UP:
                player.speedy = -5
            elif event.key == pg.K_DOWN:
                player.speedy = 5

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                player.speedx = 0
            elif event.key == pg.K_RIGHT:
                player.speedx = 0
            elif event.key == pg.K_UP:
                player.speedy = 0
            elif event.key == pg.K_DOWN:
                player.speedy = 0


        ####### !!!! .. BASIC GRID MOVEMENT .. !!!! #######
        # if event.type == pg.KEYDOWN:
        #     if (event.key == pg.K_LEFT) or (event.key == pg.K_a) or \
        #             (event.key == pg.K_KP_4):
        #         player.rect.x -= 50
        #     elif (event.key == K_RIGHT) or (event.key == pg.K_d) or \
        #             (event.key == pg.K_KP_6):
        #         player.rect.x += 50
        #     elif (event.key == K_UP) or (event.key == pg.K_w) or \
        #             (event.key == pg.K_KP_8):
        #         player.rect.y -= 50
        #     elif (event.key == K_DOWN) or (event.key == pg.K_s) or \
        #             (event.key == pg.K_KP_2) or (event.key == pg.K_KP_5):
        #         player.rect.y += 50
        #     elif (event.key == pg.K_KP_7):
        #         player.rect.y -= 50
        #         player.rect.x -= 50
        #     elif (event.key == pg.K_KP_9):
        #         player.rect.y -= 50
        #         player.rect.x += 50
        #     elif (event.key == pg.K_KP_1):
        #         player.rect.y += 50
        #         player.rect.x -= 50
        #     elif (event.key == pg.K_KP_3):
        #         player.rect.y += 50
        #         player.rect.x += 50
        ####### !!!! .. BASIC GRID FINISHED .. !!!! #######

        if event.type == pg.QUIT: # This activates if the event is a QUIT event
            running = False # Setting "running" to False
    ############ FIN ############

    ## Make updates
    allSprites.update()

    #### Rendering / Drawing ####
    screen.fill(YELLOW)
    allSprites.draw(screen)
    ############ FIN ############

    # Showing the screen
    pg.display.flip() # This is always the last thing that we do in this loop

    # Ending game for when the quit button is clicked
pg.quit()
    ########## FIN ###########