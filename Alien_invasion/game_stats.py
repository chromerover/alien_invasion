#!/usr/bin/env python
# -*- coding:utf-8 -*-
class GameStats():

    def __init__(self,ai_setting):
        self.ai_setting = ai_setting
        self.reset_stats()
        self.game_active = False

        self.read_score()
        aa = int(self.score1)
        self.high_score = aa


    def reset_stats(self):
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0
        self.level = 1

    def read_score(self):
        with open('score.txt') as file:
            self.score1 = file.read()


