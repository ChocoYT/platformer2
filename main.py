import pygame
import sys
import configparser
from os import getcwd

from map import Map
from texture_loader import Texture_loader

# main game loop
if __name__ == '__main__':

    path = getcwd()

    # load the config
    defaults = configparser.ConfigParser()
    defaults.read(f"{path}\\defaults.ini")

    levels = configparser.ConfigParser()
    levels.read(f"{path}\\levels.ini")

    # initialise imports
    pygame.init()
    textures = Texture_loader()
    
    # setup the pygame screen and timer
    screen = pygame.display.set_mode((int(defaults['screen']['screen_width']), int(defaults['screen']['screen_height'])))
    pygame.display.set_caption("Platformer")
    clock = pygame.time.Clock()

    # create the level map (which also creates the player)
    level = Map(levels['level1']['map'], int(defaults['level']['tile_size']), (screen.get_width(), screen.get_height()))
    
    # start the game loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((0, 0, 0))

        # update the player
        player_sprite = level.player.sprite
        player_sprite.vertical_movement(level.tiles)
        player_sprite.horizontal_movement(1.5, level.tiles)

        # update the enemies
        enemy_sprites = level.enemies.sprites()
        for sprite_index, enemy_sprite in enumerate(enemy_sprites):
            enemy_sprite.vertical_movement(level.tiles)
            enemy_sprite.horizontal_movement(1, level.tiles)

        level._render()

        screen.blit(level, (0, 0))

        # update the pygame display (screen)
        pygame.display.update()

        clock.tick(int(defaults['defaults']['FPS']))

# EOF
pygame.quit()
sys.exit()
