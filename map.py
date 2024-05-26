import pygame

from player import Player
from tile import Tile
from enemy import Enemy

class Map(pygame.surface.Surface):
    def __init__(self, level_data, tile_size, screen_dimensions):
        width, height = screen_dimensions
        pygame.surface.Surface.__init__(self, size = (width, height))
        self.setup(level_data, tile_size)

    def setup(self, mapData, tile_size):
        # creates sprite groups
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()

        # removes all unnescessary punctuation
        mapData = mapData.replace("\n", "").replace("'", "")
        mapData = mapData.split(",")

        # places sprites at the desired spots
        for row_index, row in enumerate(mapData):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == "X":
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
            
                if cell == "P":
                    player = Player((x, y), tile_size)
                    self.player.add(player)

                if cell == "E":
                    enemy = Enemy((x, y), tile_size)
                    self.enemies.add(enemy)
                           

    def _render(self):  # updates and renders the sprites on the 'Map' surface
        self.fill((0, 0, 0))

        self.tiles.draw(self)
        self.tiles.update()

        self.player.draw(self)
        self.tiles.update()

        self.enemies.draw(self)
        self.enemies.update()
