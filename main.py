import pygame
from pygame.locals import *
import serial
import scenes
import scripts.gamedata as gamedata
import scripts.animation as animation
from scene_loader import Scene_Loader


#screen size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600


#init
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #for publish add FULLSCREEN
pygame.mixer.init()


#scene manager setup
scene_index = 0
scenes = ['intro', 'main', 'settings', 'cheats', 'mode_select', 'player_select_1', 'player_select_2', 'level_select', 'gameplay_1', 'game_play_2', 'results']
current_scene = scenes[scene_index]
scene_loader = Scene_Loader(screen, scene_index)


#game loop
running = True
clock = pygame.time.Clock()
FPS = 60

while running:
    clock.tick(FPS)

    scene_loader.boot_to_intro()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:


            #scene managment
            if event.key == K_f:
                if scene_index == 9:
                    scene_index = 0
                else:
                    scene_index += 1
                scene_loader.scene_changer(scene_index)


    #clear the screen
    screen.fill((0,0,0))


    #display current scene
    match scene_index:
        case 0:
            scene_loader.intro.display_scene()
        case 1:
            scene_loader.main.display_scene()
            scene_loader.main.run_main()
        case 2:
            scene_loader.mode_select.display_scene()

    pygame.display.flip()


pygame.quit()