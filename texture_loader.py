import pygame
from os import getcwd

path = getcwd()

class Texture_loader():
    def __init__(self):
        self.path = f"{path}\\Sprites\\"
        self.tile_sheet = self.load("Terrain\\platform_single")

    def load(self, image):
        return pygame.image.load(f"{self.path}{image}.png")