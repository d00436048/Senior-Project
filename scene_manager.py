import pygame

class scene_intro:

    def __init__(self, screen):
        self.screen = screen

    def load_scene(self):
        self.logo = pygame.image.load("assets/images/menus/Games.png")
        
    def display_scene(self):
        self.screen.blit(self.logo, (0, 0))


class scene_main:

    def __init__(self, screen):
        self.screen = screen
        self.image_x = 512

    def load_scene(self):
        self.logo = pygame.image.load("assets/images/game/objects/missle.png")
        
    def display_scene(self):
        self.screen.blit(self.logo, (self.image_x, 300))

    def run_main(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.image_x += 5


class scene_mode_select:

    def __init__(self, screen):
        self.screen = screen

    def load_scene(self):
        self.logo = pygame.image.load("assets/images/game/sprites/green_tank_bottom.png")
        
    def display_scene(self):
        self.screen.blit(self.logo, (512, 300))

