import pygame
import numpy as np
import matplotlib as plt
import sys
import random

class world():
    def __init__(self,x,y):
        self.world_x_size = x
        self.world_y_size = y

        #initialize
        self.world_matrix=np.zeros((self.world_x_size,self.world_y_size))

        #make walls
        for y in range(0, self.world_y_size):
            for x in range(0, self.world_x_size):
                if (y == 0) or (y == self.world_y_size-1):
                    self.world_matrix[x,y] = 9
                if (x == 0) or (x == self.world_x_size-1):
                    self.world_matrix[x, y] = 9

        #place random food
        for y in range(0, self.world_y_size):
            for x in range(0, self.world_x_size):
                #if its a blank space
                if self.world_matrix[x,y] == 0:
                    #then give it a chance of putting down food.
                    if random.randint(0,10) == 2:
                        self.world_matrix[x,y] = 1

        #test enemy
        enemydrawn = False
        for y in range(0, self.world_y_size):
            if enemydrawn == False:
                for x in range(0, self.world_x_size):
                    # if its a blank space
                    if enemydrawn == False:
                        if self.world_matrix[x, y] == 0:
                            self.world_matrix[x, y] = 3
                            enemydrawn = True
                            break
            else:
                break

class player_entity():
    def __init__(self):
        self.world_x = -1
        self.world_y = -1
        self.score = 0
        self.ate_food = False
        self.hit_enemy = False
        self.died = False

    def spawn(self, world_matrix):
        playerplaced = False
        for y in range(0, world_matrix.world_y_size):
            if playerplaced == False:
                for x in range(0, world_matrix.world_x_size):
                    # if its a blank space
                    if playerplaced == False:
                        if world_matrix.world_matrix[x, y] == 0:
                            #write location to player object
                            self.world_x = x
                            self.world_y = y
                            #write location to world object -  these need to stay in sync.
                            world_matrix.world_matrix[x, y] = 2
                            playerplaced = True
                            break
            else:
                break

    def move(self, direction, the_world):
        #players pick up food automatically
        #players hit automatically
        if direction == 1:
            if (the_world.world_matrix[self.world_x][self.world_y-1] == 0) or (the_world.world_matrix[self.world_x][self.world_y-1] == 1) or (the_world.world_matrix[self.world_x][self.world_y-1] == 3):
                if (the_world.world_matrix[self.world_x][self.world_y-1] == 1):
                    self.score += 5
                if (the_world.world_matrix[self.world_x][self.world_y-1] == 3):
                    self.score += 100
                the_world.world_matrix[self.world_x][self.world_y] = 0
                the_world.world_matrix[self.world_x][self.world_y-1] = 2
                self.world_y += -1

        if direction == 3:
            if (the_world.world_matrix[self.world_x][self.world_y+1] == 0) or (the_world.world_matrix[self.world_x][self.world_y+1] == 1) or (the_world.world_matrix[self.world_x][self.world_y+1] == 3):
                if (the_world.world_matrix[self.world_x][self.world_y+1] == 1):
                    self.score += 5
                if (the_world.world_matrix[self.world_x][self.world_y+1] == 3):
                    self.score += 100
                the_world.world_matrix[self.world_x][self.world_y] = 0
                the_world.world_matrix[self.world_x][self.world_y + 1] = 2
                self.world_y += 1

        if direction == 2:
            if (the_world.world_matrix[self.world_x+1][self.world_y] == 0) or (the_world.world_matrix[self.world_x+1][self.world_y] == 1) or (the_world.world_matrix[self.world_x+1][self.world_y] == 3):
                if (the_world.world_matrix[self.world_x+1][self.world_y] == 1):
                    self.score += 5
                if (the_world.world_matrix[self.world_x+1][self.world_y] == 3):
                    self.score += 100
                the_world.world_matrix[self.world_x][self.world_y] = 0
                the_world.world_matrix[self.world_x + 1][self.world_y] = 2
                self.world_x += 1

        if direction == 4:
            if (the_world.world_matrix[self.world_x-1][self.world_y] == 0) or (the_world.world_matrix[self.world_x-1][self.world_y] == 1) or (the_world.world_matrix[self.world_x-1][self.world_y] == 3):
                if (the_world.world_matrix[self.world_x-1][self.world_y] == 1):
                    self.score += 5
                if (the_world.world_matrix[self.world_x-1][self.world_y] == 3):
                    self.score += 100
                the_world.world_matrix[self.world_x][self.world_y] = 0
                the_world.world_matrix[self.world_x - 1][self.world_y] = 2
                self.world_x += -1

    def look(self):
        #TODO

        # return view_matrix that has
        #   P for player
        #   . for space
        #   F for food
        #   E for enemy
        #   # for wall

        view_matrix = np.arange(9).reshape(3,3)
        return (view_matrix)

#WORLD SETUP
the_world = world(16,16)


#VIEW SETUP

imagesize = 50

apple = pygame.image.load("apple.png")
apple_rect = apple.get_rect()
apple = pygame.transform.scale(apple, (imagesize, imagesize))

player = pygame.image.load("player.png")
player_rect = player.get_rect()
player = pygame.transform.scale(player, (imagesize, imagesize))

enemy = pygame.image.load("enemy.png")
enemy_rect = player.get_rect()
enemy = pygame.transform.scale(enemy, (imagesize, imagesize))

wall = pygame.image.load("wall.png")
wall_rect = player.get_rect()
wall = pygame.transform.scale(wall, (imagesize, imagesize))

pygame.init()
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

speed = [2, 2]
white = 255, 255, 255

#Player setup
player1 = player_entity()
player1.spawn(the_world)
player2 = player_entity()
player2.spawn(the_world)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.move(1,the_world)
        if keys[pygame.K_d]:
            player1.move(2,the_world)
        if keys[pygame.K_s]:
            player1.move(3, the_world)
        if keys[pygame.K_a]:
            player1.move(4,the_world)

        if keys[pygame.K_UP]:
            player2.move(1,the_world)
        if keys[pygame.K_RIGHT]:
            player2.move(2,the_world)
        if keys[pygame.K_DOWN]:
            player2.move(3, the_world)
        if keys[pygame.K_LEFT]:
            player2.move(4,the_world)

    screen.fill(white)
    font = pygame.font.SysFont(None, 72)


    for y in range(0,the_world.world_y_size):
        for x in range(0,the_world.world_x_size):

            #text = font.render(str(x) + " " + str(y), True, (0, 128, 0))
            #screen.blit(text, (imagesize * x, imagesize * y))
            text = font.render(str("player1: " + str(player1.score) + "   player2: " + str(player2.score)), True, (0, 128, 0))
            screen.blit(text, (10, 10))

            #draw apple
            if the_world.world_matrix[x][y] == 1:
                screen.blit(apple, (imagesize * x,imagesize * y))
            #draw wall
            if the_world.world_matrix[x][y] == 9:
                screen.blit(wall, (imagesize * x, imagesize * y))
            # draw player
            if the_world.world_matrix[x][y] == 2:
                screen.blit(player, (imagesize * x, imagesize * y))
            # draw enemy
            if the_world.world_matrix[x][y] == 3:
                screen.blit(enemy, (imagesize * x, imagesize * y))
    pygame.display.flip()
