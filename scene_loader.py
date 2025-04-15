import scene_manager
import pygame
import game_ui

class Scene_Loader:

    def __init__(self, screen, scene_index, icon_index, p1_tank_index, p2_tank_index):
        self.screen = screen
        self.scene_index = scene_index
        self.icon_index = icon_index

        self.p1_tank_index = p1_tank_index
        self.p2_tank_index = p2_tank_index
        self.level_index = 0

        self.intro = scene_manager.scene_intro(self.screen)
        self.main = scene_manager.scene_main(self.screen)
        self.settings = scene_manager.scene_settings(self.screen)
        self.mode_select = scene_manager.scene_mode_select(self.screen)
        self.player_select_1 = scene_manager.scene_player_select_1(self.screen)
        self.player_select_2 = scene_manager.scene_player_select_2(self.screen)
        self.level_select = scene_manager.scene_level_select(self.screen)
        self.gameplay_1 = scene_manager.scene_gameplay_1(self.screen)  
        self.gameplay_2 = scene_manager.scene_gameplay_2(self.screen)
        self.results = scene_manager.scene_results(self.screen)    

    def boot_to_intro(self, elapsed_time):
        self.scene_index = 0
        #load scene 0
        self.intro.load_scene()
        self.intro.display_scene(elapsed_time)
        print("its being called")

    def scene_changer(self, new_index, icon_index, icon2_index):

        self.scene_index = new_index
        match self.scene_index:
            case 0:
                #load intro
                self.intro.load_scene()
                return
            case 1:
                #load main
                self.main.load_scene()
                return
            case 2:
                #load mode_select
                self.settings.load_scene()
                return
            case 3:
                return
            case 4:
                self.mode_select.load_scene()
                return
            case 5:
                self.player_select_1.load_scene()
                self.level_select.level_que = []
                self.gameplay_1.level_que = []
                return
            case 6:
                self.player_select_2.load_scene()
                return
            case 7:
                self.level_select.load_scene()
                return
            case 8:
                self.gameplay_1.load_scene(self.level_index, self.p1_tank_index, self.p2_tank_index)
                return
            case 9:
                self.gameplay_2.load_scene(self.level_index, self.p1_tank_index, self.p2_tank_index)
                return
            case 10:
                self.results.load_scene()
                self.gameplay_2.spawn_loc = True
                self.gameplay_1.game_ui.gameplay_1_active = False
                self.level_select.selected_3 = False
                self.level_select.selected_2 = False
                self.level_select.selected = False
                self.gameplay_1.p1_score = 0
                self.gameplay_1.p2_score = 0
                self.gameplay_1.level_que = []
                self.gameplay_1.round = 0
                self.gameplay_1.round_1_over = False
                self.gameplay_1.round_2_over = False
                self.gameplay_1.round_3_over = False
                return
            case default:
                print("error case not found")
                return
        
        self.icon_index = 0