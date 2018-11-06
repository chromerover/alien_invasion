#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame.ftfont
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
    #显示得分信息的类
    def __init__(self,screen,ai_setting,stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats

        #显示得分信息时使用的字体设置
        self.text_color = 30,30,30
        self.font = pygame.ftfont._SysFont(None,48)

        #准备初始得分图像
        self.prep_score()
        self.prep_high_score(ai_setting)
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        self.level_img = self.font.render(str(self.stats.level),True,self.text_color,self.ai_setting.bg_color)
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def prep_high_score(self,ai_setting):
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_img = self.font.render(high_score_str,True,self.text_color,ai_setting.bg_color)

        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_score(self):
        #将得分渲染为一副渲染的图像
        round_score = int(round(self.stats.score,-1))

        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_setting.bg_color)
        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_img,self.high_score_rect)
        self.screen.blit(self.level_img,self.level_rect)
        self.ships.draw(self.screen)
