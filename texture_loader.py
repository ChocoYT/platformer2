import pygame
import os

path = f"{os.getcwd()}\\platformer2"

class Texture_loader():
    def __init__(self):
        self.path = f"{path}\\Sprites\\"
        self.tile_sheet = self.load("Terrain\\platform_single")

    def load(self, image):
        return pygame.image.load(f"{self.path}{image}.png")