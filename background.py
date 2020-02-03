import pygame
import sys
from pygame.locals import *




class Background(pygame.sprite.Sprite):
    def __init__(self, ai_game, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def blitme(self):
    	self.screen.blit(self.image, self.rect)