import sys
import pygame
from bullet import Bullet
from alien import Alien

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
        fire_bullet(SETTINGS,bullets,screen,ship)
    if event.key == pygame.K_q:
        sys.exit()

def fire_bullet(SETTINGS,bullets,screen,ship):
    if(len(bullets) < SETTINGS.maximum_bullets):
        new_bullet = Bullet(SETTINGS, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(SETTINGS, screen, ship, aliens, bullets):
    screen.fill(SETTINGS.screen_bg)
    ship.blitme()
    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

def update_bullets(bulletGroup):
    for bullet in bulletGroup.copy():
        if(bullet.rect.bottom <= 0):
            bulletGroup.remove(bullet)

def get_number_aliens_x(SETTINGS,alien_width):
    available_space_x = SETTINGS.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(SETTINGS,screen,aliens,alien_number):
    alien = Alien(SETTINGS,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(SETTINGS,screen,aliens):
    alien = Alien(SETTINGS,screen)
    number_aliens_x = get_number_aliens_x(SETTINGS,alien.rect.width)
    for alien_number in range(number_aliens_x):
        create_alien(SETTINGS,screen,aliens,alien_number)