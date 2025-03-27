import sys
import pygame

def check_events(gm_settings, screen, player):
    """Kontrolli klaviatuuri sündmusi"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False
            
def update_screen(gm_settings, screen, player):
    """Uuenda pilti ekraanil ja loo uus ekraan"""
    # lisa ekraani taust
    screen.fill(gm_settings.bg_color)
    # lisa mängija ekraanile
    player.blit_me()
    # esinda viimast ekraani
    pygame.display.flip()
