import pygame
import random

class Bubble(pygame.sprite.Sprite):
    """Klass mulli objektile"""
    
    def __init__(self, screen, gm_set):
        """ a """
        super(Bubble, self).__init__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        #
        self.bubble_radius = random.randint(gm_set.bubble_min_r, gm_set.bubble_max_r)
        #
        self.bubble = pygame.Surface((self.bubble_radius * 2, self.bubble_radius * 2), pygame.SRCALPHA)
        #
        self.bubble.set_colorkey(gm_set.bg_color)
        #
        self.bubble.set_alpha(128)
        #
        self.rect = pygame.draw.circle(
            self.bubble,
            (255, 255, 255)
            (self.bubble_radius, self.bubble_radius),
            self.bubble_radius,
            2)
        #
        self.rect = self.bubble.get_rect(
            center=(
                random.randint(gm_set.screen_height + 20, gm_set.screen_width + 100),
                random.randint(0, gm_set.screen_height),
            )
        )
        
    def blit_me(self):
        self.screen.blit(self.bubble, self.rect)
        
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill
