import pygame
import pytmx

#render layers to screen maybe render floor first
class map:
    def __init__(self, screen, map_path):
        self.screen = screen
        self.map_data = map_path
        self.collision_layers = ["wall1", "wall2"]
        self.wall2_rects = []
        self.collision_rects = []
        self.top_rects = []
        self.bottom_rects = []
        self.left_rects = []
        self.right_rects = []
        self.maps_scalar = .84
        self.maps_y_offset = 50

    def render_map(self):
        for layer in self.map_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.map_data.get_tile_image_by_gid(gid)
                    if tile:
                        tile = pygame.transform.scale_by(tile, self.maps_scalar+.01)
                        self.screen.blit(tile, (x * self.map_data.tilewidth*self.maps_scalar, y * self.map_data.tileheight*self.maps_scalar + self.maps_y_offset))

        # for rect in self.collision_rects:
        #     pygame.draw.rect(self.screen, "red", rect, 2)
        # for rect in self.wall2_rects:
        #     pygame.draw.rect(self.screen, "blue", rect, 2)


    def get_collision_rects(self):
        #extract rects
        for layer_name in self.collision_layers:
            layer = self.map_data.get_layer_by_name(layer_name)
            if isinstance(layer, pytmx.TiledTileLayer) and layer_name == "wall2":
                for x, y, gid in layer:
                    if gid != 0: #check for valid tile
                        rect = pygame.Rect(
                            x * self.map_data.tilewidth*self.maps_scalar,
                            y * self.map_data.tileheight*self.maps_scalar + self.maps_y_offset,
                            self.map_data.tilewidth*self.maps_scalar,
                            self.map_data.tileheight*self.maps_scalar
                        )
                        self.wall2_rects.append(rect)
            elif isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    if gid != 0: #check for valid tile
                        rect = pygame.Rect(
                            x * self.map_data.tilewidth*self.maps_scalar,
                            y * self.map_data.tileheight*self.maps_scalar + self.maps_y_offset,
                            self.map_data.tilewidth*self.maps_scalar,
                            self.map_data.tileheight*self.maps_scalar
                        )
                        self.collision_rects.append(rect)

