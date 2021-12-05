#11/29/2021
import pygame
import time
import random
import os
import sys
pygame.init()

screen = pygame.display.set_mode((1024, 576))

player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/player1.png"), "r")
player2_img = pygame.image.load(os.path.join(sys.path[0], "assets/player2.png"), "r")
dead_img = pygame.image.load(os.path.join(sys.path[0], "assets/dead.png"), "r")
enemy_img = pygame.image.load(os.path.join(sys.path[0], "assets/enemy.png"), "r")
laser_img = pygame.image.load(os.path.join(sys.path[0], "assets/laser.png"), "r")
spike_img = pygame.image.load(os.path.join(sys.path[0], "assets/spike.png"), "r")
floor_img = pygame.image.load(os.path.join(sys.path[0], "assets/floor.png"), "r")
laser_shot_img = pygame.image.load(os.path.join(sys.path[0], "assets/laser_shot.png"), "r")
warning_laser_img = pygame.image.load(os.path.join(sys.path[0], "assets/warning_laser.png"), "r")
x_laser_img = pygame.image.load(os.path.join(sys.path[0], "assets/x_laser.png"), "r")
play_small_img = pygame.image.load(os.path.join(sys.path[0], "assets/play_small.png"), "r")
play_big_img = pygame.image.load(os.path.join(sys.path[0], "assets/play_big.png"), "r")
help_small_img = pygame.image.load(os.path.join(sys.path[0], "assets/help_small.png"), "r")
help_big_img = pygame.image.load(os.path.join(sys.path[0], "assets/help_big.png"), "r")
exit_small_img = pygame.image.load(os.path.join(sys.path[0], "assets/exit_small.png"), "r")
exit_big_img = pygame.image.load(os.path.join(sys.path[0], "assets/exit_big.png"), "r")
up_key_img = pygame.image.load(os.path.join(sys.path[0], "assets/up_key.png"), "r")
down_key_img = pygame.image.load(os.path.join(sys.path[0], "assets/down_key.png"), "r")
left_key_img = pygame.image.load(os.path.join(sys.path[0], "assets/left_key.png"), "r")
right_key_img = pygame.image.load(os.path.join(sys.path[0], "assets/right_key.png"), "r")
w_key_img = pygame.image.load(os.path.join(sys.path[0], "assets/w_key.png"), "r")
a_key_img = pygame.image.load(os.path.join(sys.path[0], "assets/a_key.png"), "r")
s_key_img = pygame.image.load(os.path.join(sys.path[0], "assets/s_key.png"), "r")
d_key_img = pygame.image.load(os.path.join(sys.path[0], "assets/d_key.png"), "r")
up_key_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/up_key_down.png"), "r")
down_key_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/down_key_down.png"), "r")
left_key_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/left_key_down.png"), "r")
right_key_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/right_key_down.png"), "r")
w_key_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/w_key_down.png"), "r")
a_key_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/a_key_down.png"), "r")
s_key_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/s_key_down.png"), "r")
d_key_down_img = pygame.image.load(os.path.join(sys.path[0], "assets/d_key_down.png"), "r")
menu_arrow_img = pygame.image.load(os.path.join(sys.path[0], "assets/menu_arrow.png"), "r")
font = font = pygame.font.SysFont(None, 72)
loop = True
x = 0
y = 0

class player():
    def __init__(self, player_x, player_y):
        self.x = player_x
        self.y = player_y
        self.hitbox = 90
    def render(self):
        if self.x < 0:
            self.x = 0
        if self.x > 934:
            self.x = 934
        if self.y < 0:
            self.y = 0
        if self.y > 486:
            self.y = 486
            

            
game_loop = False 
menu_option = 1    
tutorial_loop = 0

while loop:
    
    for key in pygame.event.get():
        if key.type == pygame.QUIT:
            pygame.quit()
            exit()
        if key.type == pygame.KEYDOWN:
            
            if key.key == pygame.K_SPACE or key.key == pygame.K_RETURN:
                if menu_option == 1:
                    game_loop = True
                if menu_option == 2:
                    tutorial_loop = True
                if menu_option == 3:
                    pygame.quit()
                    exit()
            
            if key.key == pygame.K_DOWN or key.key == pygame.K_s:
                menu_option += 1
            if key.key == pygame.K_UP or key.key == pygame.K_w:
                menu_option -= 1
            if menu_option == 0:
                menu_option = 3
            if menu_option == 4:
                menu_option = 1
                
    screen.blit(floor_img, (0, 0))
    
    screen.blit(play_small_img, (312, 28))
    screen.blit(help_small_img, (312, 228))
    screen.blit(exit_small_img, (312, 428))
    
    
    if menu_option == 1:
        screen.blit(play_big_img, (302, 22))
        screen.blit(menu_arrow_img, (150, 38))
    if menu_option == 2:
        screen.blit(help_big_img, (302, 222))
        screen.blit(menu_arrow_img, (150, 238))
    if menu_option == 3:
        screen.blit(exit_big_img, (302, 422))
        screen.blit(menu_arrow_img, (150, 438))
        
    #Tutorial    
    if tutorial_loop:
        tutorial_count = 1
        tutorial1_text = font.render("Use WASD and Arrow Keys to move", True, (0, 0, 0))
        tutorial1_x = 200
        tutorial1_p1_y = 130
        tutorial1_p2_y = 316
        tutorial2_1_text = font.render("If two players touch each other", True, (0, 0, 0))
        tutorial2_2_text = font.render("they will be shocked", True, (0, 0, 0))
        tutorial2_p1_x = 100
        tutorial2_p2_x = 800
        tutorial_shock_count = 0
        tutorial_wasd_loop = 0
        tutorial_enemy_x = 1100
        tutorial_spike_y = -50
        tutorial_spike_wait = 1
        tutorial3_text = font.render("Touching red squares will kill you", True, (0, 0, 0))
        tutorial4_text = font.render("Touching spikes will also kill you", True, (0, 0, 0,))
        tutorial5_text = font.render("Giant red laser beams will kill you", True, (0, 0, 0,))
        tutorial_x_laser_wait = 0
        tutorial_x_laser_move_back = False
        tutorial_x_laser_warning = False
        tutorial_x_laser_laser = False
        tutorial_x_laser_x = 1050
        player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/player1.png"), "r")
        player2_img = pygame.image.load(os.path.join(sys.path[0], "assets/player2.png"), "r")
        tutorial6_1_text = font.render("Moving while a blue laser is moving", True, (0, 0, 0))
        tutorial6_2_text = font.render("through you will kill you", True, (0, 0, 0))
        tutorial6_p1_y = 250
        tutorial6_timer = 0
        tutorial6_move_direction = 0
        tutorial_y_laser_x = 1100
        
    while tutorial_loop:
        screen.blit(floor_img, (0, 0))
        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
                exit()
            if key.type == pygame.KEYDOWN:
                if key.key == pygame.K_SPACE or key.key == pygame.K_RETURN:
                    tutorial_count += 1
        if tutorial_count == 1:
            if 0 <= tutorial_wasd_loop < 20:
                screen.blit(d_key_down_img, (755, 205))
                screen.blit(right_key_down_img, (755, 405))
                tutorial1_x += 5
                
            else:
                screen.blit(d_key_img, (750, 200))
                screen.blit(right_key_img, (750, 400))
                
            if 20 <= tutorial_wasd_loop < 40:
                screen.blit(s_key_down_img, (705, 205))
                screen.blit(down_key_down_img, (705, 405))
                tutorial1_p1_y += 5
                tutorial1_p2_y += 5
            else:
                screen.blit(s_key_img, (700, 200))
                screen.blit(down_key_img, (700, 400))
                
            if 40 <= tutorial_wasd_loop < 60:
                screen.blit(a_key_down_img, (655, 205))
                screen.blit(left_key_down_img, (650, 405))
                tutorial1_x -= 5
            else:
                screen.blit(a_key_img, (650, 200))
                screen.blit(left_key_img, (650, 400))
                
            if 60 <= tutorial_wasd_loop < 80:
                screen.blit(w_key_down_img, (705, 155))
                screen.blit(up_key_down_img, (705, 355))
                tutorial1_p1_y -= 5
                tutorial1_p2_y -= 5
            else:
                screen.blit(w_key_img, (700, 150))
                screen.blit(up_key_img, (700, 350))
                    
            if tutorial_wasd_loop == 79:
                tutorial_wasd_loop = 0
                
            tutorial_wasd_loop += 1
            screen.blit(player1_img, (tutorial1_x, tutorial1_p1_y))
            screen.blit(player2_img, (tutorial1_x, tutorial1_p2_y))
            screen.blit(tutorial1_text, (100, 30))
            
        if tutorial_count == 2:
            if tutorial_shock_count == 0:
                tutorial2_p1_x += 5
                tutorial2_p2_x -= 5
            if tutorial2_p1_x == 405:
                tutorial_shock_count = 20
                tutorial2_p1_x = 355
                tutorial2_p2_x = 545
            if tutorial_shock_count > 0:
                tutorial_shock_count -= 1
                
            if tutorial_shock_count % 5 == 0:
                player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/shocked_2.png"), "r")
                player2_img = pygame.image.load(os.path.join(sys.path[0], "assets/shocked_2.png"), "r")
            else:
                player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/shocked_1.png"), "r")
                player2_img = pygame.image.load(os.path.join(sys.path[0], "assets/shocked_1.png"), "r")
                
            if tutorial_shock_count == 0:
                player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/player1.png"), "r")
                player2_img = pygame.image.load(os.path.join(sys.path[0], "assets/player2.png"), "r")
            
            screen.blit(tutorial2_1_text, (100, 30))
            screen.blit(tutorial2_2_text, (100, 90))
            screen.blit(player1_img, (tutorial2_p1_x, 300))
            screen.blit(player2_img, (tutorial2_p2_x, 300))
     
        if tutorial_count == 3:
            tutorial_enemy_x -= 5
            screen.blit(enemy_img, (tutorial_enemy_x, 300))
            screen.blit(enemy_img, (tutorial_enemy_x - 100, 200))
            screen.blit(enemy_img, (tutorial_enemy_x + 100, 400))
            screen.blit(tutorial3_text, (100, 30))
            if tutorial_enemy_x <= -180:
                tutorial_enemy_x = 1200
            
        if tutorial_count == 4:
            if tutorial_spike_wait == 1:
                tutorial_spike_y += 5
            if tutorial_spike_y == 0 and tutorial_spike_wait == 1:
                tutorial_spike_wait = 50
            if tutorial_spike_wait > 1:
                tutorial_spike_wait -= 1
            if tutorial_spike_y > 576:
                tutorial_spike_y = -50
            screen.blit(tutorial4_text, (100, 30))
            screen.blit(spike_img, (910, tutorial_spike_y))
            screen.blit(spike_img, (40, tutorial_spike_y))
            
        if tutorial_count == 5:
            if tutorial_x_laser_wait == 0 and tutorial_x_laser_move_back == False:
                tutorial_x_laser_x -= 1
                tutorial_x_laser_laser = False
            if tutorial_x_laser_x < 950:
                tutorial_x_laser_x = 950
            if tutorial_x_laser_x == 950 and tutorial_x_laser_wait == 0:
                tutorial_x_laser_wait = 120
            if tutorial_x_laser_wait > 1:
                tutorial_x_laser_wait -= 1
            if tutorial_x_laser_wait > 60:
                tutorial_x_laser_warning = True
            if 1 < tutorial_x_laser_wait < 60:
                tutorial_x_laser_laser = True
                tutorial_x_laser_warning = False
            if tutorial_x_laser_wait == 1:
                tutorial_x_laser_wait = 0
                tutorial_x_laser_move_back = True
            if tutorial_x_laser_move_back:
                tutorial_x_laser_x += 1
                tutorial_x_laser_laser = False
            if tutorial_x_laser_x == 1074 and tutorial_x_laser_move_back:
                tutorial_x_laser_move_back = False
                tutorial_x_laser_x = 1050
                
            screen.blit(tutorial5_text, (100, 30))
            screen.blit(laser_shot_img, (tutorial_x_laser_x, 300))
            if tutorial_x_laser_warning:
                screen.blit(warning_laser_img, (2, 309))
            if tutorial_x_laser_laser:
                screen.blit(x_laser_img, (2, 309))
                
        if tutorial_count == 6:
            player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/player1.png"), "r")
            if 30 < tutorial6_timer <= 60:
                if tutorial6_move_direction % 2 == 0:
                    tutorial6_p1_y += 5
                else:
                    tutorial6_p1_y -= 5
                
            tutorial6_timer += 1
            tutorial_y_laser_x -= 7
            if tutorial_y_laser_x < -10:
                tutorial_y_laser_x = 1100
                tutorial6_move_direction += 1
                tutorial6_timer = 0
                
            screen.blit(player1_img, (400, tutorial6_p1_y))
            screen.blit(laser_img, (tutorial_y_laser_x, 0))
            screen.blit(tutorial6_1_text, (100, 30))
            screen.blit(tutorial6_2_text, (100, 90))
                
        if tutorial_count == 7:
                tutorial_loop = False
                
            
        pygame.display.flip()
        time.sleep(0.016)
            
        
    if game_loop:
        player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/player1.png"), "r")
        player2_img = pygame.image.load(os.path.join(sys.path[0], "assets/player2.png"), "r")
        death1 = 0
        death2 = 0
    
        class enemy():
            def __init__(self, first_rand, second_rand):
                self.x = random.randint(first_rand, second_rand)
                self.y = random.randint(0, 486)
            def render(self):
                self.x -= 5
                if self.x < -90:
                    self.x = random.randint(1080, 1500)
                    self.y = random.randint(0, 486)
                
        class y_laser():
            def __init__(self, first_rand, second_rand):
                self.x = random.randint(first_rand, second_rand)
                self.y = 0
            def render(self):
                self.x -= 7
                if self.x < -20:
                    self.x = random.randint(5000, 7000)
                
        class spike():
            def __init__(self, first_rand, second_rand):
                self.x = random.randint(0, 974)
                self.y = random.randint(first_rand, second_rand) * -1
                self.wait = 1
            def render(self):
                if self.wait == 1:
                    self.y += 5
                if self.y > 600:
                    self.y = random.randint(500, 1000) * -1
                    self.x = random.randint(0, 974)
                if 0 < self.y < 5:
                    self.y = 0
                if self.y == 0 and self.wait == 1:
                    self.wait = 50
                if self.wait > 1:
                    self.wait -= 1
    
        class x_laser():
            def __init__(self, first_rand, second_rand):
                self.wait = 0
                self.move_back = False
                self.warning = False
                self.laser = False
                self.x = random.randint(first_rand, second_rand)
                self.y = random.randint(0, 536)
            def render(self):
                if self.wait == 0 and self.move_back == False:
                    self.x -= 1
                    self.laser = False
                if self.x < 950:
                    self.x = 950
                if self.x == 950 and self.wait == 0:
                    self.wait = 120
                if self.wait > 1:
                    self.wait -= 1
                if self.wait > 60:
                    self.warning = True
                if 1 < self.wait < 60:
                    self.laser = True
                    self.warning = False
                if self.wait == 1:
                    self.wait = 0
                    self.move_back = True
                if self.move_back:
                    self.x += 1
                    self.laser = False
                if self.x == 1074 and self.move_back:
                    self.move_back = False
                    self.x = random.randint(1900, 2200)
    
        death1 = 0
        death2 = 0
        shock_count = 0

        speed_timer = 0.016
        speed_count = 0
    
        player1 = player(200, 150)
        player2 = player(200, 400)
        enemy1 = enemy(1024, 1300)
        enemy2 = enemy(1400, 1600)
        enemy3 = enemy(1700, 1900)
        enemy_list = [enemy1, enemy2, enemy3]
        y_laser1 = y_laser(5000, 7000)
        spike1 = spike(500, 1500)
        spike2 = spike(2000, 2500)
        spike_list = [spike1, spike2]
        x_laser1 = x_laser(1900, 2200)
    while game_loop:
        pressed_keys = pygame.key.get_pressed()
        #Check if player pushes the "X" button
        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
                exit()
    
    
        #Check for input
        if shock_count == 0:
            if pressed_keys[pygame.K_s]:
                player1.y += 5
            if pressed_keys[pygame.K_w]:
                player1.y -= 5
            if pressed_keys[pygame.K_d]:
                player1.x += 5
            if pressed_keys[pygame.K_a]:
                player1.x -= 5
        
            if pressed_keys[pygame.K_DOWN]:
                player2.y += 5
            if pressed_keys[pygame.K_UP]:
                player2.y -= 5
            if pressed_keys[pygame.K_RIGHT]:
                player2.x += 5
            if pressed_keys[pygame.K_LEFT]:
                player2.x -= 5
        
            #Check for player collision
            if player1.x - player1.hitbox < player2.x < player1.x + player1.hitbox and player1.y - player1.hitbox < player2.y < player1.y + player1.hitbox:
                shock_count = 20
                if pressed_keys[pygame.K_DOWN]:
                    player2.y -= 50
                if pressed_keys[pygame.K_UP]:
                    player2.y += 50
                if pressed_keys[pygame.K_RIGHT]:
                    player2.x -= 50
                if pressed_keys[pygame.K_LEFT]:
                    player2.x += 50
            
                if pressed_keys[pygame.K_s]:
                    player1.y -= 50
                if pressed_keys[pygame.K_w]:
                    player1.y += 50
                if pressed_keys[pygame.K_d]:
                    player1.x -= 50
                if pressed_keys[pygame.K_a]:
                    player1.x += 50
                
        else:
            shock_count -= 1
            if shock_count % 5 == 0:
                player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/shocked_2.png"), "r")
                player2_img = pygame.image.load(os.path.join(sys.path[0], "assets/shocked_2.png"), "r")
            else:
                player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/shocked_1.png"), "r")
                player2_img = pygame.image.load(os.path.join(sys.path[0], "assets/shocked_1.png"), "r")
            if shock_count == 0:
                player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/player1.png"), "r")
                player2_img = pygame.image.load(os.path.join(sys.path[0], "assets/player2.png"), "r")
            
        #render
        player1.render()
        player2.render()
        enemy1.render()
        enemy2.render()
        enemy3.render()
        y_laser1.render()
        spike1.render()
        spike2.render()
        x_laser1.render()
    
        #Check if enemy hits player
        for enemy in enemy_list:
            if enemy.x - player1.hitbox < player1.x < enemy.x + player1.hitbox and enemy.y - player1.hitbox < player1.y < enemy.y + player1.hitbox:
                death1 += 1
            
            if enemy.x - player2.hitbox < player2.x < enemy.x + player2.hitbox and enemy.y - player2.hitbox < player2.y < enemy.y + player2.hitbox:
                death2 += 1
        
        #Check if there's movement in a laser:
        if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_w] or pressed_keys[pygame.K_d] or pressed_keys[pygame.K_a]:
            if player1.x - 10 < y_laser1.x < player1.x + player1.hitbox:
                death1 += 1
        
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_LEFT]:
            if player2.x - 10 < y_laser1.x < player2.x +player2.hitbox:
                death2 += 1
            
        #Check for spike collision
        for spike in spike_list:
            if spike.x - player1.hitbox < player1.x < spike.x + 49 and spike.y - player1.hitbox < player1.y < spike.y + 49 and spike.y > 0:
                death1 += 1
        
            if spike.x - player2.hitbox < player2.x < spike.x + 49 and spike.y - player2.hitbox < player2.y < spike.y + 49 and spike.y > 0:
                death2 += 1
            
        #Check for x_laser collision
        if x_laser1.laser:
            if x_laser1.y - 80 < player1.y < x_laser1.y + 40:
                death1 += 1
            if x_laser1.y - 80 < player2.y < x_laser1.y + 40:
                death2 += 1
    
        
        screen.blit(floor_img, (0, 0))
        screen.blit(enemy_img, (enemy1.x, enemy1.y))
        screen.blit(enemy_img, (enemy2.x, enemy2.y))
        screen.blit(enemy_img, (enemy3.x, enemy3.y))
        screen.blit(spike_img, (spike1.x, spike1.y))
        screen.blit(spike_img, (spike2.x, spike2.y))
        screen.blit(laser_shot_img, (x_laser1.x, x_laser1.y))
        screen.blit(player1_img, (player1.x, player1.y))
        screen.blit(player2_img, (player2.x, player2.y))
        screen.blit(laser_img, (y_laser1.x, y_laser1.y))
    
        if x_laser1.warning:
            screen.blit(warning_laser_img, (2, x_laser1.y + 9))
        if x_laser1.laser:
            screen.blit(x_laser_img, (2, x_laser1.y + 9))
    
    
        #Increase frame rate
        speed_count += 1
    
        if speed_count % 1000 == 0:
            if speed_timer > 0.001:
                speed_timer -= 0.001
            elif speed_timer > 0:
                speed_timer -= 0.0001
    
    
        time.sleep(speed_timer)
        pygame.display.flip()
        
        #Check for death
        if death1 == 1:
            player1_img = pygame.image.load(os.path.join(sys.path[0], "assets/dead.png"), "r")
            game_loop = False
            screen.blit(player1_img, (player1.x, player1.y))
            pygame.display.flip()
            time.sleep(1)
        if death2 == 1:
            player2_img = pygame.image.load(os.path.join(sys.path[0], "assets/dead.png"), "r")
            game_loop = False
            screen.blit(player2_img, (player2.x, player2.y))
            pygame.display.flip()
            time.sleep(1)
        
        
    pygame.display.flip()