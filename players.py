import pygame
import math




class Missile:

    def __init__(self, screen, collision_rects, pos, angle, p_num, enemy_tank_rect, current_tank_rect, wall2_rects):
        pygame.mixer.init()
        self.original_image = pygame.image.load("assets/images/game/objects/missle.png").convert_alpha()
        self.image = self.original_image
        self.image = pygame.transform.rotozoom(self.image, -angle, 1)
        self.rect = self.image.get_rect()
        self.barrel_offset = pygame.Vector2(math.cos(math.radians(angle)), math.sin(math.radians(angle))) * 20
        self.pos = pygame.Vector2(pos) + self.barrel_offset
        self.rect.center = self.pos
        self.vel_x = 0
        self.vel_y = 0
        self.flip_horizontal = False
        self.flip_vertical = False
        self.speed = 5
        self.angle = angle
        self.armed = True
        self.lives = 2
        self.lives_cooldown = 5
        self.screen = screen

        self.p_num = p_num
        self.collided_with_enemy = False
        self.enemy_tank_rect = enemy_tank_rect
        self.current_tank_rect = current_tank_rect
        self.collided_with_self = False

        self.collision_rects_map = collision_rects
        self.wall2_rects = wall2_rects
        #("collision rects: ", self.collision_rects_map, " wall2 rects: ", self.wall2_rects)

        self.disarm_distance = self.current_tank_rect.width //2+5

        self.richochet_sound_wood = pygame.mixer.Sound("assets/sound/sound_effects/game/wood wall hit.mp3")
        self.richochet_sound_metal = pygame.mixer.Sound("assets/sound/sound_effects/game/metal wall hit.mp3")

        self.explosion_sound = pygame.mixer.Sound("assets/sound/sound_effects/game/explosion.mp3")
        self.richochet_sound_wood.set_volume(5)
        self.richochet_sound_metal.set_volume(5)
        self.explosion_sound.set_volume(2)


    def active(self):
        if self.armed:
            rad = math.radians(self.angle)
            if self.flip_horizontal:
                self.vel_x = math.cos(rad) * -self.speed
            else:
                self.vel_x = math.cos(rad) * self.speed

            if self.flip_vertical:
                self.vel_y = math.sin(rad) * -self.speed
            else:
                self.vel_y = math.sin(rad) * self.speed

            next_pos = self.pos + pygame.Vector2(self.vel_x, self.vel_y)

            old_lives = self.lives
            self.check_collisions(self.collision_rects_map, next_pos, self.wall2_rects)#add collision rects for enemy tank
            if self.lives != old_lives and self.lives <= 0:
                if self.lives <= 0:
                    #("missle destroyed")
                    self.explosion_sound.play()
                    return False

            self.pos = next_pos
            self.rect.center = (self.pos)

            self.disarm_distance -= self.speed

            if self.lives_cooldown > 0:
                self.lives_cooldown -= 1
            return True

    def check_collisions(self, collision_rects, next_pos, wall2_rects):
        temp_hit_box_rect = self.rect.copy()
        temp_hit_box_rect.center = next_pos
        for rect in wall2_rects:
           if temp_hit_box_rect.colliderect(rect): #this is were we determine what type of collision it is
                self.richochet_sound_metal.play()
                overlap_left = temp_hit_box_rect.right - rect.left
                overlap_right = rect.right - temp_hit_box_rect.left
                overlap_top = temp_hit_box_rect.bottom - rect.top
                overlap_bottom = rect.bottom - temp_hit_box_rect.top

                smallset_overlap = min(overlap_bottom, overlap_top, overlap_left, overlap_right)

                if smallset_overlap == overlap_left:
                    self.vel_x = -self.vel_x
                    self.pos.x = rect.left - temp_hit_box_rect.width / 2
                    if self.flip_horizontal:
                        self.flip_horizontal = False
                    else:
                        self.flip_horizontal = True

                if smallset_overlap == overlap_right:
                    self.vel_x = -self.vel_x
                    self.pos.x = rect.right + temp_hit_box_rect.width / 2
                    if self.flip_horizontal:
                        self.flip_horizontal = False
                    else:
                        self.flip_horizontal = True

                if smallset_overlap == overlap_top:
                    self.vel_y = -self.vel_y
                    self.pos.y = rect.top + temp_hit_box_rect.height / 2
                    if self.flip_vertical:
                        self.flip_vertical = False
                    else:
                        self.flip_vertical = True

                if smallset_overlap == overlap_bottom:
                    self.vel_y = -self.vel_y
                    self.pos.y = rect.bottom - temp_hit_box_rect.height / 2
                    if self.flip_vertical:
                        self.flip_vertical  = False
                    else:
                        self.flip_vertical = True

                #print("Collision with wall2 detected!")
                #print("lives: ", self.lives)
                return

        for rect in collision_rects:
            if temp_hit_box_rect.colliderect(rect): #this is were we determine what type of collision it is
                self.richochet_sound_wood.play()
                overlap_left = temp_hit_box_rect.right - rect.left
                overlap_right = rect.right - temp_hit_box_rect.left
                overlap_top = temp_hit_box_rect.bottom - rect.top
                overlap_bottom = rect.bottom - temp_hit_box_rect.top

                smallset_overlap = min(overlap_bottom, overlap_top, overlap_left, overlap_right)

                if smallset_overlap == overlap_left:
                    self.vel_x = -self.vel_x
                    self.pos.x = rect.left - temp_hit_box_rect.width / 2
                    if self.flip_horizontal:
                        self.flip_horizontal = False
                    else:
                        self.flip_horizontal = True
                if smallset_overlap == overlap_right:
                    self.vel_x = -self.vel_x
                    self.pos.x = rect.right + temp_hit_box_rect.width / 2
                    if self.flip_horizontal:
                        self.flip_horizontal = False
                    else:
                        self.flip_horizontal = True
                if smallset_overlap == overlap_top:
                    self.vel_y = -self.vel_y
                    self.pos.y = rect.top + temp_hit_box_rect.height / 2
                    if self.flip_vertical:
                        self.flip_vertical = False
                    else:
                        self.flip_vertical = True
                if smallset_overlap == overlap_bottom:
                    self.vel_y = -self.vel_y
                    self.pos.y = rect.bottom - temp_hit_box_rect.height / 2
                    if self.flip_vertical:
                        self.flip_vertical = False
                    else:
                        self.flip_vertical = True
                        

                if self.lives_cooldown <= 0 : #and rect.layer != "wall2":
                    self.lives -= 1
                    self.lives_cooldown = 5
                #print("\nrect: ", rect)
                return
        if temp_hit_box_rect.colliderect(self.enemy_tank_rect):
            self.explosion_sound.play()
            self.collided_with_enemy = True
            return
        elif self.disarm_distance <= 0 and temp_hit_box_rect.colliderect(self.current_tank_rect):
            self.collided_with_self = True
            self.explosion_sound.play()
            return
        else:
            self.collided_with_enemy = False
            self.collided_with_self = False
            return


    def render(self):
        self.image = pygame.transform.rotozoom(self.original_image, -self.angle, 1)
        self.image = pygame.transform.flip(self.image, self.flip_horizontal, self.flip_vertical)
        self.rect = self.image.get_rect(center=self.pos)
        self.screen.blit(self.image, (self.pos.x-10, self.pos.y-5))
        #pygame.draw.rect(self.screen, "red", self.rect, 2)
        #pygame.draw.line(self.screen, "yellow", self.pos, self.pos + pygame.Vector2(self.vel_x, self.vel_y) * 20, 2)


class player:

    def __init__(self, screen, p_num):
        pygame.mixer.init()
        self.x = 150
        self.y = 300
        self.pos = pygame.math.Vector2(self.x, self.y)
        self.rot = 0
        self.top_tank_image = pygame.image.load("assets/images/game/sprites/green_tank_top.png").convert_alpha()
        self.base_tank_image = pygame.image.load("assets/images/game/sprites/green_tank_bottom.png").convert_alpha()
        self.base_tank_image = pygame.transform.scale_by(self.base_tank_image, .65)
        self.top_tank_image = pygame.transform.scale_by(self.top_tank_image, .65)
        self.top_tank_image_copy = self.top_tank_image
        self.base_tank_image_copy = self.base_tank_image
        self.hit_box_rect = self.base_tank_image_copy.get_rect(center = self.pos)
        self.hit_box_rect = self.hit_box_rect.scale_by(.8,.8)
        self.hit_box_rect_copy = self.hit_box_rect

        self.speed = 10

        self.screen = screen

        self.p_num = p_num

        self.can_move = True

        self.is_shooting = False
        self.reload_cooldown = 0
        self.missile_list = []
        self.enemy_tank_rect = None
        
        self.shoot_sound = pygame.mixer.Sound("assets/sound/sound_effects/game/shooting.mp3")
        self.move_sound = pygame.mixer.Sound("assets/sound/sound_effects/game/tankd rive.mp3")
        self.move_sound.set_volume(.5)
        self.tank_idle_sound = pygame.mixer.Sound("assets/sound/sound_effects/game/tank idle.mp3")
        self.tank_rotate_sound = pygame.mixer.Sound("assets/sound/sound_effects/game/turning_sound.mp3")

    def rotation(self):
        self.base_tank_image = pygame.transform.rotate(self.base_tank_image_copy, -self.rot)
        self.top_tank_image = pygame.transform.rotate(self.top_tank_image_copy, -self.rot)
        self.hit_box_rect = self.base_tank_image.get_rect(center=self.pos)


    def get_input(self, collision_rects, wall2_rects, pot, rb, wb):
        self.velocity_x = 0
        self.velocity_y = 0

        #handle acceleration
        if rb == 1:
            self.speed = 2
        else:
            self.speed = 0
        #handle shooting
        if wb == 1:
            self.is_shooting = True
        else:
            self.is_shooting = False

        keys = pygame.key.get_pressed()
        if self.p_num == 0:
            if keys[pygame.K_w]:
                self.speed = 2
                #self.move_sound.play()
            else:
                self.speed = 0
                #self.move_sound.stop()
            if keys[pygame.K_d]:
                if self.rot ==360:
                    self.rot = 0
                else:
                    self.rot +=4
            if keys[pygame.K_a]:
                if self.rot ==0:
                    self.rot = 360
                else:
                    self.rot-=4
            if keys[pygame.K_s]:
                self.is_shooting = True
            else:
                self.is_shooting = False
        else:
            if keys[pygame.K_i]:
                #self.move_sound.play()
                self.speed = 2
            else:
                self.speed = 0
                #self.move_sound.stop()
            if keys[pygame.K_l]:

                if self.rot ==360:
                    self.rot = 0
                else:
                    self.rot +=4
            if keys[pygame.K_j]:

                if self.rot ==0:
                    self.rot = 360
                else:
                    self.rot-=4
            if keys[pygame.K_k]:
                self.is_shooting = True
            else:
                self.is_shooting = False


    def move(self, collision_rects, wall_2rects):
        rad = math.radians(self.rot)
        self.velocity_x = math.cos(rad) * self.speed *1.5 #speed modifier
        self.velocity_y = math.sin(rad) * self.speed*1.5
        next_pos = self.pos + pygame.math.Vector2(self.velocity_x, self.velocity_y)

        self.check_collisions(collision_rects, next_pos, wall_2rects)

        if self.can_move:
            self.pos = next_pos
            self.hit_box_rect.center = self.pos
            self.hit_box_rect.center = self.pos

    def check_collisions(self, collision_rects, next_pos, wall2_rects):
        self.can_move = True

        temp_hit_box_rect = self.hit_box_rect.copy()
        temp_hit_box_rect.center = next_pos
        for rect in collision_rects + wall2_rects:
            if temp_hit_box_rect.colliderect(rect):
                self.can_move = False
                #print("collison detected")
                break

    def shoot(self):
        if self.reload_cooldown == 0 and self.is_shooting:

            return True
        else:
            return False


    def update(self, collision_rects, both_tank_alive, wall2_rects, pot, rb, wb): #if controls not working try explicity passing pot1 and pot2 etc...
        self.get_input(collision_rects, wall2_rects, pot, rb, wb) #also checks collisons
        if both_tank_alive:
            self.move(collision_rects, wall2_rects)
        # self.rotation_esp(pot)
        if self.shoot():
            self.shoot_sound.play()
            self.reload_cooldown = 100
            new_missile = Missile(self.screen, collision_rects, self.pos,  self.rot, self.p_num, self.enemy_tank_rect, self.hit_box_rect, wall2_rects) #maybe change to inside shoot function if mulitple bullets spawn
            self.missile_list.append(new_missile)
        else:
            if self.reload_cooldown != 0:
                self.reload_cooldown -= 2
        for missile in self.missile_list:
            missile.render()
            #print("lives: ", missile.lives)
            if not missile.active():
                self.missile_list.remove(missile)

        self.screen.blit(self.base_tank_image, self.hit_box_rect)
        self.screen.blit(self.top_tank_image, self.hit_box_rect)
        # if self.can_move == True:
        #     pygame.draw.rect(self.screen, "blue", self.hit_box_rect, width=2)
        # else:
        #     pygame.draw.rect(self.screen, "red", self.hit_box_rect, width=2)