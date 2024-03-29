import pygame
import os


class Ship():
    def __init__(self,SETTINGS,screen):
        
        self.SETTINGS = SETTINGS

        self.shipImage = ((os.path.dirname(__file__) + '\images\ship.bmp'))
        self.screen = screen
        self.image = pygame.image.load(self.shipImage)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.SETTINGS.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.SETTINGS.ship_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
       self.screen.blit(self.image,self.rect)
