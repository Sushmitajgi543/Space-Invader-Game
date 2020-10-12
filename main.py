# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:53:32 2020

@author: sushmita singh

"""
import pygame
import random

# initializing all pygame modules
pygame.init()

# creating window
screen = pygame.display.set_mode((800, 700))

# inserting logo image
logo = pygame.image.load("image\logo.png")
pygame.display.set_icon(logo)

# Changing the tittle of the window
pygame.display.set_caption("SPACE INVADER @BY SUSHMITA SINGH")

# SPACESHIP for player
player = pygame.image.load("image/spaceship.png")
playerx = 360
playery = 600
playerx_change = 0
playery_change = 0

# ENEMY of game
enemy = pygame.image.load('image/enemy.png')
enemyx = random.randint(0, 740)
enemyy = random.randint(15, 120)
enemyx_change = 0.3
enemyy_change = 40

# Bullet for firing
bullet = pygame.image.load('image/bullet.png')
bulletx = 0
bullety = 600
bullex_change = 0
bullety_change = 1 #it will decide the speed on bullet
bullet_state = "ready"


# ready = we can't see the bullet on screen surface
# fire = we can see the bullet on the screen surface


# function for player image
def playerImg(x, y):
    screen.blit(player, (x, y))


# function for enemy image
def enemyImg(x, y):
    screen.blit(enemy, (x, y))


# function fore bullet image
# for changing state of bullet to fire
def bulletFire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 5, y - 17))  # changing x and y value to fire bullet from top and bottom of spaceship


run = True
# game loop
while run:
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


    # fill color to the surface of window
    screen.fill((60, 60, 110))  # CHANGING THE COLOR OF WINDOW

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

    # for the movement of enemy ; changing the x co-ordinates
    enemyx += enemyx_change

    # enemy boundary collision
    if enemyx <= 0:
        enemyx = 0
        enemyx_change = 0.3  # when enemy touches left boundary move back to right direction
        enemyy += enemyy_change

    if enemyx >= 740:
        enemyx = 740
        enemyy += enemyy_change
        enemyx_change = -0.3  # when enemy touches right boundary move back to left direction

    enemyImg(enemyx, enemyy)  # calling enemyimage function


    #multiple bullet but when one bullet go beyond the boundary
    if bullety<=0:
        bullety =600
        bullet_state="ready"

    # Bullet movement
    if bullet_state == "fire":
        bulletFire(bulletx, bullety)
        bullety -= bullety_change

    # updating the changes in the window
    # Draws the surface object to the screen.
    pygame.display.update()
