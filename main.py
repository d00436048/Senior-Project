import cProfile
import pstats
from io import StringIO
import threading
import queue
import pygame
from pygame.locals import *
import serial
import time
import random

from scene_loader import Scene_Loader


#esp32 setup
try:
    esp = serial.Serial('/dev/cu.usbserial-0001', 9600)
    time.sleep(2)
except:
    print("no esp")
    esp = None


#screen size 
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600


#init
pygame.mixer.init()
pygame.init()
pygame_icon = pygame.image.load("assets/images/menus/tank icon green.png")
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("Tanks!", "this is tanks")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.font.init()


scene_index = 0
scenes = ['intro', 'main', 'settings', 'cheats', 'mode_select', 'player_select_1', 'player_select_2', 'level_select', 'gameplay_1', 'game_play_2', 'results']
current_scene = scenes[scene_index]
scene_loader = Scene_Loader(screen, scene_index, icon_index=0, p1_tank_index=0, p2_tank_index=0)


#game loop
running = True
clock = pygame.time.Clock()
FPS = 30
start_time = pygame.time.get_ticks()

#global vars
icon_index = 0
icon2_index = 1 #for two player select tank
p1_tank_index = 0
p2_tank_index = 0
gm = 1
lvl_selected = False



def main():
    #scene manager setup

    switched_scene = False

    sound_on = True
    muisc_on = True
    click_sound = pygame.mixer.Sound("assets/sound/sound_effects/menus/click.mp3")
    punch_sound = pygame.mixer.Sound("assets/sound/sound_effects/menus/hard-slap-46388.mp3")
    menu_music = pygame.mixer.music.load("assets/sound/music/menu music.mp3")

    reload_sound = pygame.mixer.Sound("assets/sound/sound_effects/menus/1911-reload-6248.mp3")
    reload_sound.set_volume(0.5)
    shoot_sound = pygame.mixer.Sound("assets/sound/sound_effects/menus/pistol-shot-233473.mp3")
    shoot_sound.set_volume(0.5)
    reload_channel = pygame.mixer.Channel(1)
    shoot_channel = pygame.mixer.Channel(2)
    global running, scene_index, icon_index, icon2_index, current_scene, start_time, gm, lvl_selected

    if esp == None:
        pot1 = 0
        pot2 = 0
        rb1 = 0
        rb2 = 0
        wb1 = 0
        wb2 = 0


    while running:
        clock.tick(FPS)
        elapsed_time = pygame.time.get_ticks() - start_time

        if muisc_on:
            pygame.mixer_music.set_volume(.25)
        else:
            pygame.mixer_music.set_volume(0)
        if sound_on:
            pygame.mixer.unpause()
        else:
            pygame.mixer.pause()


        # scene_loader.boot_to_intro(elapsed_time)

        
        # if elapsed_time < 4000: #chagne back to four sceonds
        #     scene_index = 0
        # if elapsed_time > 4000 and elapsed_time < 4100:
        #     pygame.mixer.music.play(-1)
        #     pygame.mixer.music.set_volume(.25)
        #     scene_index = 1
        #     scene_loader.scene_changer(scene_index, icon_index=0, icon2_index=0)

        if elapsed_time < 50 and elapsed_time > 0:
            scene_index = 1
            scene_loader.scene_changer(scene_index, icon_index, icon2_index)

        if esp == None:

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:

                    if event.key == K_t:
                        pot1 += 1
                    if event.key == K_y:
                        pot1 -= 1
                    if event.key == K_w:
                        rb1 = 1
                    else:
                        rb1 = 0
                    if event.key == K_e:
                        wb1 = 1
                    else:
                        wb1 = 0


                    #scene managment
                    new_scene_index = scene_index
                    if event.key == K_f: #debug chagne scences
                        if scene_index == 10:
                            new_scene_index = 0
                        else:
                            new_scene_index += 1
                    
                    if event.key == K_j: #move icon/p1 selector
                        if scene_index == 1: # if main
                            reload_channel.play(reload_sound)
                            if icon_index == 0:
                                icon_index = 1
                            elif icon_index != 0:
                                icon_index = 0
                        
                        if scene_index == 2 or scene_index == 4:
                            reload_channel.play(reload_sound)
                            if icon_index != 2:
                                icon_index += 1
                            else:
                                icon_index = 0
                        
                        if scene_index == 6 and scene_loader.player_select_2.get_p1_select() == False:
                            reload_channel.play(reload_sound)
                            if icon_index == 3:
                                icon_index = 0
                            else:
                                icon_index +=1
                        
                        if scene_index == 7 and lvl_selected == False:
                            reload_channel.play(reload_sound)
                            if icon_index == 13:
                                icon_index = 0
                            else:
                                icon_index += 1

                        if scene_index == 8:
                            if scene_loader.gameplay_1.round_1_over == False:
                                scene_loader.gameplay_1.round_1_over = True
                            if scene_loader.gameplay_1.round_1_over == True and scene_loader.gameplay_1.round_2_over == False:
                                scene_loader.gameplay_1.round_2_over = True
                            if scene_loader.gameplay_1.round_1_over == True and scene_loader.gameplay_1.round_2_over == True and scene_loader.gameplay_1.round_3_over == False:
                                scene_loader.gameplay_1.round_3_over = True


                        if scene_index == 9:
                            if scene_loader.gameplay_2.both_tanks_alive == False:
                                new_scene_index = 10
                    
                    if event.key == K_k:
                        if scene_index == 6 and scene_loader.player_select_2.get_p2_select() == False:
                            if icon2_index == 3:
                                icon2_index = 0
                            else:
                                icon2_index +=1


                    if event.key == K_h: #change scene
                        if scene_index == 1:
                            shoot_channel.play(shoot_sound)
                            if icon_index == 0:
                                new_scene_index = 4 #mode select
                            if icon_index == 1:
                                new_scene_index = 2 #settings
                            icon_index = 0

                        if scene_index == 2:
                            shoot_channel.play(shoot_sound)
                            if icon_index == 0:
                                if sound_on == True:
                                    pygame.mixer.pause()
                                    pygame.mixer_music.pause()
                                    reload_channel.pause()
                                    shoot_channel.pause()
                                    sound_on = False
                                    muisc_on = False
                                else:
                                    pygame.mixer.unpause()
                                    pygame.mixer_music.unpause()
                                    reload_channel.unpause()
                                    shoot_channel.unpause()
                                    sound_on = True
                                    muisc_on = True
                            if icon_index == 1:
                                scene_loader.settings.shutdown_pi()
                            if icon_index == 2:
                                new_scene_index = 1 #return to main
                            icon_index = 0

                        if scene_index == 4:
                            shoot_channel.play(shoot_sound)
                            if icon_index == 0:
                                new_scene_index = 6
                                scene_loader.gameplay_1.game_ui.gameplay_1_active = False
                            if icon_index == 1:
                                new_scene_index = 6
                                scene_loader.gameplay_1.game_ui.gameplay_1_active = True
                            if icon_index == 2:
                                new_scene_index = 1 #return to main
                            icon_index = 0

                        if scene_index == 6 and scene_loader.player_select_2.get_p1_select() == False:
                            shoot_channel.play(shoot_sound)
                            scene_loader.player_select_2.set_p1_select(True)
                        elif scene_index == 6 and scene_loader.player_select_2.get_p1_select() == True:
                            shoot_channel.play(shoot_sound)
                            scene_loader.player_select_2.set_p1_select(False)

                        if scene_index == 7: 
                            shoot_channel.play(shoot_sound)
                            if scene_loader.gameplay_1.game_ui.gameplay_1_active:
                                if scene_loader.level_select.selected_3 == False:
                                    scene_loader.level_select.selected_3 = True
                                    scene_loader.level_select.level_que.append(icon_index)
                                elif scene_loader.level_select.selected_2 == False:
                                    scene_loader.level_select.selected_2 = True
                                    scene_loader.level_select.level_que.append(icon_index)
                                elif scene_loader.level_select.selected_3 and scene_loader.level_select.selected_2:
                                    scene_loader.level_select.selected = True
                                    scene_loader.level_select.level_que.append(icon_index)
                                else:
                                    scene_loader.level_select.selected = False
                            else:
                                if lvl_selected == False:
                                    print("setting selected to true")
                                    lvl_selected = True
                                else:
                                    lvl_selected = False
                        

                        if scene_index == 9:
                            if scene_loader.gameplay_2.both_tanks_alive == False:
                                new_scene_index = 10


                    if event.key == K_l:
                        shoot_channel.play(shoot_sound)
                        if scene_index == 6 and scene_loader.player_select_2.get_p2_select() == False:
                            scene_loader.player_select_2.set_p2_select(True)
                        elif scene_index == 6 and scene_loader.player_select_2.get_p2_select() == True:
                            scene_loader.player_select_2.set_p2_select(False)
                        
                        if scene_index == 9 and scene_loader.gameplay_2.both_tanks_alive == False:
                            new_scene_index = 10

                    if event.key == K_g:
                        shoot_channel.play(shoot_sound)
                        if scene_index == 5 and scene_loader.player_select_2.get_p1_select() and scene_loader.player_select_2.get_p2_select():
                            scene_loader.p1_tank_index = icon_index
                            scene_loader.p2_tank_index = icon2_index
                            new_scene_index = 7

                        if scene_index == 6 and scene_loader.player_select_2.get_p1_select() and scene_loader.player_select_2.get_p2_select():
                            scene_loader.p1_tank_index = icon_index
                            scene_loader.p2_tank_index = icon2_index
                            new_scene_index = 7
                        
                        if scene_index == 7 and lvl_selected == True:
                            if icon_index != 13:
                                scene_loader.level_index = icon_index
                            else:
                                icon_index = random.randint(0,12)
                                scene_loader.level_index = icon_index
                            if scene_loader.gameplay_1.game_ui.gameplay_1_active:
                                scene_loader.gameplay_1.level_que = scene_loader.level_select.level_que
                                nl = []
                                for item in scene_loader.gameplay_1.level_que:
                                    if item not in nl:
                                        nl.append(item)
                                scene_loader.gameplay_1.level_que = nl
                                new_scene_index = 8
                            else:
                                new_scene_index = 9
                        
                        if scene_index == 8:
                            gm = 1
                            if scene_loader.gameplay_1.p1_score >= 2 or scene_loader.gameplay_1.p2_score >= 2:
                                new_scene_index = 10

                        if scene_index == 9 and scene_loader.gameplay_2.both_tanks_alive == False:
                            new_scene_index = 10
                            gm = 2

                        if scene_index == 10:
                            shoot_channel.play(shoot_sound)
                            new_scene_index = 1
                            pygame.mixer_music.play()


                    if wb1 == 1:
                        if scene_index == 1:
                            if icon_index == 0:
                                punch_sound.play()
                                new_scene_index = 4 #mode select
                            if icon_index == 1:
                                punch_sound.play()
                                new_scene_index = 2 #settings
                            icon_index = 0

                        if scene_index == 2:
                            if icon_index == 0:
                                if sound_on == True:
                                    pygame.mixer.pause()
                                    sound_on = False
                                else:
                                    pygame.mixer.unpause()
                                    sound_on = True
                            if icon_index == 1:
                                scene_loader.settings.shutdown_pi()
                            if icon_index == 2:
                                punch_sound.play()
                                new_scene_index = 1 #return to main
                            icon_index = 0

                        if scene_index == 4:
                            if icon_index == 0:
                                punch_sound.play()
                                new_scene_index = 6
                            if icon_index == 1:
                                punch_sound.play()
                                new_scene_index = 5
                            if icon_index == 2:
                                punch_sound.play()
                                new_scene_index = 1 #return to main
                            icon_index = 0

                        if scene_index == 5 and scene_loader.player_select_1.get_p1_select() == False:
                            scene_loader.player_select_1.set_p1_select(True)
                        elif scene_index == 5 and scene_loader.player_select_1.get_p2_select() == True:
                            scene_loader.player_select_1.set_p2_select(False)
                        
                        if scene_index == 6 and scene_loader.player_select_2.get_p1_select() == False:
                            scene_loader.player_select_2.set_p1_select(True)
                        elif scene_index == 6 and scene_loader.player_select_2.get_p2_select() == True:
                            scene_loader.player_select_2.set_p2_select(False)

                        if scene_index == 7:
                            if lvl_selected == False:
                                lvl_selected = True
                            else:
                                lvl_selected = False

                        if scene_index == 10:
                            new_scene_index = 1
                    #change to if key pressed
                    scene_index = new_scene_index
                    scene_loader.scene_changer(scene_index, icon_index, icon2_index)


        else:
            if esp.in_waiting > 0:
                line = esp.readline().decode('utf-8', errors='ignore').strip()
                try:
                    pot1, pot2, rb1, wb1, rb2, wb2  = map(int, line.split(','))
                    new_scene_index = scene_index
                    print(pot1, pot2, rb1, wb1, rb2, wb2)

                    #br1 done   
                    if rb1 == 1:
                        print("Rb 1 pressed")
                        #gp2 both tanks selected change scene
                        if scene_index == 6 and scene_loader.player_select_2.get_p1_select() == True and scene_loader.player_select_2.get_p2_select() == True:
                            punch_sound.play()
                            new_scene_index = 7
                        
                        #if level is selected change scene handle randomness etc...
                        if scene_index == 7 and lvl_selected == True:
                            if icon_index != 13:
                                scene_loader.level_index = icon_index
                            else:
                                icon_index = random.randint(0,12)
                                scene_loader.level_index = icon_index
                            if scene_loader.gameplay_1.game_ui.gameplay_1_active:
                                scene_loader.gameplay_1.level_que = scene_loader.level_select.level_que
                                nl = []
                                for item in scene_loader.gameplay_1.level_que:
                                    if item not in nl:
                                        nl.append(item)
                                scene_loader.gameplay_1.level_que = nl
                                new_scene_index = 8
                            else:
                                new_scene_index = 9

                    # if rb2 == 1:
                    #     pass
                    if wb1 == 1:
                        if scene_index == 1:
                            if icon_index == 0:
                                punch_sound.play()
                                new_scene_index = 4 #mode select
                            if icon_index == 1:
                                punch_sound.play()
                                new_scene_index = 2 #settings
                            icon_index = 0

                        if scene_index == 2:
                            if icon_index == 0:
                                if sound_on == True:
                                    pygame.mixer.pause()
                                    sound_on = False
                                else:
                                    pygame.mixer.unpause()
                                    sound_on = True
                            if icon_index == 1:
                                scene_loader.settings.shutdown_pi()
                            if icon_index == 2:
                                punch_sound.play()
                                new_scene_index = 1 #return to main
                            icon_index = 0

                        if scene_index == 4:
                            if icon_index == 0:
                                punch_sound.play()
                                new_scene_index = 6
                            if icon_index == 1:
                                punch_sound.play()
                                new_scene_index = 5
                            if icon_index == 2:
                                punch_sound.play()
                                new_scene_index = 1 #return to main
                            icon_index = 0

                        if scene_index == 5 and scene_loader.player_select_1.get_p1_select() == False:
                            scene_loader.player_select_1.set_p1_select(True)
                        elif scene_index == 5 and scene_loader.player_select_1.get_p2_select() == True:
                            scene_loader.player_select_1.set_p2_select(False)
                        
                        if scene_index == 6 and scene_loader.player_select_2.get_p1_select() == False:
                            scene_loader.player_select_2.set_p1_select(True)
                        elif scene_index == 6 and scene_loader.player_select_2.get_p2_select() == True:
                            scene_loader.player_select_2.set_p2_select(False)

                        if scene_index == 7:
                            if lvl_selected == False:
                                lvl_selected = True
                            else:
                                lvl_selected = False

                        if scene_index == 10:
                            new_scene_index = 1

                    if wb2 == 1:
                        if scene_index == 6 and scene_loader.player_select_2.get_p2_select() == False:
                            scene_loader.player_select_2.set_p2_select(True)
                        elif scene_index == 6 and scene_loader.player_select_2.get_p2_select() == True:
                            scene_loader.player_select_2.set_p2_select(False)


                    #pot1 and pot2
                    if scene_index == 1 or scene_index == 2 or scene_index == 4:
                        pot1_mod = pot1 % 120
                        if pot1_mod <= 40:
                            icon_index = 0

                        elif pot1_mod > 40 and pot1_mod < 80:
                            icon_index = 1

                        elif pot1_mod >= 80:
                            icon_index = 2

                    elif scene_index == 5:
                        if scene_loader.player_select_2.get_p1_select() == False:
                            pot1_mod = pot1 % 90
                            if pot1_mod <= 22:
                                icon_index = 0
                            elif pot1_mod > 22 and pot1_mod < 45:
                                icon_index = 1
                            elif pot1_mod >= 45 and pot1_mod <= 67:
                                icon_index = 2
                            elif pot1_mod > 67:
                                icon_index = 3

                        if scene_loader.player_select_2.get_p2_select() == False:
                            pot2_mod = pot2 % 90
                            if pot2_mod <= 22:
                                icon2_index = 0
                            elif pot2_mod > 22 and pot2_mod < 45:
                                icon2_index = 1
                            elif pot2_mod >= 45 and pot2_mod <= 67:
                                icon2_index = 2
                            elif pot2_mod > 67:
                                icon2_index = 3
                                
                    elif scene_index == 6:
                        if scene_loader.player_select_2.get_p1_select() == False:
                            pot1_mod = pot1 % 90
                            if pot1_mod <= 22:
                                icon_index = 0
                            elif pot1_mod > 22 and pot1_mod < 45:
                                icon_index = 1
                            elif pot1_mod >= 45 and pot1_mod <= 67:
                                icon_index = 2
                            elif pot1_mod > 67:
                                icon_index = 3

                        if scene_loader.player_select_2.get_p2_select() == False:
                            pot2_mod = pot2 % 90
                            if pot2_mod <= 22:
                                icon2_index = 0
                            elif pot2_mod > 22 and pot2_mod < 45:
                                icon2_index = 1
                            elif pot2_mod >= 45 and pot2_mod <= 67:
                                icon2_index = 2
                            elif pot2_mod > 67:
                                icon2_index = 3

                    elif scene_index == 7:
                        if lvl_selected == False:
                            pot1_mod = pot1 % 192
                            if pot1_mod <= 12:
                                icon_index = 1
                            elif pot1_mod > 12 and pot1_mod < 24:
                                icon_index = 2
                            elif pot1_mod >= 24 and pot1_mod < 36:
                                icon_index = 3
                            elif pot1_mod  >= 36 and pot1_mod < 48:
                                icon_index = 4
                            elif pot1_mod >= 48 and pot1_mod < 60:
                                icon_index = 5
                            elif pot1_mod >= 72 and pot1_mod < 84:
                                icon_index = 6
                            elif pot1_mod >= 84 and pot1_mod < 96:
                                icon_index = 7
                            elif pot1_mod >= 96 and pot1_mod < 108:
                                icon_index = 8
                            elif pot1_mod >= 120 and pot1_mod < 132:
                                icon_index = 9
                            elif pot1_mod >= 132 and pot1_mod < 144:
                                icon_index = 10
                            elif pot1_mod >= 144 and pot1_mod < 156:
                                icon_index = 11
                            elif pot1_mod >= 168 and pot1_mod < 180:
                                icon_index = 12
                            elif pot1_mod >= 180:
                                icon_index = 13
                                
                    scene_index = new_scene_index
                    scene_loader.scene_changer(scene_index, icon_index, icon2_index)

                except ValueError:
                    print("cannot find controller data")


        #clear the screen
        screen.fill((0,0,0))


        #display current scene
        match scene_index:
            case 0:
                scene_loader.intro.display_scene(elapsed_time)
            case 1:
                scene_loader.main.display_scene(icon_index)
                scene_loader.main.run_main()
            case 2:
                scene_loader.settings.display_scene()
                scene_loader.settings.run_settings(icon_index, sound_on)
            case 4:
                scene_loader.mode_select.display_scene()
                scene_loader.mode_select.run_mode_select(icon_index)
            case 5:
                scene_loader.player_select_1.display_scene()
                scene_loader.player_select_1.run_player_select_1(icon_index)
            case 6:
                scene_loader.player_select_2.display_scene()
                scene_loader.player_select_2.run_player_select_2(icon_index, icon2_index)
            case 7:
                scene_loader.level_select.display_scene(icon_index)
                if scene_loader.gameplay_1.game_ui.gameplay_1_active:
                    scene_loader.level_select.run_level_select_1(icon_index)
                else:
                    scene_loader.level_select.run_level_select(icon_index, lvl_selected)
            case 8:
                scene_loader.gameplay_1.display_scene() #best 2/3
                scene_loader.gameplay_1.run_gameplay_1(pot1, pot2, rb1, rb2, wb1, wb2)
                if gm == 2:
                    gm = 1

            case 9:
                scene_loader.gameplay_2.display_scene() #1 live
                scene_loader.gameplay_2.run_gameplay_2(pot1, pot2, rb1, rb2, wb1, wb2)
                print(pot1)
                if gm == 1:
                    gm = 2

            case 10:
                scene_loader.results.display_scene(gm, scene_loader.gameplay_1.current_winner, scene_loader.gameplay_2.current_winner, scene_loader.p1_tank_index, scene_loader.p2_tank_index)
                scene_loader.results.run_results()

        pygame.display.flip()

    pygame.mixer_music.stop()
    pygame.quit()

main()


# if __name__ == "__main__":
#     # Use cProfile to profile the main function
#     profiler = cProfile.Profile()
#     profiler.enable()

#     main()

#     profiler.disable()
#     # Save profiling results
#     s = StringIO()
#     ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
#     ps.print_stats()

#     # Save stats to a file for later analysis
#     with open("profiling_stats.txt", "w") as f:
#         f.write(s.getvalue())

#     print("Profiling complete. Stats saved to 'profiling_stats.txt'.")