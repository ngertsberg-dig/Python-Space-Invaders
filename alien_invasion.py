import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    SETTINGS = Settings()
    screen = pygame.display.set_mode((SETTINGS.screen_width, SETTINGS.screen_height))
    ship = Ship(SETTINGS, screen)
    bullets = Group()
    while True:
        gf.check_events(SETTINGS, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(SETTINGS, screen, ship, bullets)
        
        pygame.display.flip()

run_game()