import pygame

class gameplay_ui:

    def __init__(self, screen, p1_name, p2_name, p1_tank_index, p2_tank_index):
        self.screen = screen
        self.p1_bg_x = 5
        self.p1_bg_y = 5
        self.p2_bg_x = 715
        self.p2_bg_y = 495
        
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_tank_index = p1_tank_index
        self.p2_tank_index = p2_tank_index

        self.player_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 25)

        self.gameplay_1_active = False
        


    def load_game_2_ui(self):
        self.p1_bg = pygame.image.load("assets/images/game/ui/p1_bg2.png").convert_alpha()
        self.p2_bg = pygame.image.load("assets/images/game/ui/p2_bg2.png").convert_alpha()
        self.p1_text = self.player_font.render(f'{self.p1_name}', True, (255, 255, 255))
        self.p2_text = self.player_font.render(f'{self.p2_name}', True, (255, 255, 255))

        self.player_icon_bg = pygame.image.load("assets/images/game/ui/player_icon_bg.png").convert_alpha()
        self.player_green = pygame.image.load("assets/images/menus/tank icon green.png").convert_alpha()
        self.player_blue = pygame.image.load("assets/images/menus/tank icon blue.png").convert_alpha()
        self.player_red = pygame.image.load("assets/images/menus/tank icon red.png").convert_alpha()
        self.player_gray = pygame.image.load("assets/images/menus/tank icon gray.png").convert_alpha()
        self.player_green = pygame.transform.scale_by(self.player_green, 3.5)
        self.player_blue = pygame.transform.scale_by(self.player_blue, 3.5)
        self.player_red = pygame.transform.scale_by(self.player_red, 3.5)
        self.player_gray = pygame.transform.scale_by(self.player_gray, 3.5)
        self.gameplay_1 = False

    def render_ui(self):
        self.screen.blit(self.p1_bg, (self.p1_bg_x, self.p1_bg_y))
        self.screen.blit(self.p2_bg, (self.p2_bg_x, self.p2_bg_y))
        self.screen.blit(self.p1_text, (self.p1_bg_x+100, self.p1_bg_y+50))
        self.screen.blit(self.p2_text, (self.p2_bg_x+85,self.p2_bg_y+50))

        if self.p1_tank_index == 0:
            self.screen.blit(self.player_green, (self.p1_bg_x+8, self.p1_bg_y+25))
        elif self.p1_tank_index == 1:
            self.screen.blit(self.player_blue, (self.p1_bg_x+8, self.p1_bg_y+25))
        elif self.p1_tank_index == 2:
            self.screen.blit(self.player_red, (self.p1_bg_x+8, self.p1_bg_y+25))
        elif self.p1_tank_index == 3:
            self.screen.blit(self.player_gray, (self.p1_bg_x+8, self.p1_bg_y+25))

        if self.p2_tank_index == 0:
            p2_green = pygame.transform.flip(self.player_green, True, False)
            self.screen.blit(p2_green, (self.p2_bg_x+205, self.p2_bg_y+25))
        elif self.p2_tank_index == 1:
            p2_blue = pygame.transform.flip(self.player_blue, True, False)
            self.screen.blit(p2_blue, (self.p2_bg_x+205, self.p2_bg_y+25))
        elif self.p2_tank_index == 2:
            p2_red = pygame.transform.flip(self.player_red, True, False)
            self.screen.blit(p2_red, (self.p2_bg_x+205, self.p2_bg_y+25))
        elif self.p2_tank_index == 3:
            p2_gray = pygame.transform.flip(self.player_gray, True, False)
            self.screen.blit(p2_gray, (self.p2_bg_x+205, self.p2_bg_y+25))

        if self.gameplay_1:
            if self.p1_score == 0:
                self.p1_score_img = pygame.image.load("assets/images/game/ui/score_bg.png").convert_alpha()
            elif self.p1_score == 1:
                self.p1_score_img = pygame.image.load("assets/images/game/ui/score_1_bg.png").convert_alpha()
            elif self.p1_score == 2:
                self.p1_score_img = pygame.image.load("assets/images/game/ui/score_2_bg.png").convert_alpha()
            
            if self.p2_score == 0:
                self.p2_score_img = pygame.image.load("assets/images/game/ui/score_bg.png").convert_alpha()
            elif self.p2_score == 1:
                self.p2_score_img = pygame.image.load("assets/images/game/ui/score_1_bg.png").convert_alpha()
            elif self.p2_score == 2:
                self.p2_score_img = pygame.image.load("assets/images/game/ui/score_2_bg.png").convert_alpha()

            self.screen.blit(self.scene_text, (600,300))
            self.screen.blit(self.p1_score_img, (self.p1_bg_x + 300, self.p1_bg_y + 25))
            self.screen.blit(self.p2_score_img, (self.p2_bg_x - 135, self.p2_bg_y + 20))


    def update_game_2_ui(self):
        pass

    def load_game_1_ui(self, p1_score, p2_score):
        self.p1_bg = pygame.image.load("assets/images/game/ui/p1_bg2.png").convert_alpha()
        self.p2_bg = pygame.image.load("assets/images/game/ui/p2_bg2.png").convert_alpha()
        self.p1_text = self.player_font.render(f'{self.p1_name}', True, (255, 255, 255))
        self.p2_text = self.player_font.render(f'{self.p2_name}', True, (255, 255, 255))
        self.scene_text = self.player_font.render("GAMEPLAY 1", True, (255, 255, 255))

        self.player_icon_bg = pygame.image.load("assets/images/game/ui/player_icon_bg.png").convert_alpha()
        self.player_green = pygame.image.load("assets/images/menus/tank icon green.png").convert_alpha()
        self.player_blue = pygame.image.load("assets/images/menus/tank icon blue.png").convert_alpha()
        self.player_red = pygame.image.load("assets/images/menus/tank icon red.png").convert_alpha()
        self.player_gray = pygame.image.load("assets/images/menus/tank icon gray.png").convert_alpha()
        self.player_green = pygame.transform.scale_by(self.player_green, 3.5)
        self.player_blue = pygame.transform.scale_by(self.player_blue, 3.5)
        self.player_red = pygame.transform.scale_by(self.player_red, 3.5)
        self.player_gray = pygame.transform.scale_by(self.player_gray, 3.5)
        self.gameplay_1 = True

        self.p1_score = p1_score
        self.p2_score = p2_score
        self.p1_score_img = pygame.image.load("assets/images/game/ui/score_bg.png").convert_alpha()
        self.p2_score_img = pygame.image.load("assets/images/game/ui/score_bg.png").convert_alpha()
