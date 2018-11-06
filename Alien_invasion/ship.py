#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx

    def blitme(self,screen):
        screen.blit(self.image,self.rect)

    def ship_update(self,ai_setting):
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.x += ai_setting.ship_speed
        if self.moving_left and self.rect.left >= 0:
            self.rect.x -= ai_setting.ship_speed

