import pygame

from enum import Enum

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        # initialises and sets up the enemy
        pygame.sprite.Sprite.__init__(self)
        self.size = size

        self.image = pygame.Surface((size, size))
        self.image.fill((255, 0, 255))
        self.rect = self.image.get_rect(topleft = pos)

        self.rect.x, self.rect.y = pos
        self.y_vel = 0

        self.directions = Enum('direction', ['RIGHT', 'LEFT'])
        self.attribites = Enum('attribute', ['CANNOT_FALL'])

        self.on_ground = False
        self.facing = self.directions.RIGHT
        self.capabilities = [self.attribites.CANNOT_FALL]

    def horizontal_movement(self, speed, collisions):
        # moves enemy
        if self.facing == self.directions.RIGHT:
            self.rect.x += speed
        elif self.facing == self.directions.LEFT:
            self.rect.x -= speed
        else:
            print("Error - Enemy Direction")

        # changes enemy direction before falling off
        for i, capablity in  enumerate(self.capabilities):
            if capablity == self.attribites.CANNOT_FALL:
                self.rect.y += self.size
                if self.facing == self.directions.RIGHT:
                        self.rect.x += self.size
                elif self.facing == self.directions.LEFT:
                            self.rect.x -= self.size

                if not self.collide(collisions):
                    if self.facing == self.directions.RIGHT:
                        self.rect.x -= self.size
                        self.facing = self.directions.LEFT
                    elif self.facing == self.directions.LEFT:
                        self.rect.x += self.size
                        self.facing = self.directions.RIGHT
                else:
                    if self.facing == self.directions.RIGHT:
                        self.rect.x -= self.size
                    elif self.facing == self.directions.LEFT:
                        self.rect.x += self.size
                self.rect.y -= self.size

        # moves enemy out of wall
        if self.collide(collisions):
            if self.facing == self.directions.RIGHT:
                self.facing = self.directions.LEFT
                # moves out of wall if facing right
                while self.collide(collisions):
                    self.rect.x -= 1
            elif self.facing == self.directions.LEFT:
                self.facing = self.directions.RIGHT
                # moves out of wall if facing left
                while self.collide(collisions):
                    self.rect.x += 1

    def vertical_movement(self, collisions):
        # applies y velocity to enemy
        self.rect.y -= self.y_vel
        if self.collide(collisions):
            while self.collide(collisions):
                # moves enemy out of the block they are colliding with
                if self.y_vel > 0:
                    self.rect.y += 1
                    self.on_ground = False
                else:
                    self.rect.y -= 1
                    self.on_ground = True
            self.y_vel = 0
        else:
            self.on_ground = False
        self.y_vel -= 1

        # caps the y velocity
        if self.y_vel < -30:
            self.y_vel = -30

    def collide(self, spriteGroup):
        # checks if colliding
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            return True
        else:
            return False
        