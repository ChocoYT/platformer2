import keyboard
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        # initialises and sets up the player
        pygame.sprite.Sprite.__init__(self)
        self.size = size

        self.image = pygame.Surface((size, size))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft = pos)

        self.rect.x, self.rect.y = pos
        self.x_vel = 0
        self.y_vel = 0

        self.on_ground = False

    def horizontal_movement(self, speed, collisions):
        # applies x velocity to player
        self.rect.x += self.x_vel
        if self.collide(collisions):
            while self.collide(collisions):
                # moves player out of the block they are colliding with
                if self.x_vel > 0:
                    self.rect.x -= 1
                else:
                    self.rect.x += 1
            self.x_vel = 0

        # applies x movement force and friction
        self.x_vel += ((keyboard.is_pressed("D") or keyboard.is_pressed("RIGHT")) - (keyboard.is_pressed("A") or keyboard.is_pressed("LEFT"))) * speed
        self.x_vel *= 0.85

    def vertical_movement(self, collisions):
        # applies y velocity to player
        self.rect.y -= self.y_vel
        if self.collide(collisions):
            while self.collide(collisions):
                # moves player out of the block they are colliding with
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
        # applies jump force
        if (keyboard.is_pressed("SPACE") or keyboard.is_pressed("W") or keyboard.is_pressed("UP")) and self.on_ground:
            self.y_vel = 20
        # caps the y velocity
        elif self.y_vel < -30:
            self.y_vel = -30

    def collide(self, spriteGroup):
        # checks if colliding
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            return True
        else:
            return False
        