import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        # initialises and sets up the tiles
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        
        self.image = pygame.Surface((size, size))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(topleft = pos)
        