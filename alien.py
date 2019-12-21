import pygame
import os
from pygame.sprite import Sprite
class Alien(Sprite):

    def __init__(self,SETTINGS,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.SETTINGS = SETTINGS

        self.image = pygame.image.load(os.path.dirname(__file__) + '/images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width   
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)