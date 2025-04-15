import pygame
import os
import time
import pytmx
import game_ui
import players
pygame.font.init()


class scene_intro:

    def __init__(self, screen):
        self.screen = screen
        self.frame_count = 0

    def load_scene(self):
        self.logo = pygame.image.load("assets/images/menus/Games.png").convert_alpha()

        #rect for fade
        self.rect_surface = pygame.Surface((1024, 600), pygame.SRCALPHA)
        self.rect_surface.fill((0, 0, 0, 0))

        #sound
        self.goat_sound = pygame.mixer.Sound("assets/sound/sound_effects/menus/donkey.mp3")
        self.goat_sound.set_volume(1.0)
        
    def display_scene(self, elapsed_time):
        self.screen.blit(self.logo, (0, 0))
        self.screen.blit(self.rect_surface, (0, 0))

        #rect
        if elapsed_time > 100:
            alpha_val = (elapsed_time - 3000)*.255
            alpha_val = max(0, min(255, int(alpha_val)))

            self.screen.blit(self.rect_surface, (0, 0))
            self.rect_surface.fill((0, 0, 0, alpha_val))

        #sound
        if self.frame_count < 1:
            self.goat_sound.play()
            self.frame_count += 1


class scene_main:

    def __init__(self, screen):
        self.screen = screen
        self.icon_y = 350
        self.icon_x = 400
        self.icon_bool = False
        self.title_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 100)
        self.select_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 25)



    def load_scene(self):
        self.title = self.title_font.render('TANKS', True, (255,0,0) )
        self.play_text = self.select_font.render('play', True, (255, 0, 0))
        self.settings_text = self.select_font.render('settings', True, (255, 255, 255))

        self.green_tank = pygame.image.load('assets/images/menus/tank icon green.png').convert_alpha()
        self.blue_tank = pygame.image.load('assets/images/menus/tank icon blue.png').convert_alpha()
        self.red_tank = pygame.image.load('assets/images/menus/tank icon red.png').convert_alpha()
        self.gray_tank = pygame.image.load('assets/images/menus/tank icon gray.png').convert_alpha()

        self.green_tank = pygame.transform.scale2x(self.green_tank)
        self.blue_tank = pygame.transform.scale2x(self.blue_tank)
        self.red_tank = pygame.transform.scale2x(self.red_tank)
        self.gray_tank = pygame.transform.scale2x(self.gray_tank)

        self.icon = pygame.image.load('assets/images/menus/tank icon green.png').convert_alpha()

    def display_scene(self, icon_index):
        self.screen.blit(self.title, (357, 100))
        if icon_index == 0:
            self.icon_y = 350
            self.play_text = self.select_font.render('play', True, (255, 0, 0))
            self.settings_text = self.select_font.render('settings', True, (255, 255, 255))
        else:
            self.icon_y = 400
            self.play_text = self.select_font.render('play', True, (255, 255, 255))
            self.settings_text = self.select_font.render('settings', True, (255, 0, 0))
        self.screen.blit(self.play_text, (485, 350))
        self.screen.blit(self.settings_text, (455, 400))
        self.screen.blit(self.icon, (self.icon_x, self.icon_y))

        self.screen.blit(self.green_tank, (93, 200))
        self.screen.blit(self.blue_tank, (93+256, 200))
        self.screen.blit(self.red_tank, (93+512, 200))
        self.screen.blit(self.gray_tank, (93+768, 200))

    def run_main(self):
        #icon animaton
        if self.icon_bool == False:
            self.icon_x -= 2
        if self.icon_x <= 399:
            self.icon_bool = True
        if self.icon_bool == True:
            self.icon_x += 2
        if self.icon_x >= 410:
            self.icon_bool = False

class scene_settings:

    def __init__(self, screen):
        self.screen = screen
        self.icon_y = 350
        self.icon_x = 400
        self.icon_bool = False
        self.title_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 100)
        self.select_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 25)
        self.text_color = (255, 255, 255)
        self.selected_text_color = (255, 0, 0)


    def load_scene(self):
        self.title = self.title_font.render('SETTINGS', True, (255,0,0) )
        self.sound_text = self.select_font.render('sound on', True, (255, 255, 255))
        self.exit_text = self.select_font.render('turn off', True, (255, 255, 255))
        self.back_text = self.select_font.render('back to main menu', True, (255, 255, 255))
        self.power_down_text = self.title_font.render('powering off', True, (255, 255, 255))

        self.icon = pygame.image.load('assets/images/menus/tank icon green.png').convert_alpha()
        self.bg = pygame.image.load('assets/images/menus/bg2.png').convert_alpha()


    def display_scene(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.title, (262, 50))
        self.screen.blit(self.sound_text, (450, 350))
        self.screen.blit(self.exit_text, (450, 400))
        self.screen.blit(self.back_text, (380, 450))
        self.screen.blit(self.icon, (self.icon_x, self.icon_y))

    def run_settings(self, icon_index, sound_on):
        #icon animaton
        if self.icon_bool == False:
            self.icon_x -= 2
        if self.icon_x <= 300:
            self.icon_bool = True
        if self.icon_bool == True:
            self.icon_x += 2
        if self.icon_x >= 310:
            self.icon_bool = False

        if icon_index == 0:
            self.icon_y = 350
            self.exit_text = self.select_font.render('turn off', True, (255, 255, 255))
            self.back_text = self.select_font.render('back to main menu', True, (255, 255, 255))
            if sound_on == True:
                self.sound_text = self.select_font.render("sound on", True, (255, 0, 0))
            else:
                self.sound_text = self.select_font.render("sound off", True, (255, 0, 0))
        
        elif icon_index == 1:
            self.icon_y = 400
            self.exit_text = self.select_font.render('turn off', True, (255, 0, 0))
            self.back_text = self.select_font.render('back to main menu', True, (255, 255, 255))
            if sound_on == True:
                self.sound_text = self.select_font.render("sound on", True, (255, 255, 255))
            else:
                self.sound_text = self.select_font.render("sound off", True, (255, 255, 255))
        else:
            self.icon_y = 450
            self.exit_text = self.select_font.render('turn off', True, (255, 255, 255))
            self.back_text = self.select_font.render('back to main menu', True, (255, 0, 0))
            if sound_on == True:
                self.sound_text = self.select_font.render("sound on", True, (255, 255, 255))
            else:
                self.sound_text = self.select_font.render("sound off", True, (255, 255, 255))


    def shutdown_pi(self):
        self.screen.blit(self.power_down_text, (262, 300))
        time.sleep(3)
        os.system("sudo shutdown -h now")


class scene_cheats:

    def __init(self, screen):
        self.screen = screen

    def load_scene(self):
        pass

    def display_scene(self):
        pass


class scene_mode_select:

    def __init__(self, screen):
        self.screen = screen
        self.icon_y = 350
        self.icon_x = 400
        self.icon_bool = False
        self.title_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 100)
        self.select_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 25)

    def load_scene(self):
        self.title = self.title_font.render('GAME MODE', True, (255,0,0) )
        self.versus_text = self.select_font.render('SUDDEN DEATH', True, (255, 255, 255))
        self.campeign_text = self.select_font.render('BEST 2/3  (beta)', True, (255, 255, 255))
        self.back_text = self.select_font.render('back to main menu', True, (255, 255, 255))


        self.icon = pygame.image.load('assets/images/menus/tank icon green.png').convert_alpha()
        self.bg = pygame.image.load('assets/images/menus/bg.png').convert_alpha()

        
    def display_scene(self):
        self.screen.blit(self.bg, (0,0))
        self.screen.blit(self.title, (210, 50))
        self.screen.blit(self.versus_text, (410, 350))
        self.screen.blit(self.campeign_text, (440, 400))
        self.screen.blit(self.back_text, (377, 450))
        self.screen.blit(self.icon, (self.icon_x, self.icon_y))

    def run_mode_select(self, icon_index):
        #icon animaton
        if self.icon_bool == False:
            self.icon_x -= 2
        if self.icon_x <= 325:
            self.icon_bool = True
        if self.icon_bool == True:
            self.icon_x += 2
        if self.icon_x >= 335:
            self.icon_bool = False

        if icon_index == 0:
            self.icon_y = 350
            self.versus_text = self.select_font.render('SUDDEN DEATH', True, (255, 0, 0))
            self.campeign_text = self.select_font.render('BEST 2/3  (beta)', True, (255, 255, 255))
            self.back_text = self.select_font.render('back to main menu', True, (255, 255, 255))
        elif icon_index == 1:
            self.icon_y = 400
            self.versus_text = self.select_font.render('SUDDEN DEATH', True, (255, 255, 255))
            self.campeign_text = self.select_font.render('BEST 2/3  (beta)', True, (255, 0, 0))
            self.back_text = self.select_font.render('back to main menu', True, (255, 255, 255))
        else:
            self.icon_y = 450
            self.versus_text = self.select_font.render('SUDDEN DEATH', True, (255, 255, 255))
            self.campeign_text = self.select_font.render('BEST 2/3  (beta)', True, (255, 255, 255))
            self.back_text = self.select_font.render('back to main menu', True, (255, 0, 0))


class scene_player_select_1:

    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 100)

    def load_scene(self):
        self.title = self.title_font.render('PLAYER SELECT 1', True, (255,0,0) )


    def display_scene(self):
        self.screen.blit(self.title, (70, 50))

    def run_player_select_1(self, icon_index):
        pass


class scene_player_select_2:

    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 100)
        self.name_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 25)
        self.red_selector_x = 257
        self.blue_selector_x = 427 # width = 70
        self.p1_x = 200
        self.p1_y = 250
        self.p2_x = 800
        self.p2_y = 250

        self.x_modifier = 30

        self.p1_selected = False
        self.p2_selected = False
        self.p1_tank_index = 0
        self.p2_tank_index = 0


        self.next_text_transparency = 255
        self.next_text_transparency_bool = False


    def load_scene(self):
        #text
        self.title = self.title_font.render('PLAYER SELECT 2', True, (255,0,0) )
        self.p1_text = self.name_font.render('P1', True, (255, 255, 255))
        self.p2_text = self.name_font.render('P2: ', True, (255, 255, 255))
        self.p1_text_tank = self.name_font.render('G.I. John', True, (255, 255, 255))
        self.p2_text_tank = self.name_font.render('COLD CUT', True, (255, 255, 255))
        self.tank_names = ['G.I. JOHN', 'COLD CUT', 'SHREDDER', 'MI-MI']
        self.next_text1 = self.title_font.render('P1', True, ( 255, 255, 255))
        self.next_text2 = self.name_font.render('press red to continue', True, ( 255, 255, 255))


        #image
        self.red_selector = pygame.image.load('assets/images/menus/red_selector.png').convert_alpha()
        self.blue_selector = pygame.image.load('assets/images/menus/blue_selector.png').convert_alpha()

        self.green_tank = pygame.image.load('assets/images/menus/tank icon green.png').convert_alpha()
        self.blue_tank = pygame.image.load('assets/images/menus/tank icon blue.png').convert_alpha()
        self.red_tank = pygame.image.load('assets/images/menus/tank icon red.png').convert_alpha()
        self.gray_tank = pygame.image.load('assets/images/menus/tank icon gray.png').convert_alpha()
        
        #change to 128x128
        self.green_tank = pygame.transform.scale2x(self.green_tank)
        self.blue_tank = pygame.transform.scale2x(self.blue_tank)
        self.red_tank = pygame.transform.scale2x(self.red_tank)
        self.gray_tank = pygame.transform.scale2x(self.gray_tank)

        #change to 256x256
        self.green_tank_256 = pygame.transform.scale2x(self.green_tank)
        self.blue_tank_256 = pygame.transform.scale2x(self.blue_tank)
        self.red_tank_256 = pygame.transform.scale2x(self.red_tank)
        self.gray_tank_256 = pygame.transform.scale2x(self.gray_tank)

        self.tank_icon_bg = pygame.image.load('assets/images/menus/tank icon bg.png').convert_alpha()

        self.banner = pygame.image.load('assets/images/menus/banner.png').convert_alpha()
        self.selected_rect = pygame.Surface((66, 66), pygame.SRCALPHA)
        self.selected_rect2 = pygame.Surface((66, 66), pygame.SRCALPHA)
        self.selected_rect.fill((0, 0, 0, 100))
        self.selected_rect2.fill((0, 0, 0, 100))

        self.bg = pygame.image.load('assets/images/menus/bg4.png').convert_alpha()

     

    def display_scene(self):
        self.screen.blit(self.bg, (0,0))
        self.screen.blit(self.title, (70, 50))

        self.screen.blit(self.tank_icon_bg, (249-self.x_modifier, 412))
        self.screen.blit(self.tank_icon_bg, (419-self.x_modifier, 412))
        self.screen.blit(self.tank_icon_bg, (589-self.x_modifier, 412))
        self.screen.blit(self.tank_icon_bg, (759-self.x_modifier, 412))

        #icon layer
        self.screen.blit(self.green_tank, (257-self.x_modifier, 430))
        self.screen.blit(self.blue_tank, (427-self.x_modifier, 430))
        self.screen.blit(self.red_tank, (597-self.x_modifier, 430))
        self.screen.blit(self.gray_tank, (767-self.x_modifier, 430))

        #selectors
        self.screen.blit(self.red_selector, (self.red_selector_x-self.x_modifier, 410))
        self.screen.blit(self.blue_selector, (self.blue_selector_x-self.x_modifier, 410))

        self.screen.blit(self.p1_text, (self.p1_x-30-self.x_modifier,self.p1_y-50))
        self.screen.blit(self.p2_text, (self.p2_x-30-self.x_modifier, self.p2_y-50))

    def run_player_select_2(self, icon_index, icon2_index):
        if icon_index == 0:
            self.p1_tank_index = 0
            self.red_selector_x = 247
            self.screen.blit(self.green_tank_256, (self.p1_x, self.p1_y))
            self.p1_text_tank = (self.name_font.render(self.tank_names[icon_index], True, (255, 255, 255)))
            self.screen.blit(self.p1_text_tank, (self.p1_x+20, self.p1_y-50))
        elif icon_index == 1:
            self.p1_tank_index = 1
            self.red_selector_x = 417
            self.screen.blit(self.blue_tank_256, (self.p1_x, self.p1_y))
            self.p1_text_tank = (self.name_font.render(self.tank_names[icon_index], True, (255, 255, 255)))
            self.screen.blit(self.p1_text_tank, (self.p1_x+20, self.p1_y-50))
        elif icon_index == 2:
            self.p1_tank_index = 2
            self.red_selector_x = 587
            self.screen.blit(self.red_tank_256, (self.p1_x, self.p1_y))
            self.p1_text_tank = (self.name_font.render(self.tank_names[icon_index], True, (255, 255, 255)))
            self.screen.blit(self.p1_text_tank, (self.p1_x+20, self.p1_y-50))
        elif icon_index == 3:
            self.p1_tank_index = 3
            self.red_selector_x = 757
            self.screen.blit(self.gray_tank_256, (self.p1_x, self.p1_y))
            self.p1_text_tank = (self.name_font.render(self.tank_names[icon_index], True, (255, 255, 255)))
            self.screen.blit(self.p1_text_tank, (self.p1_x+20, self.p1_y-50))
        else:
            icon_index = 0
            self.p1_tank_index = 0
            self.red_selector_x = 247
            self.screen.blit(self.green_tank_256, (self.p1_x, self.p1_y))
            self.p1_text_tank = (self.name_font.render(self.tank_names[icon_index], True, (255, 255, 255)))
            self.screen.blit(self.p1_text_tank, (self.p1_x+20, self.p1_y-50))

        if icon2_index == 0:
            self.p2_tank_index = 0
            self.blue_selector_x = 247
            self.screen.blit(self.green_tank_256, (self.p2_x, self.p2_y))
            self.p2_text_tank = (self.name_font.render(self.tank_names[icon2_index], True, (255, 255, 255)))
            self.screen.blit(self.p2_text_tank, (self.p2_x+20, self.p2_y-50))
        elif icon2_index == 1:
            self.p2_tank_index = 1
            self.blue_selector_x = 417
            self.screen.blit(self.blue_tank_256, (self.p2_x, self.p2_y))
            self.p2_text_tank = (self.name_font.render(self.tank_names[icon2_index], True, (255, 255, 255)))
            self.screen.blit(self.p2_text_tank, (self.p2_x+20, self.p2_y-50))
        elif icon2_index == 2:
            self.p2_tank_index = 2
            self.blue_selector_x = 587
            self.screen.blit(self.red_tank_256, (self.p2_x, self.p2_y))
            self.p2_text_tank = (self.name_font.render(self.tank_names[icon2_index], True, (255, 255, 255)))
            self.screen.blit(self.p2_text_tank, (self.p2_x+20, self.p2_y-50))
        elif icon2_index == 3:
            self.p2_tank_index = 3
            self.blue_selector_x = 757
            self.screen.blit(self.gray_tank_256, (self.p2_x, self.p2_y))
            self.p2_text_tank = (self.name_font.render(self.tank_names[icon2_index], True, (255, 255, 255)))
            self.screen.blit(self.p2_text_tank, (self.p2_x+20, self.p2_y-50))
        else:
            icon2_index = 0
            self.blue_selector_x = 247
            self.screen.blit(self.green_tank_256, (self.p2_x, self.p2_y))
            self.p2_text_tank = (self.name_font.render(self.tank_names[icon2_index], True, (255, 255, 255)))
            self.screen.blit(self.p2_text_tank, (self.p2_x+20, self.p2_y-50))


        #banner
        if self.p1_selected:
            self.screen.blit(self.selected_rect, (self.red_selector_x+2-self.x_modifier, 412))
        if self.p2_selected:
            self.screen.blit(self.selected_rect2,(self.blue_selector_x+2-self.x_modifier, 412))
        if self.p1_selected and self.p2_selected:
            self.screen.blit(self.banner, (0, 200))
            self.screen.blit(self.next_text1, (450, 225))
            self.screen.blit(self.next_text2, (350, 305))
            if self.next_text_transparency_bool == False:
                self.next_text_transparency -= 8
            if self.next_text_transparency <= 0:
                self.next_text_transparency_bool = True
            if self.next_text_transparency_bool == True:
                self.next_text_transparency += 8
            if self.next_text_transparency >= 255:
                self.next_text_transparency_bool = False
            self.next_text1.set_alpha(self.next_text_transparency)
            self.next_text2.set_alpha(self.next_text_transparency)




    #helpers
    def get_p1_select(self):
        return self.p1_selected
    
    def get_p2_select(self):
        return self.p2_selected
    
    def set_p1_select(self, selected):
        self.p1_selected = selected
    
    def set_p2_select(self, selected):
        self.p2_selected = selected


class scene_level_select:

    def __init__(self, screen):
        self.screen = screen

        


    def load_scene(self):
        self.title_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 50)
        self.large_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 100)
        self.button_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 25)
        self.random_level_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 200)
        self.random_level_small_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 75)
        self.small_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 60)

        self.top_icon_x = 175
        self.bottom_icon_x = 175
        self.icon_dx = 89

        self.selected_3 = False
        self.selected_2 = False
        self.selected = False

        self.level_text_x = 405
        self.level_text_y = 430

        self.banner = pygame.image.load('assets/images/menus/banner.png').convert_alpha()
        self.next_text_transparency = 255
        self.next_text_transparency_bool = False

        self.bg = pygame.image.load('assets/images/menus/bg5.png').convert_alpha()

        self.level_que = []
        self.title = self.title_font.render('LEVEL SELECT', True, (255, 255, 255))
        self.random_text = self.title_font.render('?', True, (255, 255, 255))
        self.next_scene_text = self.large_font.render('READY', True, (255, 255, 255))
        self.button_text = self.button_font.render('P1 PRESS RED TO PLAY', True, (255, 255, 255))

        self.level_select_1 = pygame.image.load("assets/images/menus/level_select_1.png").convert_alpha()
        self.level_select_2 = pygame.image.load("assets/images/menus/level_select_2.png").convert_alpha()

        self.level_select_scalar = .4
        self.icon_select_scalar = .35
        self.level1_icon = pygame.image.load("assets/images/menus/lvl_1_icon.png").convert_alpha()
        self.level2_icon = pygame.image.load("assets/images/menus/lvl_2_icon.png").convert_alpha()
        self.level3_icon = pygame.image.load("assets/images/menus/lvl_3_icon.png").convert_alpha()
        self.level4_icon = pygame.image.load("assets/images/menus/lvl_4_icon.png").convert_alpha()
        self.level5_icon = pygame.image.load("assets/images/menus/lvl_5_icon.png").convert_alpha()
        self.level6_icon = pygame.image.load("assets/images/menus/lvl_6_icon.png").convert_alpha()
        self.level7_icon = pygame.image.load("assets/images/menus/lvl_7_icon.png").convert_alpha()
        self.level8_icon = pygame.image.load("assets/images/menus/lvl_8_icon.png").convert_alpha()
        self.level9_icon = pygame.image.load("assets/images/menus/lvl_9_icon.png").convert_alpha()
        self.level10_icon = pygame.image.load("assets/images/menus/lvl_10_icon.png").convert_alpha()
        self.level11_icon = pygame.image.load("assets/images/menus/lvl_11_icon.png").convert_alpha()
        self.level12_icon = pygame.image.load("assets/images/menus/lvl_12_icon.png").convert_alpha()
        self.level13_icon = pygame.image.load("assets/images/menus/lvl_13_icon.png").convert_alpha()
        self.random_level = pygame.Surface((1024*self.level_select_scalar, 494*self.level_select_scalar))
        self.random_level.fill((179, 179, 178))
        self.random_level_text = self.random_level_font.render('?', True, (255, 255, 255))
        self.level_select_icon = pygame.image.load("assets/images/menus/level_select_icon.png").convert_alpha()

        #for big snapshot
        self.level1_icon = pygame.transform.scale_by(self.level1_icon, self.level_select_scalar)
        self.level2_icon = pygame.transform.scale_by(self.level2_icon, self.level_select_scalar)
        self.level3_icon = pygame.transform.scale_by(self.level3_icon, self.level_select_scalar)
        self.level4_icon = pygame.transform.scale_by(self.level4_icon, self.level_select_scalar)
        self.level5_icon = pygame.transform.scale_by(self.level5_icon, self.level_select_scalar)
        self.level6_icon = pygame.transform.scale_by(self.level6_icon, self.level_select_scalar)
        self.level7_icon = pygame.transform.scale_by(self.level7_icon, self.level_select_scalar)
        self.level8_icon = pygame.transform.scale_by(self.level8_icon, self.level_select_scalar)
        self.level9_icon = pygame.transform.scale_by(self.level9_icon, self.level_select_scalar)
        self.level10_icon = pygame.transform.scale_by(self.level10_icon, self.level_select_scalar)
        self.level11_icon = pygame.transform.scale_by(self.level11_icon, self.level_select_scalar)
        self.level12_icon = pygame.transform.scale_by(self.level12_icon, self.level_select_scalar)
        self.level13_icon = pygame.transform.scale_by(self.level13_icon, self.level_select_scalar*.5)
        self.level1_text = self.small_font.render('LEVEL 1', True, (255, 255, 255))
        self.level2_text = self.small_font.render('LEVEL 2', True, (255, 255, 255))
        self.level3_text = self.small_font.render('LEVEL 3', True, (255, 255, 255))
        self.level4_text = self.small_font.render('LEVEL 4', True, (255, 255, 255))
        self.level5_text = self.small_font.render('LEVEL 5', True, (255, 255, 255))
        self.level6_text = self.small_font.render('LEVEL 6', True, (255, 255, 255))
        self.level7_text = self.small_font.render('LEVEL 7', True, (255, 255, 255))
        self.level8_text = self.small_font.render('LEVEL 8', True, (255, 255, 255))
        self.level9_text = self.small_font.render('LEVEL 9', True, (255, 255, 255))
        self.level10_text = self.small_font.render('LEVEL 10', True, (255, 255, 255))
        self.level11_text = self.small_font.render('LEVEL 11', True, (255, 255, 255))
        self.level12_text = self.small_font.render('LEVEL 12', True, (255, 255, 255))
        self.level13_text = self.small_font.render('LEVEL 13', True, (255, 255, 255))
        self.random_big_text = self.small_font.render('RANDOM', True, (255, 255, 255))

        #for icon selector
        self.level1_icon_small = pygame.transform.scale_by(self.level1_icon, self.icon_select_scalar)
        self.level2_icon_small = pygame.transform.scale_by(self.level2_icon, self.icon_select_scalar)
        self.level3_icon_small = pygame.transform.scale_by(self.level3_icon, self.icon_select_scalar)
        self.level4_icon_small = pygame.transform.scale_by(self.level4_icon, self.icon_select_scalar)
        self.level5_icon_small = pygame.transform.scale_by(self.level5_icon, self.icon_select_scalar)
        self.level6_icon_small = pygame.transform.scale_by(self.level6_icon, self.icon_select_scalar)
        self.level7_icon_small = pygame.transform.scale_by(self.level7_icon, self.icon_select_scalar)
        self.level8_icon_small = pygame.transform.scale_by(self.level8_icon, self.icon_select_scalar)
        self.level9_icon_small = pygame.transform.scale_by(self.level9_icon, self.icon_select_scalar)
        self.level10_icon_small = pygame.transform.scale_by(self.level10_icon, self.icon_select_scalar)
        self.level11_icon_small = pygame.transform.scale_by(self.level11_icon, self.icon_select_scalar)
        self.level12_icon_small = pygame.transform.scale_by(self.level12_icon, self.icon_select_scalar)
        self.level13_icon_small = pygame.transform.scale_by(self.level13_icon, self.icon_select_scalar)
        self.random_level_small = pygame.Surface((288, 148))
        self.random_level_small = pygame.transform.scale_by(self.random_level_small, .49)
        self.random_level_small.fill((179, 179, 178))
        self.random_level_small_text = self.random_level_small_font.render('?', True, (255, 255, 255))

        self.transparent_selector = pygame.Surface((144, 71), pygame.SRCALPHA)
        self.transparent_selector.fill((0,0,0, 100))
        self.new_icon = self.transparent_selector
        self.level_index = 0
        



    def display_scene(self, icon_index):
        self.screen.blit(self.bg, (0,0))
        self.screen.blit(self.title, (320, 25))
        self.screen.blit(self.level_select_1, (200, 150))
        self.screen.blit(self.level_select_2, (200, 500))
        self.screen.blit(self.random_text, (765, 505))

        if icon_index == 0:
            self.screen.blit(self.level1_icon, (315, 225))
            self.screen.blit(self.level1_text, (self.level_text_x, self.level_text_y))
            self.screen.blit(self.level1_icon_small, (self.top_icon_x+3, 140))
            self.screen.blit(self.level_select_icon, (self.top_icon_x,137))
        if icon_index == 1:
            self.screen.blit(self.level2_icon, (315, 225))
            self.screen.blit(self.level2_text, (self.level_text_x, self.level_text_y))
            self.screen.blit(self.level2_icon_small, (self.top_icon_x+3+self.icon_dx, 140))
            self.screen.blit(self.level_select_icon, (self.top_icon_x+self.icon_dx,137))
        if icon_index == 2:
            self.screen.blit(self.level3_icon, (315, 225))
            self.screen.blit(self.level3_text, (self.level_text_x, self.level_text_y))
            self.screen.blit(self.level3_icon_small, (self.top_icon_x+3+(2*self.icon_dx), 140))
            self.screen.blit(self.level_select_icon, (self.top_icon_x+(2*self.icon_dx),137))
        if icon_index == 3:
            self.screen.blit(self.level4_icon, (315, 225))
            self.screen.blit(self.level4_text, (self.level_text_x, self.level_text_y))
            self.screen.blit(self.level4_icon_small, (self.top_icon_x+3+(3*self.icon_dx), 140))
            self.screen.blit(self.level_select_icon, (self.top_icon_x+(3*self.icon_dx),137))
        if icon_index == 4:
            self.screen.blit(self.level5_icon, (315, 225))
            self.screen.blit(self.level5_text, (self.level_text_x, self.level_text_y))
            self.screen.blit(self.level5_icon_small, (self.top_icon_x+3+(4*self.icon_dx), 140))
            self.screen.blit(self.level_select_icon, (self.top_icon_x+(4*self.icon_dx),137))
        if icon_index == 5:
            self.screen.blit(self.level6_icon, (315, 225))
            self.screen.blit(self.level6_text, (self.level_text_x, self.level_text_y))
            self.screen.blit(self.level6_icon_small, (self.top_icon_x+3+(5*self.icon_dx), 140))
            self.screen.blit(self.level_select_icon, (self.top_icon_x+(5*self.icon_dx),137))
        if icon_index == 6:
            self.screen.blit(self.level7_icon, (315, 225))
            self.screen.blit(self.level7_text, (self.level_text_x, self.level_text_y))
            self.screen.blit(self.level7_icon_small, (self.top_icon_x+3+(6*self.icon_dx), 140))
            self.screen.blit(self.level_select_icon, (self.top_icon_x+(6*self.icon_dx),137))
        if icon_index == 7:
            self.screen.blit(self.level8_icon, (315, 225))
            self.screen.blit(self.level8_text, (self.level_text_x, self.level_text_y))
            self.screen.blit(self.level8_icon_small, (self.bottom_icon_x+3, 493))
            self.screen.blit(self.level_select_icon, (self.bottom_icon_x,490))
        if icon_index == 8:
            self.screen.blit(self.level9_icon, (315, 225))
            self.screen.blit(self.level9_text, (self.level_text_x, self.level_text_y))
            self.screen.blit(self.level9_icon_small, (self.bottom_icon_x+3+(self.icon_dx), 493))
            self.screen.blit(self.level_select_icon, (self.bottom_icon_x+(self.icon_dx),490))
        if icon_index == 9:
            self.screen.blit(self.level10_icon, (315, 225))
            self.screen.blit(self.level10_text, (self.level_text_x-17, self.level_text_y))
            self.screen.blit(self.level10_icon_small, (self.bottom_icon_x+3+(2*self.icon_dx), 493))
            self.screen.blit(self.level_select_icon, (self.bottom_icon_x+(2*self.icon_dx),490))
        if icon_index == 10:
            self.screen.blit(self.level11_icon, (315, 225))
            self.screen.blit(self.level11_text, (self.level_text_x-17, self.level_text_y))
            self.screen.blit(self.level1_icon_small, (self.bottom_icon_x+3+(3*self.icon_dx), 493))
            self.screen.blit(self.level_select_icon, (self.bottom_icon_x+(3*self.icon_dx),490))
        if icon_index == 11:
            self.screen.blit(self.level12_icon, (315, 225))
            self.screen.blit(self.level12_text, (self.level_text_x-17, self.level_text_y))
            self.screen.blit(self.level12_icon_small, (self.bottom_icon_x+3+(4*self.icon_dx), 493))
            self.screen.blit(self.level_select_icon, (self.bottom_icon_x+(4*self.icon_dx),490))
        if icon_index == 12:
            self.screen.blit(self.level13_icon, (315, 225))
            self.screen.blit(self.level13_text, (self.level_text_x-17, self.level_text_y))
            self.screen.blit(self.level13_icon_small, (self.bottom_icon_x+3+(5*self.icon_dx), 493))
            self.screen.blit(self.level_select_icon, (self.bottom_icon_x+(5*self.icon_dx),490))
        if icon_index == 13:
            self.screen.blit(self.random_level, (315, 225))
            self.screen.blit(self.random_big_text, (self.level_text_x, self.level_text_y))
            self.screen.blit(self.random_level_text, (460, 250))
            self.screen.blit(self.random_level_small, (self.bottom_icon_x+3+(6*self.icon_dx),493))
            self.screen.blit(self.random_level_small_text, (self.bottom_icon_x+50+(6*self.icon_dx), 495))
            self.screen.blit(self.level_select_icon, (self.bottom_icon_x+(6*self.icon_dx),490))
        


    def run_level_select(self, icon_index, lvl_selected):

        #add to each if statement to have level selected
        if lvl_selected == True:
            if icon_index == 0:
                self.screen.blit(self.transparent_selector, (self.top_icon_x+3, 140))
            if icon_index == 1:
                self.screen.blit(self.transparent_selector, (self.top_icon_x+3+self.icon_dx, 140))
            if icon_index == 2:
                self.screen.blit(self.transparent_selector, (self.top_icon_x+3+(2*self.icon_dx), 140))
            if icon_index == 3:
                self.screen.blit(self.transparent_selector, (self.top_icon_x+3+(3*self.icon_dx), 140))
            if icon_index == 4:
                self.screen.blit(self.transparent_selector, (self.top_icon_x+3+(4*self.icon_dx), 140))
            if icon_index == 5:
                self.screen.blit(self.transparent_selector, (self.top_icon_x+3+(5*self.icon_dx), 140))
            if icon_index == 6:
                self.screen.blit(self.transparent_selector, (self.top_icon_x+3+(6*self.icon_dx), 140))
            if icon_index == 7:
                self.screen.blit(self.transparent_selector, (self.bottom_icon_x+3, 493))
            if icon_index == 8:
                self.screen.blit(self.transparent_selector, (self.bottom_icon_x+3+(self.icon_dx), 493))
            if icon_index == 9:
                self.screen.blit(self.transparent_selector, (self.bottom_icon_x+3+(2*self.icon_dx), 493))
            if icon_index == 10:
                self.screen.blit(self.transparent_selector, (self.bottom_icon_x+3+(3*self.icon_dx), 493))
            if icon_index == 11:
                self.screen.blit(self.transparent_selector, (self.bottom_icon_x+3+(4*self.icon_dx), 493))
            if icon_index == 12:
                self.screen.blit(self.transparent_selector, (self.bottom_icon_x+3+(5*self.icon_dx), 493))
            if icon_index == 13:
                self.screen.blit(self.transparent_selector, (self.bottom_icon_x+3+(6*self.icon_dx), 493))

            self.screen.blit(self.banner, (0, 200))
            self.screen.blit(self.next_scene_text, (360, 220))
            self.screen.blit(self.button_text, (375, 305))
            if self.next_text_transparency_bool == False:
                self.next_text_transparency -= 8
            if self.next_text_transparency <= 0:
                self.next_text_transparency_bool = True
            if self.next_text_transparency_bool == True:
                self.next_text_transparency += 8
            if self.next_text_transparency >= 255:
                self.next_text_transparency_bool = False
            self.next_scene_text.set_alpha(self.next_text_transparency)
            self.button_text.set_alpha(self.next_text_transparency)
            self.level_index = icon_index



    def run_level_select_1(self, icon_index):
        
        #add to each if statement to have level selected
        if self.selected_2 == True:
            self.level_que.append(icon_index)
        if self.selected_3 == True:
            self.level_que.append(icon_index)
        if self.selected == True:
            self.level_que.append(icon_index)
            self.screen.blit(self.banner, (0, 200))
            self.screen.blit(self.next_scene_text, (360, 220))
            self.screen.blit(self.button_text, (375, 305))
            if self.next_text_transparency_bool == False:
                self.next_text_transparency -= 4
            if self.next_text_transparency <= 0:
                self.next_text_transparency_bool = True
            if self.next_text_transparency_bool == True:
                self.next_text_transparency += 4
            if self.next_text_transparency >= 255:
                self.next_text_transparency_bool = False
            self.next_scene_text.set_alpha(self.next_text_transparency)
            self.button_text.set_alpha(self.next_text_transparency)
            self.screen.blit(self.transparent_selector, (self.top_icon_x+3, 140))




class scene_gameplay_1:

    def __init__(self, screen):

        #normal init
        self.screen = screen
        self.game_ui = game_ui.gameplay_ui(self.screen, p1_name="", p2_name="", p1_tank_index=0, p2_tank_index=0)
        self.game_ui.gameplay_1_active = False
        self.p1 = players.player(self.screen, 0)
        self.p2 = players.player(self.screen, 1)
        self.p2.x = 150
        self.p2.y = 200
        self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
        self.p2.rot = 180
        self.tank_scale = .65
        self.spawn_loc = True
        self.p1.wins = 0
        self.p2.wins = 0
        self.current_winner = "none"

    def load_scene(self, level_index, p1_tank_index, p2_tank_index):
        #get file paths and convert to tiled object
        self.map1_tmx_data = pytmx.load_pygame("assets/levels/map1.tmx")
        self.map2_tmx_data = pytmx.load_pygame("assets/levels/map2.tmx")
        self.map3_tmx_data = pytmx.load_pygame("assets/levels/map3.tmx")
        self.map4_tmx_data = pytmx.load_pygame("assets/levels/map4.tmx")
        self.map5_tmx_data = pytmx.load_pygame("assets/levels/map5.tmx")
        self.map6_tmx_data = pytmx.load_pygame("assets/levels/map6.tmx")
        self.map7_tmx_data = pytmx.load_pygame("assets/levels/map7.tmx")
        self.map8_tmx_data = pytmx.load_pygame("assets/levels/map8.tmx")
        self.map9_tmx_data = pytmx.load_pygame("assets/levels/map9.tmx")
        self.map10_tmx_data = pytmx.load_pygame("assets/levels/map10.tmx")
        self.map11_tmx_data = pytmx.load_pygame("assets/levels/map11.tmx")
        self.map12_tmx_data = pytmx.load_pygame("assets/levels/map12.tmx")
        self.map13_tmx_data = pytmx.load_pygame("assets/levels/map13.tmx")

        self.title_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 100)
        self.small_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 25)

        #init level objects
        import maps
        self.level1 = maps.map(self.screen, self.map1_tmx_data)
        self.level2 = maps.map(self.screen, self.map2_tmx_data) 
        self.level3 = maps.map(self.screen, self.map3_tmx_data)
        self.level4 = maps.map(self.screen, self.map4_tmx_data)
        self.level5 = maps.map(self.screen, self.map5_tmx_data)
        self.level6 = maps.map(self.screen, self.map6_tmx_data)
        self.level7 = maps.map(self.screen, self.map7_tmx_data)
        self.level8 = maps.map(self.screen, self.map8_tmx_data)
        self.level9 = maps.map(self.screen, self.map9_tmx_data)
        self.level10 = maps.map(self.screen, self.map10_tmx_data)
        self.level11 = maps.map(self.screen, self.map11_tmx_data)
        self.level12 = maps.map(self.screen, self.map12_tmx_data)
        self.level13 = maps.map(self.screen, self.map13_tmx_data)




        #init players
 

        self.both_tanks_alive = True

        self.level_que = []
        self.round = 0
        self.p1_score = 0
        self.p2_score = 0

        if self.both_tanks_alive == False: #init players for next round
            self.p1 = players.player(self.screen, 0)
            self.p2 = players.player(self.screen, 1)
            self.p2.x = 150
            self.p2.y = 150
            self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            self.p2.rot = 180
            self.tank_scale = .65
            self.both_tanks_alive = True

        self.level_index = level_index
        
        
        self.game_ui.p1_tank_index = p1_tank_index
        self.game_ui.p2_tank_index = p2_tank_index

        self.game_over_text = self.title_font.render("GAME OVER", True, "red")
        self.button_text = self.small_font.render("PRESS ANY BUTTON", True, "red")

            #add player tank index to player objects
        if p1_tank_index == 0:
            self.game_ui.p1_name = "G.I. JOHN"
            self.p1.top_tank_image = pygame.image.load("assets/images/game/sprites/green_tank_top.png").convert_alpha()
            self.p1.base_tank_image = pygame.image.load("assets/images/game/sprites/green_tank_bottom.png").convert_alpha()
            self.p1.base_tank_image = pygame.transform.scale_by(self.p1.base_tank_image, self.tank_scale)
            self.p1.top_tank_image = pygame.transform.scale_by(self.p1.top_tank_image, self.tank_scale)
            self.p1.top_tank_image_copy = self.p1.top_tank_image
            self.p1.base_tank_image_copy = self.p1.base_tank_image
            self.p1.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p1.pos)
            self.p1.hit_box_rect_copy = self.p1.hit_box_rect

        elif p1_tank_index == 1:
            self.game_ui.p1_name = "COLD CUT"
            self.p1.top_tank_image = pygame.image.load("assets/images/game/sprites/blue_tank_top.png").convert_alpha()
            self.p1.base_tank_image = pygame.image.load("assets/images/game/sprites/blue_tank_bottom.png").convert_alpha()
            self.p1.base_tank_image = pygame.transform.scale_by(self.p1.base_tank_image, self.tank_scale)
            self.p1.top_tank_image = pygame.transform.scale_by(self.p1.top_tank_image, self.tank_scale)
            self.p1.top_tank_image_copy = self.p1.top_tank_image
            self.p1.base_tank_image_copy = self.p1.base_tank_image
            self.p1.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p1.pos)
            self.p1.hit_box_rect_copy = self.p1.hit_box_rect

        elif p1_tank_index == 2:
            self.game_ui.p1_name = "SHREDDER"
            self.p1.top_tank_image = pygame.image.load("assets/images/game/sprites/red_tank_top.png").convert_alpha()
            self.p1.base_tank_image = pygame.image.load("assets/images/game/sprites/red_tank_bottom.png").convert_alpha()
            self.p1.base_tank_image = pygame.transform.scale_by(self.p1.base_tank_image, self.tank_scale)
            self.p1.top_tank_image = pygame.transform.scale_by(self.p1.top_tank_image, self.tank_scale)
            self.p1.top_tank_image_copy = self.p1.top_tank_image
            self.p1.base_tank_image_copy = self.p1.base_tank_image
            self.p1.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p1.pos)
            self.p1.hit_box_rect_copy = self.p1.hit_box_rect

        elif p1_tank_index == 3:
            self.game_ui.p1_name = "MI-MI"
            self.p1.top_tank_image = pygame.image.load("assets/images/game/sprites/gray_tank_top.png").convert_alpha()
            self.p1.base_tank_image = pygame.image.load("assets/images/game/sprites/gray_tank_bottom.png").convert_alpha()
            self.p1.base_tank_image = pygame.transform.scale_by(self.p1.base_tank_image, self.tank_scale)
            self.p1.top_tank_image = pygame.transform.scale_by(self.p1.top_tank_image, self.tank_scale)
            self.p1.top_tank_image_copy = self.p1.top_tank_image
            self.p1.base_tank_image_copy = self.p1.base_tank_image
            self.p1.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p1.pos)
            self.p1.hit_box_rect_copy = self.p1.hit_box_rect
            

        if p2_tank_index == 0:
            self.game_ui.p2_name = "G.I. JOHN"
            self.p2.top_tank_image = pygame.image.load("assets/images/game/sprites/green_tank_top.png").convert_alpha()
            self.p2.base_tank_image = pygame.image.load("assets/images/game/sprites/green_tank_bottom.png").convert_alpha()
            self.p2.base_tank_image = pygame.transform.scale_by(self.p2.base_tank_image, self.tank_scale)
            self.p2.top_tank_image = pygame.transform.scale_by(self.p2.top_tank_image, self.tank_scale)
            self.p2.top_tank_image_copy = self.p2.top_tank_image
            self.p2.base_tank_image_copy = self.p2.base_tank_image
            self.p2.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p2.pos)
            self.p2.hit_box_rect_copy = self.p2.hit_box_rect
            
        elif p2_tank_index == 1:
            self.game_ui.p2_name = "COLD CUT"
            self.p2.top_tank_image = pygame.image.load("assets/images/game/sprites/blue_tank_top.png").convert_alpha()
            self.p2.base_tank_image = pygame.image.load("assets/images/game/sprites/blue_tank_bottom.png").convert_alpha()
            self.p2.base_tank_image = pygame.transform.scale_by(self.p2.base_tank_image, self.tank_scale)
            self.p2.top_tank_image = pygame.transform.scale_by(self.p2.top_tank_image, self.tank_scale)
            self.p2.top_tank_image_copy = self.p2.top_tank_image
            self.p2.base_tank_image_copy = self.p2.base_tank_image
            self.p2.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p2.pos)
            self.p2.hit_box_rect_copy = self.p2.hit_box_rect
            
        elif p2_tank_index == 2:
            self.game_ui.p2_name = "SHREDDER"
            self.p2.top_tank_image = pygame.image.load("assets/images/game/sprites/red_tank_top.png").convert_alpha()
            self.p2.base_tank_image = pygame.image.load("assets/images/game/sprites/red_tank_bottom.png").convert_alpha()
            self.p2.base_tank_image = pygame.transform.scale_by(self.p2.base_tank_image, self.tank_scale)
            self.p2.top_tank_image = pygame.transform.scale_by(self.p2.top_tank_image, self.tank_scale)
            self.p2.top_tank_image_copy = self.p2.top_tank_image
            self.p2.base_tank_image_copy = self.p2.base_tank_image
            self.p2.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p2.pos)
            self.p2.hit_box_rect_copy = self.p2.hit_box_rect
            
        elif p2_tank_index == 3:
            self.game_ui.p2_name = "MI-MI"
            self.p2.x = 100
            self.p2.y = 100
            self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            self.p2.rot = 100
            self.p2.top_tank_image = pygame.image.load("assets/images/game/sprites/gray_tank_top.png").convert_alpha()
            self.p2.base_tank_image = pygame.image.load("assets/images/game/sprites/gray_tank_bottom.png").convert_alpha()
            self.p2.base_tank_image = pygame.transform.scale_by(self.p2.base_tank_image, self.tank_scale)
            self.p2.top_tank_image = pygame.transform.scale_by(self.p2.top_tank_image, self.tank_scale)
            self.p2.top_tank_image_copy = self.p2.top_tank_image
            self.p2.base_tank_image_copy = self.p2.base_tank_image
            self.p2.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p2.pos)
            self.p2.hit_box_rect_copy = self.p2.hit_box_rect
            
        self.level1.get_collision_rects()
        self.level2.get_collision_rects()
        self.level3.get_collision_rects()
        self.level4.get_collision_rects()
        self.level5.get_collision_rects()
        self.level6.get_collision_rects()
        self.level7.get_collision_rects()
        self.level8.get_collision_rects()
        self.level9.get_collision_rects()
        self.level10.get_collision_rects()
        self.level11.get_collision_rects()
        self.level12.get_collision_rects()
        self.level13.get_collision_rects()


        if self.spawn_loc:
            #print("tank index reset running")
            self.spawn_loc = False
            if self.level_index == 0:
                self.p1.x = 90
                self.p1.y = 150
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 425
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 1:
                self.p1.x = 90
                self.p1.y = 425
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 150
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 2:
                self.p1.x = 90
                self.p1.y = 150
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 425
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 3:
                self.p1.x = 90
                self.p1.y = 150
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 425
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 4:
                self.p1.x = 90
                self.p1.y = 150
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 425
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 5:
                self.p1.x = 90
                self.p1.y = 290
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 295
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 6:
                self.p1.x = 90
                self.p1.y = 290
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 295
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 7:
                self.p1.x = 90
                self.p1.y = 150
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 425
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 8:
                self.p1.x = 90
                self.p1.y = 425
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 150
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 9:
                self.p1.x = 90
                self.p1.y = 290
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 295
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 10:
                self.p1.x = 90
                self.p1.y = 290
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 295
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 11:
                self.p1.x = 90
                self.p1.y = 290
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 295
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 12:
                self.p1.x = 90
                self.p1.y = 425
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 150
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)

        self.bg_mud = pygame.image.load("assets/images/game/background/bg.png").convert_alpha()
        self.trumpet_w = pygame.mixer.Sound("assets/sound/sound_effects/game/trumpet_win.mp3")
        self.trumpet_s = pygame.mixer.Sound("assets/sound/sound_effects/game/trumpet_s.mp3")
        self.explosion_2 = pygame.mixer.Sound("assets/sound/sound_effects/game/explosion-sound-effect-1-free-on-gamesfxpackscom-241821.mp3")


        try:
            if self.level_que is not []:
                level_index = self.level_que[self.round]
        except:
            pass
        if level_index == 0:
            self.collision_rects = self.level1.collision_rects
            self.wall2_rects = self.level1.wall2_rects
        elif level_index == 1:
            self.collision_rects = self.level2.collision_rects
            self.wall2_rects = self.level2.wall2_rects
        elif level_index == 2:
            self.collision_rects = self.level3.collision_rects
            self.wall2_rects = self.level3.wall2_rects
            #print("rects c and w: ", self.collision_rects, self.wall2_rects)
        elif level_index == 3:
            self.collision_rects = self.level4.collision_rects
            self.wall2_rects = self.level4.wall2_rects
        elif level_index == 4:
            self.collision_rects = self.level5.collision_rects
            self.wall2_rects = self.level5.wall2_rects
            self.wall2_rects = self.level5.wall2_rects
        elif level_index == 5:
            self.collision_rects = self.level6.collision_rects
            self.wall2_rects = self.level6.wall2_rects
        elif level_index == 6:
            self.collision_rects = self.level7.collision_rects
            self.wall2_rects = self.level7.wall2_rects
        elif level_index == 7:
            self.collision_rects = self.level8.collision_rects
            self.wall2_rects = self.level8.wall2_rects
        elif level_index == 8:
            self.collision_rects = self.level9.collision_rects
            self.wall2_rects = self.level9.wall2_rects
        elif level_index == 9:
            self.collision_rects = self.level10.collision_rects
            self.wall2_rects = self.level10.wall2_rects
        elif level_index == 10:
            self.collision_rects = self.level11.collision_rects
            self.wall2_rects = self.level11.wall2_rects
        elif level_index == 11:
            self.collision_rects = self.level12.collision_rects
            self.wall2_rects = self.level12.wall2_rects
        elif level_index == 12:
            self.collision_rects = self.level13.collision_rects
            self.wall2_rects = self.level13.wall2_rectslevel13.collision_rects
            #maybe update display recs by calling load scene in level select rather than loading every frame
        self.level_index = level_index

        #load ui
        self.game_ui.load_game_1_ui(self.p1_score, self.p2_score)
        self.round_1_over = False
        self.round_2_over = False
        self.round_3_over = False


    def display_scene(self):
        self.screen.blit(self.bg_mud, (0,0))


        match self.level_index:
            case 0:
                self.level1.render_map()
            case 1:
                self.level2.render_map()
            case 2:
                self.level3.render_map()
            case 3:
                self.level4.render_map()
            case 4:
                self.level5.render_map()
            case 5:
                self.level6.render_map()
            case 6:
                self.level7.render_map()
            case 7:
                self.level8.render_map()
            case 8:
                self.level9.render_map()
            case 9:
                self.level10.render_map()
            case 10:
                self.level11.render_map()
            case 11:
                self.level12.render_map()
            case 12:
                self.level13.render_map()
        #ui 
        self.game_ui.render_ui()

    def run_gameplay_1(self, pot1, pot2, rb1, rb2, wb1, wb2):

        if self.p1 != None and self.p2 != None:
            self.p1.enemy_tank_rect = self.p2.hit_box_rect
            self.p1.update(self.collision_rects, self.both_tanks_alive, self.wall2_rects, pot1, rb1, wb1)
            self.p2.enemy_tank_rect = self.p1.hit_box_rect
            self.p2.update(self.collision_rects, self.both_tanks_alive, self.wall2_rects, pot2, rb2, wb2)
            for missile in self.p1.missile_list:
                if missile.collided_with_enemy:
                    self.explosion_2.play()
                    self.p2 = None
                    self.both_tanks_alive = False
                    self.p1.missile_list.clear()
                    self.current_winner = "p1"
                    self.p1_score += 1
                    self.trumpet_w.play()
                    break
                if missile.collided_with_self:
                    self.explosion_2.play()
                    self.p1 = None
                    self.both_tanks_alive = False
                    self.current_winner = "p2"
                    self.p2_score += 1
                    self.trumpet_s.play()
                    break
            if self.both_tanks_alive:
                for missile in self.p2.missile_list:
                    if missile.collided_with_enemy:
                        self.explosion_2.play()
                        self.p1 = None
                        self.both_tanks_alive = False
                        self.p2.missile_list.clear()
                        self.current_winner = "p2"
                        self.p2_score += 1
                        self.trumpet_w.play()
                        #print("p2 missile hit p1")
                    if missile.collided_with_self:
                        self.explosion_2.play()
                        self.p2 = None
                        self.both_tanks_alive = False
                        self.current_winner = "p1"
                        self.p1_score += 1
                        #print("p2 missile hit self")
                        self.trumpet_s.play()
        else:
            if self.p1 != None:
                self.p1.update(self.collision_rects, self.both_tanks_alive, self.wall2_rects, pot1, rb1, wb1)
            if self.p2 != None:
                self.p2.update(self.collision_rects, self.both_tanks_alive, self.wall2_rects, pot2, rb2, wb2)

            if self.p1 == None or self.p2 == None:
                if self.round < len(self.level_que) or self.p1_score < 2 or self.p2_score < 2:
                    if self.round_1_over == False:
                        self.game_over_text = self.title_font.render(f"{self.current_winner} Wins round 1!", True, "red")
                        self.screen.blit(self.game_over_text, (200, 250))
                        self.screen.blit(self.button_text, (350, 400))
                        self.round = 1
                        self.level_index = self.level_que[self.round]
                        self.round_1_over = True

                    elif self.round_2_over == False:
                        self.game_over_text = self.title_font.render(f"{self.current_winner} Wins round 1!", True, "red")
                        self.screen.blit(self.game_over_text, (200, 250))
                        self.screen.blit(self.button_text, (350, 400))
                        self.round = 2
                        self.level_index = self.level_que[self.round]
                        self.round_2_over = True


                else:
                    if self.p1_score >= 2:
                        self.current_winner = "p1"
                    if self.p2_score >= 2:
                        self.current_winner = "p2"
                    self.self.game_over_text = self.title_font.render(f"{self.current_winner} Wins! Game over", True, "red")
                    self.screen.blit(self.game_over_text, (200, 250))
                    self.screen.blit(self.button_text, (350, 400))
                    self.round_3_over = True

            #add get ready for next level stuff here
            #etc...


class scene_gameplay_2:

    def __init__(self, screen):
        #get file paths and convert to tiled object


        #import because pytmx sucks

        
        #normal init
        self.screen = screen



        self.game_ui = game_ui.gameplay_ui(self.screen, p1_name="", p2_name="", p1_tank_index=0, p2_tank_index=0)
        self.game_ui.gameplay_1_active = False

        #init players
        self.p1 = players.player(self.screen, 0)
        self.p2 = players.player(self.screen, 1)
        self.p2.x = 150
        self.p2.y = 200
        self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
        self.p2.rot = 180
        self.tank_scale = .65
        self.spawn_loc = True

        self.both_tanks_alive = True
        self.current_winner = "none"

    def load_scene(self, level_index, p1_tank_index, p2_tank_index):
        import maps
        self.map1_tmx_data = pytmx.load_pygame("assets/levels/map1.tmx")
        self.map2_tmx_data = pytmx.load_pygame("assets/levels/map2.tmx")
        self.map3_tmx_data = pytmx.load_pygame("assets/levels/map3.tmx")
        self.map4_tmx_data = pytmx.load_pygame("assets/levels/map4.tmx")
        self.map5_tmx_data = pytmx.load_pygame("assets/levels/map5.tmx")
        self.map6_tmx_data = pytmx.load_pygame("assets/levels/map6.tmx")
        self.map7_tmx_data = pytmx.load_pygame("assets/levels/map7.tmx")
        self.map8_tmx_data = pytmx.load_pygame("assets/levels/map8.tmx")
        self.map9_tmx_data = pytmx.load_pygame("assets/levels/map9.tmx")
        self.map10_tmx_data = pytmx.load_pygame("assets/levels/map10.tmx")
        self.map11_tmx_data = pytmx.load_pygame("assets/levels/map11.tmx")
        self.map12_tmx_data = pytmx.load_pygame("assets/levels/map12.tmx")
        self.map13_tmx_data = pytmx.load_pygame("assets/levels/map13.tmx")
        self.title_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 100)
        self.small_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 25)

        #init level objects
        self.level1 = maps.map(self.screen, self.map1_tmx_data)
        self.level2 = maps.map(self.screen, self.map2_tmx_data) 
        self.level3 = maps.map(self.screen, self.map3_tmx_data)
        self.level4 = maps.map(self.screen, self.map4_tmx_data)
        self.level5 = maps.map(self.screen, self.map5_tmx_data)
        self.level6 = maps.map(self.screen, self.map6_tmx_data)
        self.level7 = maps.map(self.screen, self.map7_tmx_data)
        self.level8 = maps.map(self.screen, self.map8_tmx_data)
        self.level9 = maps.map(self.screen, self.map9_tmx_data)
        self.level10 = maps.map(self.screen, self.map10_tmx_data)
        self.level11 = maps.map(self.screen, self.map11_tmx_data)
        self.level12 = maps.map(self.screen, self.map12_tmx_data)
        self.level13 = maps.map(self.screen, self.map13_tmx_data)

        if self.both_tanks_alive == False: #init players for next round
            self.p1 = players.player(self.screen, 0)
            self.p2 = players.player(self.screen, 1)
            self.p2.x = 150
            self.p2.y = 150
            self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            self.p2.rot = 180
            self.tank_scale = .65
            self.both_tanks_alive = True

        self.level_index = level_index
        
        
        self.game_ui.p1_tank_index = p1_tank_index
        self.game_ui.p2_tank_index = p2_tank_index

        self.game_over_text = self.title_font.render("GAME OVER", True, "red")
        self.button_text = self.small_font.render("PRESS ANY BUTTON", True, "white")

        self.next_text_transparency = 255
        self.next_text_transparency_bool = False

        self.banner = pygame.image.load('assets/images/menus/banner.png').convert_alpha()
        self.selected_rect = pygame.Surface((66, 66), pygame.SRCALPHA)
        self.selected_rect2 = pygame.Surface((66, 66), pygame.SRCALPHA)
        self.selected_rect.fill((0, 0, 0, 100))
        self.selected_rect2.fill((0, 0, 0, 100))

            #add player tank index to player objects
        if p1_tank_index == 0:
            self.game_ui.p1_name = "G.I. JOHN"
            self.p1.top_tank_image = pygame.image.load("assets/images/game/sprites/green_tank_top.png").convert_alpha()
            self.p1.base_tank_image = pygame.image.load("assets/images/game/sprites/green_tank_bottom.png").convert_alpha()
            self.p1.base_tank_image = pygame.transform.scale_by(self.p1.base_tank_image, self.tank_scale)
            self.p1.top_tank_image = pygame.transform.scale_by(self.p1.top_tank_image, self.tank_scale)
            self.p1.top_tank_image_copy = self.p1.top_tank_image
            self.p1.base_tank_image_copy = self.p1.base_tank_image
            self.p1.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p1.pos)
            self.p1.hit_box_rect_copy = self.p1.hit_box_rect

        elif p1_tank_index == 1:
            self.game_ui.p1_name = "COLD CUT"
            self.p1.top_tank_image = pygame.image.load("assets/images/game/sprites/blue_tank_top.png").convert_alpha()
            self.p1.base_tank_image = pygame.image.load("assets/images/game/sprites/blue_tank_bottom.png").convert_alpha()
            self.p1.base_tank_image = pygame.transform.scale_by(self.p1.base_tank_image, self.tank_scale)
            self.p1.top_tank_image = pygame.transform.scale_by(self.p1.top_tank_image, self.tank_scale)
            self.p1.top_tank_image_copy = self.p1.top_tank_image
            self.p1.base_tank_image_copy = self.p1.base_tank_image
            self.p1.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p1.pos)
            self.p1.hit_box_rect_copy = self.p1.hit_box_rect

        elif p1_tank_index == 2:
            self.game_ui.p1_name = "SHREDDER"
            self.p1.top_tank_image = pygame.image.load("assets/images/game/sprites/red_tank_top.png").convert_alpha()
            self.p1.base_tank_image = pygame.image.load("assets/images/game/sprites/red_tank_bottom.png").convert_alpha()
            self.p1.base_tank_image = pygame.transform.scale_by(self.p1.base_tank_image, self.tank_scale)
            self.p1.top_tank_image = pygame.transform.scale_by(self.p1.top_tank_image, self.tank_scale)
            self.p1.top_tank_image_copy = self.p1.top_tank_image
            self.p1.base_tank_image_copy = self.p1.base_tank_image
            self.p1.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p1.pos)
            self.p1.hit_box_rect_copy = self.p1.hit_box_rect

        elif p1_tank_index == 3:
            self.game_ui.p1_name = "MI-MI"
            self.p1.top_tank_image = pygame.image.load("assets/images/game/sprites/gray_tank_top.png").convert_alpha()
            self.p1.base_tank_image = pygame.image.load("assets/images/game/sprites/gray_tank_bottom.png").convert_alpha()
            self.p1.base_tank_image = pygame.transform.scale_by(self.p1.base_tank_image, self.tank_scale)
            self.p1.top_tank_image = pygame.transform.scale_by(self.p1.top_tank_image, self.tank_scale)
            self.p1.top_tank_image_copy = self.p1.top_tank_image
            self.p1.base_tank_image_copy = self.p1.base_tank_image
            self.p1.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p1.pos)
            self.p1.hit_box_rect_copy = self.p1.hit_box_rect
            

        if p2_tank_index == 0:
            self.game_ui.p2_name = "G.I. JOHN"
            self.p2.top_tank_image = pygame.image.load("assets/images/game/sprites/green_tank_top.png").convert_alpha()
            self.p2.base_tank_image = pygame.image.load("assets/images/game/sprites/green_tank_bottom.png").convert_alpha()
            self.p2.base_tank_image = pygame.transform.scale_by(self.p2.base_tank_image, self.tank_scale)
            self.p2.top_tank_image = pygame.transform.scale_by(self.p2.top_tank_image, self.tank_scale)
            self.p2.top_tank_image_copy = self.p2.top_tank_image
            self.p2.base_tank_image_copy = self.p2.base_tank_image
            self.p2.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p2.pos)
            self.p2.hit_box_rect_copy = self.p2.hit_box_rect
            
        elif p2_tank_index == 1:
            self.game_ui.p2_name = "COLD CUT"
            self.p2.top_tank_image = pygame.image.load("assets/images/game/sprites/blue_tank_top.png").convert_alpha()
            self.p2.base_tank_image = pygame.image.load("assets/images/game/sprites/blue_tank_bottom.png").convert_alpha()
            self.p2.base_tank_image = pygame.transform.scale_by(self.p2.base_tank_image, self.tank_scale)
            self.p2.top_tank_image = pygame.transform.scale_by(self.p2.top_tank_image, self.tank_scale)
            self.p2.top_tank_image_copy = self.p2.top_tank_image
            self.p2.base_tank_image_copy = self.p2.base_tank_image
            self.p2.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p2.pos)
            self.p2.hit_box_rect_copy = self.p2.hit_box_rect
            
        elif p2_tank_index == 2:
            self.game_ui.p2_name = "SHREDDER"
            self.p2.top_tank_image = pygame.image.load("assets/images/game/sprites/red_tank_top.png").convert_alpha()
            self.p2.base_tank_image = pygame.image.load("assets/images/game/sprites/red_tank_bottom.png").convert_alpha()
            self.p2.base_tank_image = pygame.transform.scale_by(self.p2.base_tank_image, self.tank_scale)
            self.p2.top_tank_image = pygame.transform.scale_by(self.p2.top_tank_image, self.tank_scale)
            self.p2.top_tank_image_copy = self.p2.top_tank_image
            self.p2.base_tank_image_copy = self.p2.base_tank_image
            self.p2.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p2.pos)
            self.p2.hit_box_rect_copy = self.p2.hit_box_rect
            
        elif p2_tank_index == 3:
            self.game_ui.p2_name = "MI-MI"
            self.p2.x = 100
            self.p2.y = 100
            self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            self.p2.rot = 100
            self.p2.top_tank_image = pygame.image.load("assets/images/game/sprites/gray_tank_top.png").convert_alpha()
            self.p2.base_tank_image = pygame.image.load("assets/images/game/sprites/gray_tank_bottom.png").convert_alpha()
            self.p2.base_tank_image = pygame.transform.scale_by(self.p2.base_tank_image, self.tank_scale)
            self.p2.top_tank_image = pygame.transform.scale_by(self.p2.top_tank_image, self.tank_scale)
            self.p2.top_tank_image_copy = self.p2.top_tank_image
            self.p2.base_tank_image_copy = self.p2.base_tank_image
            self.p2.hit_box_rect = self.p1.base_tank_image_copy.get_rect(center = self.p2.pos)
            self.p2.hit_box_rect_copy = self.p2.hit_box_rect
            
        self.level1.get_collision_rects()
        self.level2.get_collision_rects()
        self.level3.get_collision_rects()
        self.level4.get_collision_rects()
        self.level5.get_collision_rects()
        self.level6.get_collision_rects()
        self.level7.get_collision_rects()
        self.level8.get_collision_rects()
        self.level9.get_collision_rects()
        self.level10.get_collision_rects()
        self.level11.get_collision_rects()
        self.level12.get_collision_rects()
        self.level13.get_collision_rects()


        if self.spawn_loc:
            #print("tank index reset running")
            self.spawn_loc = False
            if self.level_index == 0:
                self.p1.x = 90
                self.p1.y = 150
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 425
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 1:
                self.p1.x = 90
                self.p1.y = 425
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 150
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 2:
                self.p1.x = 90
                self.p1.y = 150
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 425
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 3:
                self.p1.x = 90
                self.p1.y = 150
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 425
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 4:
                self.p1.x = 90
                self.p1.y = 150
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 425
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 5:
                self.p1.x = 90
                self.p1.y = 290
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 295
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 6:
                self.p1.x = 90
                self.p1.y = 290
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 295
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 7:
                self.p1.x = 90
                self.p1.y = 150
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 425
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 8:
                self.p1.x = 90
                self.p1.y = 425
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 150
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 9:
                self.p1.x = 90
                self.p1.y = 290
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 295
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 10:
                self.p1.x = 90
                self.p1.y = 290
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 295
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 11:
                self.p1.x = 90
                self.p1.y = 290
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 925
                self.p2.y = 295
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)
            if self.level_index == 12:
                self.p1.x = 90
                self.p1.y = 425
                self.p1.pos = pygame.math.Vector2(self.p1.x, self.p1.y)
                self.p2.x = 900
                self.p2.y = 150
                self.p2.pos = pygame.math.Vector2(self.p2.x, self.p2.y)

        
        #display map and load collision rects
        if level_index == 0:
            self.collision_rects = self.level1.collision_rects
            self.wall2_rects = self.level1.wall2_rects
        elif level_index == 1:
            self.collision_rects = self.level2.collision_rects
            self.wall2_rects = self.level2.wall2_rects
        elif level_index == 2:
            self.collision_rects = self.level3.collision_rects
            self.wall2_rects = self.level3.wall2_rects
            #print("rects c and w: ", self.collision_rects, self.wall2_rects)
        elif level_index == 3:
            self.collision_rects = self.level4.collision_rects
            self.wall2_rects = self.level4.wall2_rects
        elif level_index == 4:
            self.collision_rects = self.level5.collision_rects
            self.wall2_rects = self.level5.wall2_rects
            self.wall2_rects = self.level5.wall2_rects
        elif level_index == 5:
            self.collision_rects = self.level6.collision_rects
            self.wall2_rects = self.level6.wall2_rects
        elif level_index == 6:
            self.collision_rects = self.level7.collision_rects
            self.wall2_rects = self.level7.wall2_rects
        elif level_index == 7:
            self.collision_rects = self.level8.collision_rects
            self.wall2_rects = self.level8.wall2_rects
        elif level_index == 8:
            self.collision_rects = self.level9.collision_rects
            self.wall2_rects = self.level9.wall2_rects
        elif level_index == 9:
            self.collision_rects = self.level10.collision_rects
            self.wall2_rects = self.level10.wall2_rects
        elif level_index == 10:
            self.collision_rects = self.level11.collision_rects
            self.wall2_rects = self.level11.wall2_rects
        elif level_index == 11:
            self.collision_rects = self.level12.collision_rects
            self.wall2_rects = self.level12.wall2_rects
        elif level_index == 12:
            self.collision_rects = self.level13.collision_rects
            self.wall2_rects = self.level13.wall2_rects

        self.level_index = level_index

        self.bg_mud = pygame.image.load("assets/images/game/background/bg.png").convert_alpha()
        self.trumpet_w = pygame.mixer.Sound("assets/sound/sound_effects/game/trumpet_win.mp3")
        self.trumpet_s = pygame.mixer.Sound("assets/sound/sound_effects/game/trumpet_s.mp3")
        self.explosion_2 = pygame.mixer.Sound("assets/sound/sound_effects/game/explosion-sound-effect-1-free-on-gamesfxpackscom-241821.mp3")


        #load ui
        self.game_ui.load_game_2_ui()


    def display_scene(self):
        self.screen.blit(self.bg_mud, (0,0))
        match self.level_index:
            case 0:
                self.level1.render_map()
            case 1:
                self.level2.render_map()
            case 2:
                self.level3.render_map()
            case 3:
                self.level4.render_map()
            case 4:
                self.level5.render_map()
            case 5:
                self.level6.render_map()
            case 6:
                self.level7.render_map()
            case 7:
                self.level8.render_map()
            case 8:
                self.level9.render_map()
            case 9:
                self.level10.render_map()
            case 10:
                self.level11.render_map()
            case 11:
                self.level12.render_map()
            case 12:
                self.level13.render_map()
        #ui 
        self.game_ui.render_ui()

    def run_gameplay_2(self, pot1, pot2, rb1, rb2, wb1, wb2):

        if self.p1 != None and self.p2 != None:
            self.p1.enemy_tank_rect = self.p2.hit_box_rect
            self.p1.update(self.collision_rects, self.both_tanks_alive, self.wall2_rects, pot1, rb1, wb1)
            self.p2.enemy_tank_rect = self.p1.hit_box_rect
            self.p2.update(self.collision_rects, self.both_tanks_alive, self.wall2_rects, pot2, rb2, wb2)
            for missile in self.p1.missile_list:
                if missile.collided_with_enemy:
                    # pygame.mixer_music.pause()
                    self.explosion_2.play()
                    self.p2 = None
                    self.both_tanks_alive = False
                    self.p1.missile_list.clear()
                    self.current_winner = "p1"
                    self.trumpet_w.play()
                    break
                if missile.collided_with_self:
                    self.explosion_2.play()
                    self.p1 = None
                    self.both_tanks_alive = False
                    self.current_winner = "p2"
                    # pygame.mixer_music.pause()
                    self.trumpet_s.play()

                    break
            if self.both_tanks_alive:
                for missile in self.p2.missile_list:
                    if missile.collided_with_enemy:
                        self.explosion_2.play()
                        self.p1 = None
                        self.both_tanks_alive = False
                        self.p2.missile_list.clear()
                        self.current_winner = "p2"
                        # pygame.mixer_music.pause()
                        self.trumpet_w.play()
                    if missile.collided_with_self:
                        self.explosion_2.play()
                        self.p2 = None
                        self.both_tanks_alive = False
                        self.current_winner = "p1"
                        # pygame.mixer_music.pause()
                        self.trumpet_s.play()
        else:

            if self.p1 != None:
                self.p1.update(self.collision_rects, self.both_tanks_alive, self.wall2_rects, pot1, rb1, wb1)
            if self.p2 != None:
                self.p2.update(self.collision_rects, self.both_tanks_alive, self.wall2_rects, pot2, rb2, wb2)
            # self.screen.blit(self.game_over_text, (300, 200))
            # self.screen.blit(self.button_text, (400, 300))
            self.game_over_text = self.title_font.render(f"{self.current_winner} Wins!", True, "white")
            self.screen.blit(self.banner, (0, 200))
            self.screen.blit(self.game_over_text, (325, 220))
            self.screen.blit(self.button_text, (415, 305))
            if self.next_text_transparency_bool == False:
                self.next_text_transparency -= 8
            if self.next_text_transparency <= 0:
                self.next_text_transparency_bool = True
            if self.next_text_transparency_bool == True:
                self.next_text_transparency += 8
            if self.next_text_transparency >= 255:
                self.next_text_transparency_bool = False
            self.button_text.set_alpha(self.next_text_transparency)
        



# class scene_results:

#     def __init__(self, screen):
#         self.screen = screen
#         self.title_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 100)
#         self.winner_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 50)
#         self.small_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 25)

#         self.player_icon_bg = pygame.image.load("assets/images/menus/resutls_bg.png").convert_alpha()

#         self.original_ribbon = pygame.image.load("assets/images/menus/results_ribbon.png").convert_alpha()
#         self.ribbon = self.original_ribbon.copy()
#         self.ribbon_x = 230
#         self.ribbon_y = 350
        
#         self.zoom_bool = True
#         self.zoom_scalar = 1

#         self.xpos = 440
#         self.ypos = 250

#         self.alpha_value = 230
#         self.alpha_bool = False

#     def load_scene(self):
#         self.title = self.title_font.render('RESULTS', True, (255,255,255) )
#         self.game_mode = "sudden_death"
#         self.green_tank = pygame.image.load("assets/images/menus/tank icon green.png").convert_alpha()
#         self.blue_tank = pygame.image.load("assets/images/menus/tank icon blue.png").convert_alpha()
#         self.red_tank = pygame.image.load("assets/images/menus/tank icon red.png").convert_alpha()
#         self.gray_tank = pygame.image.load("assets/images/menus/tank icon gray.png").convert_alpha()
#         self.green_tank = pygame.transform.scale_by(self.green_tank, 6)
#         self.blue_tank = pygame.transform.scale_by(self.blue_tank, 6)
#         self.red_tank = pygame.transform.scale_by(self.red_tank, 6)
#         self.gray_tank = pygame.transform.scale_by(self.gray_tank, 6)
#         self.next_text = self.small_font.render('press any button to continue', True, (255, 255, 255))
#         self.selected_rect = pygame.Surface((300, 300), pygame.SRCALPHA)
#         self.selected_rect.fill((0, 0, 0, self.alpha_value))


#     def display_scene(self, gm, gp1_w, gp2_w, p1_tank_index, p2_tank_index):

#         self.game_mode = gm
#         self.screen.blit(self.title, (290, 50))
#         self.screen.blit(self.player_icon_bg, (390, 175))

#         # Create a new surface for the text with alpha support
#         text_surface = self.small_font.render('press any button to continue', True, (255, 255, 255))
#         text_surface.set_alpha(self.alpha_value)

#         # Blit the text onto the screen directly
#         self.screen.blit(text_surface, (295, 550))

#         if self.alpha_value >= 255:
#             self.alpha_bool = False
#         if self.alpha_value <= 0:
#             self.alpha_bool = True
#         if self.alpha_bool:
#             self.alpha_value += 4
#         if self.alpha_bool == False:
#             self.alpha_value -= 4

#         #make book and alpha val changer

#         self.winner_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 50)
#         if self.game_mode == 1:
#             self.winner_text = self.winner_font.render(f"{gp1_w} WINS!", True, (255,255,255) )

#             if gp1_w == "p1":
#                 if p1_tank_index == 0:
#                     self.screen.blit(self.green_tank, (self.xpos, self.ypos))
#                 elif p1_tank_index == 1:
#                     self.screen.blit(self.blue_tank, (self.xpos, self.ypos))
#                 elif p1_tank_index == 2:
#                     self.screen.blit(self.red_tank, (self.xpos, self.ypos))
#                 elif p1_tank_index == 3:
#                     self.screen.blit(self.gray_tank, (self.xpos, self.ypos))
#             if gp1_w == "p2":
#                 if p2_tank_index == 0:
#                     self.screen.blit(self.green_tank, (self.xpos, self.ypos))
#                 elif p2_tank_index == 1:
#                     self.screen.blit(self.blue_tank, (self.xpos, self.ypos))
#                 elif p2_tank_index == 2:
#                     self.screen.blit(self.red_tank, (self.xpos, self.ypos))
#                 elif p2_tank_index == 3:
#                     self.screen.blit(self.gray_tank, (self.xpos, self.ypos))
#             self.screen.blit(self.ribbon, (self.ribbon_x-20,340))
#             self.screen.blit(self.winner_text, (400, 500))

#         if self.game_mode == 2:
#             self.winner_text = self.winner_font.render(f"{gp2_w} WINS!", True, (255,255,255) )
#             if gp2_w == "p1":
#                 if p1_tank_index == 0:
#                     self.screen.blit(self.green_tank, (self.xpos, self.ypos))
#                 elif p1_tank_index == 1:
#                     self.screen.blit(self.blue_tank, (self.xpos, self.ypos))
#                 elif p1_tank_index == 2:
#                     self.screen.blit(self.red_tank, (self.xpos, self.ypos))
#                 elif p1_tank_index == 3:
#                     self.screen.blit(self.gray_tank, (self.xpos, self.ypos))
#             if gp2_w == "p2":
#                 if p2_tank_index == 0:
#                     self.screen.blit(self.green_tank, (self.xpos, self.ypos))
#                 elif p2_tank_index == 1:
#                     self.screen.blit(self.blue_tank, (self.xpos, self.ypos))
#                 elif p2_tank_index == 2:
#                     self.screen.blit(self.red_tank, (self.xpos, self.ypos))
#                 elif p2_tank_index == 3:
#                     self.screen.blit(self.gray_tank, (self.xpos, self.ypos))
#             self.screen.blit(self.ribbon, (self.ribbon_x-20,340))
#             self.screen.blit(self.winner_text, (400, 500))
#             #self.screen.blit(self.next_text, (325, 550))

#     def run_results(self):
#         # if self.zoom_bool:
#         #     self.zoom_scalar -= .001
#         #     self.ribbon_x += .005
#         # if self.zoom_scalar <= .95:
#         #     self.zoom_bool = False
#         # if self.zoom_bool == False:
#         #     self.zoom_scalar += .001
#         #     self.ribbon_x -= .005
#         # if self.zoom_scalar >= 1:
#         #     self.zoom_bool = True

#         self.ribbon = pygame.transform.scale_by(self.original_ribbon, self.zoom_scalar)
#         #if self.game_mode == "sudden_death":

class scene_results:

    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 100)
        self.winner_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 50)
        self.small_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 25)

        self.player_icon_bg = pygame.image.load("assets/images/menus/resutls_bg.png").convert_alpha()

        self.original_ribbon = pygame.image.load("assets/images/menus/results_ribbon.png").convert_alpha()
        self.ribbon = self.original_ribbon.copy()
        self.ribbon_x = 230
        self.ribbon_y = 350
        
        self.zoom_bool = True
        self.zoom_scalar = 1

        self.xpos = 440
        self.ypos = 250

        self.alpha_value = 230
        self.alpha_bool = False

    def load_scene(self):
        self.title = self.title_font.render('RESULTS', True, (255,255,255) )
        self.game_mode = "sudden_death"
        self.green_tank = pygame.image.load("assets/images/menus/tank icon green.png").convert_alpha()
        self.blue_tank = pygame.image.load("assets/images/menus/tank icon blue.png").convert_alpha()
        self.red_tank = pygame.image.load("assets/images/menus/tank icon red.png").convert_alpha()
        self.gray_tank = pygame.image.load("assets/images/menus/tank icon gray.png").convert_alpha()
        self.green_tank = pygame.transform.scale_by(self.green_tank, 6)
        self.blue_tank = pygame.transform.scale_by(self.blue_tank, 6)
        self.red_tank = pygame.transform.scale_by(self.red_tank, 6)
        self.gray_tank = pygame.transform.scale_by(self.gray_tank, 6)
        self.next_text = self.small_font.render('press any button to continue', True, (255, 255, 255))
        self.selected_rect = pygame.Surface((300, 300), pygame.SRCALPHA)
        self.selected_rect.fill((0, 0, 0, self.alpha_value))


    def display_scene(self, gm, gp1_w, gp2_w, p1_tank_index, p2_tank_index):

        self.game_mode = gm
        self.screen.blit(self.title, (290, 50))
        self.screen.blit(self.player_icon_bg, (390, 175))

        # Create a new surface for the text with alpha support
        text_surface = self.small_font.render('press any button to continue', True, (255, 255, 255))
        text_surface.set_alpha(self.alpha_value)

        # Blit the text onto the screen directly
        self.screen.blit(text_surface, (295, 550))

        if self.alpha_value >= 255:
            self.alpha_bool = False
        if self.alpha_value <= 0:
            self.alpha_bool = True
        if self.alpha_bool:
            self.alpha_value += 4
        if self.alpha_bool == False:
            self.alpha_value -= 4

        #make book and alpha val changer

        self.winner_font = pygame.font.Font('assets/fonts/ShapeBitRegular-VGZvl.otf', 50)
        if self.game_mode == 1:
            self.winner_text = self.winner_font.render(f"{gp1_w} WINS!", True, (255,255,255) )

            if gp1_w == "p1":
                if p1_tank_index == 0:
                    self.screen.blit(self.green_tank, (self.xpos, self.ypos))
                elif p1_tank_index == 1:
                    self.screen.blit(self.blue_tank, (self.xpos, self.ypos))
                elif p1_tank_index == 2:
                    self.screen.blit(self.red_tank, (self.xpos, self.ypos))
                elif p1_tank_index == 3:
                    self.screen.blit(self.gray_tank, (self.xpos, self.ypos))
            if gp1_w == "p2":
                if p2_tank_index == 0:
                    self.screen.blit(self.green_tank, (self.xpos, self.ypos))
                elif p2_tank_index == 1:
                    self.screen.blit(self.blue_tank, (self.xpos, self.ypos))
                elif p2_tank_index == 2:
                    self.screen.blit(self.red_tank, (self.xpos, self.ypos))
                elif p2_tank_index == 3:
                    self.screen.blit(self.gray_tank, (self.xpos, self.ypos))
            self.screen.blit(self.ribbon, (self.ribbon_x-20,340))
            self.screen.blit(self.winner_text, (400, 500))

        if self.game_mode == 2:
            self.winner_text = self.winner_font.render(f"{gp2_w} WINS!", True, (255,255,255) )
            if gp2_w == "p1":
                if p1_tank_index == 0:
                    self.screen.blit(self.green_tank, (self.xpos, self.ypos))
                elif p1_tank_index == 1:
                    self.screen.blit(self.blue_tank, (self.xpos, self.ypos))
                elif p1_tank_index == 2:
                    self.screen.blit(self.red_tank, (self.xpos, self.ypos))
                elif p1_tank_index == 3:
                    self.screen.blit(self.gray_tank, (self.xpos, self.ypos))
            if gp2_w == "p2":
                if p2_tank_index == 0:
                    self.screen.blit(self.green_tank, (self.xpos, self.ypos))
                elif p2_tank_index == 1:
                    self.screen.blit(self.blue_tank, (self.xpos, self.ypos))
                elif p2_tank_index == 2:
                    self.screen.blit(self.red_tank, (self.xpos, self.ypos))
                elif p2_tank_index == 3:
                    self.screen.blit(self.gray_tank, (self.xpos, self.ypos))
            self.screen.blit(self.ribbon, (self.ribbon_x-20,340))
            self.screen.blit(self.winner_text, (400, 500))
            #self.screen.blit(self.next_text, (325, 550))

    def run_results(self):
        # if self.zoom_bool:
        #     self.zoom_scalar -= .001
        #     self.ribbon_x += .005
        # if self.zoom_scalar <= .95:
        #     self.zoom_bool = False
        # if self.zoom_bool == False:
        #     self.zoom_scalar += .001
        #     self.ribbon_x -= .005
        # if self.zoom_scalar >= 1:
        #     self.zoom_bool = True

        self.ribbon = pygame.transform.scale_by(self.original_ribbon, self.zoom_scalar)
        #if self.game_mode == "sudden_death":