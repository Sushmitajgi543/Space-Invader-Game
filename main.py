# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:53:32 2020

@author: sushmita singh

"""
import pygame
import random
import math

# initializing all pygame modules
pygame.init()
score = 0
# creating window
screen = pygame.display.set_mode((800, 700))

# inserting logo image
logo = pygame.image.load("image\logo.png")
pygame.display.set_icon(logo)

# Changing the tittle of the window
pygame.display.set_caption("SPACE INVADER @BY SUSHMITA SINGH")

# score diplay
# implenting font style
font = pygame.font.Font("freesansbold.ttf", 20)
textx = 10
texty = 10

# SPACESHIP for player
player = pygame.image.load("image/spaceship.png")
playerx = 360
playery = 600
playerx_change = 0
playery_change = 0

# ENEMY of game
#empty list for append 6 enemy
enemy = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
enemyno =6
#appending enemy
for en in range(enemyno):
    enemy.append(pygame.image.load('image/enemy.png'))
    enemyx.append( random.randint(0, 740))
    enemyy.append( random.randint(15, 120))
    enemyx_change.append( 0.3)
    enemyy_change.append(40)


    # function for enemy image
    def enemyImg(x, y):
        screen.blit(enemy[en], (x, y))

# Bullet for firing
bullet = pygame.image.load('image/bullet.png')
bulletx = 0
bullety = 600
bullex_change = 0
bullety_change = 1  # it will decide the speed on bullet
bullet_state = "ready"


# ready = we can't see the bullet on screen surface
# fire = we can see the bullet on the screen surface


# function for player image
def playerImg(x, y):
    screen.blit(player, (x, y))


# function fore bullet image
# for changing state of bullet to fire
def bulletFire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 5, y - 17))  # changing x and y value to fire bullet from top and bottom of spaceship


# function to etect collision of bullet and enemy
def collision(enemyx, enemyy, bulletx, bullety):
    # measuring distance bet two co-ordinates
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


# function to display text
def show(x, y):
    text_score = font.render("score:" + str(score), True, (0, 0, 0))  # message to display
    screen.blit(text_score,(x, y))


run = True
# game loop
while run:

    # fill color to the surface of window
    screen.fill((60, 60, 110))  # CHANGING THE COLOR OF WINDOW

    for event in pygame.event.get():  # it will call all events of pyagme
        # quit the program.
        if event.type == pygame.QUIT:  # IT WIL ENABLLE CLOSE BUTTON TO CLOSE THE WINDOW
            run = False

        # checking wheather the key is pressed
        if event.type == pygame.KEYDOWN:

            # movement of player  on pressing left arrow key
            if event.key == pygame.K_LEFT:
                playerx_change = -0.3

            # movement of player  on pressing right arrow key
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.3

            # when we press space bar bullet will be fired
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":  # bullet will only fired when it is in ready state
                    bulletx = playerx
                    bulletFire(bulletx, bullety)  # calling bulletimage function

        # checking wheather the key is RELEASED
        if event.type == pygame.KEYUP:
            # stop the player if key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0


    # for the movement of player space ship ; changing the x co-ordinates
    playerx += playerx_change

    # setting boundaries:
    # when spaceship will touch the left boundary is will stop
    if playerx <= 0:
        playerx = 0

    # when spaceship will touch the right boundary is will stop
    if playerx >= 740:
        playerx = 740

    playerImg(playerx, playery)  # calling playerimage function


    for en in range(enemyno):
        # for the movement of enemy ; changing the x co-ordinates
        enemyx[en] += enemyx_change[en]

        # enemy boundary collision
        if enemyx[en] <= 0:
            enemyx[en] = 0
            enemyx_change[en] = 0.3  # when enemy touches left boundary move back to right direction
            enemyy[en] += enemyy_change[en]

        if enemyx[en] >= 740:
            enemyx[en] = 740
            enemyy[en] += enemyy_change[en]
            enemyx_change[en] = -0.3  # when enemy touches right boundary move back to left direction

        # Calling collision function
        coll = collision(enemyx[en], enemyy[en], bulletx, bullety)
        if coll:
            bullety = 480
            bullet_state = "ready"
            score += 10  # score will inrease by 10 when bullet hits enemy
            # new enemy will appear after collision
            enemyx[en] = random.randint(0, 740)
            enemyy[en] = random.randint(15, 120)
        enemyImg(enemyx[en], enemyy[en])  # calling enemyimage function

    # multiple bullet but when one bullet go beyond the boundary
    if bullety <= 0:
        bullety = 600
        bullet_state = "ready"


    # Bullet movement
    if bullet_state == "fire":
        bulletFire(bulletx, bullety)
        bullety -= bullety_change

    # callinf score show function
    show(textx, texty)

    # updating the changes in the window
    # Draws the surface object to the screen.
    pygame.display.update()
