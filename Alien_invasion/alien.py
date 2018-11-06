#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Aliens(Sprite):
    def __init__(self,ai_setting,screen):
        super().__init__()
        self.ai_setting = ai_setting
        self.screen = screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        self.x += self.ai_setting.alien_speed * self.ai_setting.fleet_direction
        self.rect.x = self.x


    def blitme(self,screen):
        screen.blit(self.image,self.rect)