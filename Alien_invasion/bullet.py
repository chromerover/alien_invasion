#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,screen,ship,ai_setting):
        super().__init__()
        self.rect = pygame.Rect(0,0,ai_setting.bullet_width,ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.bullet_color = 60,60,60
        #self.bullet_speed = 1.5
        self.y = float(self.rect.y)

    def drawme(self,screen):
        pygame.draw.rect(screen,self.bullet_color,self.rect)

    def bullet_update(self,ai_setting):
        self.y -= ai_setting.bullet_speed
        self.rect.y = self.y

