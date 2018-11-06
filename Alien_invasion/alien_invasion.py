import pygame
from pygame.sprite import Group
from setting import Setting
import game_function as gf
from ship import Ship
from game_stats import GameStats
from botton import Botton
from scoreboard import ScoreBoard

def run_game():
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Alien Invasi   on')
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    gf.create_alien_fleet(ai_setting,aliens,screen)
    stats = GameStats(ai_setting)
    play_botton = Botton(screen,'Play')
    sb = ScoreBoard(screen,ai_setting,stats)

    while True:
        screen.fill(ai_setting.bg_color)
        gf.check_events(ship, bullets,screen,ai_setting,play_botton,stats,aliens,sb)

        if stats.game_active:
            ship.ship_update(ai_setting)
            gf.update_aliens(aliens,ai_setting,ship,stats,bullets,screen,sb)
            gf.update_bullets(bullets, aliens, screen, ai_setting,stats,sb)

        gf.screen_update(screen,ai_setting,ship,bullets,aliens,play_botton,stats,sb)

run_game()

