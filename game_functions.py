import sys
import pygame


#
pygame.init()
ADDBUBBLE = pygame.USEREVENT + 1
pygame.time.set_timer(ADDBUBBLE, 250)

def check_events(gm_set, screen, player, bubbles):
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
        elif event.type == ADDBUBBLE:
            create_bubble(gm_set, screen, bubbles)
            
def create_bubble(gm_set, screen, bubbles):
    new_bubble = Bubble(screen, gm_set)
    bubbles.add(new_bubble)
            
def update_screen(gm_set, screen, player, bubbles):
    """Uuenda pilti ekraanil ja loo uus ekraan"""
    # lisa ekraani taust
    screen.fill(gm_set.bg_color)
    # lisa mängija ekraanile
    player.blit_me()
    # add bubbles to screen
    for bubble in bubbles:
        bubble.blit_me()
    # lisa mull ekraanile
    bubble.blit_me()
    # esinda viimast ekraani
    pygame.display.flip()
