#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import pygame
from bullet import Bullet
from time import sleep
from alien import Aliens


def check_events(ship,bullets,screen,ai_setting,play_botton,stats,aliens,sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write_score(stats)
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if play_botton.rect.collidepoint(mouse_x,mouse_y):
                check_play_botton(stats,aliens,bullets,ai_setting,screen,ship,play_botton,mouse_x,mouse_y,sb)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_q:
                write_score(stats)
                sys.exit()
            elif event.key == pygame.K_SPACE:
                if len(bullets) < 3:
                    bullet = Bullet(screen,ship,ai_setting)
                    bullets.add(bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False




def screen_update(screen,ai_setting,ship,bullets,aliens,play_botton,stats,sb):
    #screen.fill(ai_setting.bg_color)
    sb.show_score()
    ship.blitme(screen)
    #update_bullets(bullets,aliens,screen,ai_setting)
    aliens.draw(screen)
    if not stats.game_active:
        play_botton.draw_botton()
    pygame.display.flip()

def update_bullets(bullets,aliens,screen,ai_setting,stats,sb):
    for bullet in bullets:
        bullet.bullet_update(ai_setting)
        bullet.drawme(screen)
    for bullet in bullets.copy():
        if bullet.rect.y <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(bullets,aliens,ai_setting,screen,stats,sb)

def check_bullet_alien_collisions(bullets,aliens,ai_setting,screen,stats,sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()
        create_alien_fleet(ai_setting, aliens, screen)
        stats.level += 1
        sb.prep_level()
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_setting.alien_points * len(aliens)
        sb.prep_score()
    check_high_score(stats,sb,ai_setting)

def create_alien_fleet(ai_setting,aliens,screen):
    number = alien_number(ai_setting,screen)
    num_y = alien_number_y(ai_setting,screen)
    for numy in range(num_y):
        alien = Aliens(ai_setting,screen)
        alien_y = float(alien.rect.height + alien.rect.height * 2 * numy)

        for num in range(number):
            alien = Aliens(ai_setting,screen)
            alien.x = float(alien.rect.width + alien.rect.width * 2 * num)
            alien.rect.x = alien.x
            alien.rect.y = alien_y
            aliens.add(alien)


def alien_number(ai_setting,screen):
    alien = Aliens(ai_setting,screen)
    space = ai_setting.screen_width - alien.rect.width * 2
    number = int(space / (alien.rect.width * 2))
    return number

def alien_number_y(ai_setting,screen):
    alien = Aliens(ai_setting,screen)
    space = ai_setting.screen_height - alien.rect.height * 3
    number = int(space / (alien.rect.height * 2))
    return number

def update_aliens(aliens,ai_setting,ship,stats,bullets,screen,sb):
    check_fleet_edges(aliens,ai_setting)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,aliens,bullets,ai_setting,screen,ship,sb)
    check_aliens_bottom(screen,aliens,ship,stats,bullets,ai_setting,sb)

def ship_hit(stats,aliens,bullets,ai_setting,screen,ship,sb):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_alien_fleet(ai_setting,aliens,screen)
        ship.center_ship()
        sb.prep_ships()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)



def check_fleet_edges(aliens,ai_setting):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens,ai_setting)
            break

def change_fleet_direction(aliens,ai_setting):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop

    ai_setting.fleet_direction *= -1

def check_aliens_bottom(screen,aliens,ship,stats,bullets,ai_setting,sb):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats,aliens,bullets,ai_setting,screen,ship,sb)
            break

def check_play_botton(stats,aliens,bullets,ai_setting,screen,ship,play_botton,mouse_x,mouse_y,sb):
    botton_clicked =  play_botton.rect.collidepoint(mouse_x,mouse_y)
    if botton_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        ai_setting.initialize_dynamic_setting()
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()

        create_alien_fleet(ai_setting,aliens,screen)
        ship.center_ship()
        sb.prep_high_score(ai_setting)
        sb.prep_level()
        sb.prep_score()
        sb.prep_ships()

def check_high_score(stats,sb,ai_setting):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score(ai_setting)


def write_score(stats):
    with open ('score.txt','w') as file:
        file.write(str(stats.high_score))
        file.close()