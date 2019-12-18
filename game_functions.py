import sys
import pygame
from bullet import Bullet


def check_events(SETTINGS, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, SETTINGS, screen, ship, bullets )
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, SETTINGS, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
        #create new bullet
        new_bullet = Bullet(SETTINGS, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(SETTINGS, screen, ship, bullets):
    screen.fill(SETTINGS.screen_bg)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()