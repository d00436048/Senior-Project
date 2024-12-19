import scene_manager

class Scene_Loader:

    def __init__(self, screen, scene_index):
        self.screen = screen
        self.scene_index = scene_index
        self.intro = scene_manager.scene_intro(self.screen)
        self.main = scene_manager.scene_main(self.screen)
        self.mode_select = scene_manager.scene_mode_select(self.screen)

    def boot_to_intro(self):
        self.scene_index = 0
        #load scene 0
        self.intro.load_scene()
        self.intro.display_scene()

    def scene_changer(self, new_index):
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
                self.mode_select.load_scene()
                return
            case 3:
                return
            case 4:
                return
            case 5:
                return
            case 6:
                return
            case 7:
                return
            case 8:
                return
            case 9:
                return
            case default:
                print("error case not found")
                return
