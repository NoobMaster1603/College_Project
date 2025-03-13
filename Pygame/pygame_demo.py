import pygame
from os.path import join
from random import randint,uniform

# Classes or Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('Pygame','images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT-50))
        self.direction = pygame.Vector2()
        self.speed = 300
        
        # Cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_time = 300
        
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_time:
                self.can_shoot = True
    def update(self,dt):
        keys = pygame.key.get_pressed()
        attack_key = pygame.key.get_just_pressed()
        # Player movemnet
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        attack = int(attack_key[pygame.K_SPACE]) 
        # Laser shooting
        if attack and self.can_shoot:
            Laser((all_group,laser_sprite), laser_surface, self.rect.midtop)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            laser_sound.play()
        self.laser_timer()
        # Control the movement speed regardless of the framerate
        self.rect.center += self.direction * self.speed * dt 

class Star(pygame.sprite.Sprite):
    def __init__(self, groups,surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)))

class Meteor(pygame.sprite.Sprite):
    def __init__(self,surf,pos,groups):
        super().__init__(groups)
        self.image = surf
        self.image2 = surf
        self.pos = pos
        self.rect = self.image.get_frect(center = pos)
        self.direction = pygame.Vector2(uniform(-0.5,0.5),1)
        self.speed = randint(100,150)
        self.rotation_speed = randint(40,50)
        self.rotation = 0
    def update(self, dt):
        
        self.rect.center += self.direction * self.speed * dt
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()  # Kill the meteor when it goes off the screen
        
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.image2,self.rotation,1)
        self.rect = self.image.get_frect(center = self.rect.center)
        
class Laser(pygame.sprite.Sprite):
    def __init__(self,groups,surf,pos):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
        
    def update(self,dt):
        self.rect.centery -= 500 * dt  # Move the laser up by 500 pixels per second
        if self.rect.bottom < 0:
            self.kill()  # Kill the laser when it goes off the screen

class Animated_explosion(pygame.sprite.Sprite):
    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_frect(center = pos)
        
    def update(self, dt):
        self.frames_index += 20 * dt
        if self.frames_index >= len(self.frames):
            self.kill()  # Kill the explosion when all frames have been displayed
        else:
            self.image = self.frames[int(self.frames_index)]
    
def collisions():
    global running
    
    player_collide = pygame.sprite.spritecollide(player, meteor_sprite,True,pygame.sprite.collide_mask) # collide_mask ignores the transparent pixels
    if player_collide:
        running = False
        # damage_sound.play()
    
    for laser in laser_sprite:
        laser_collide = pygame.sprite.spritecollide(laser, meteor_sprite,True)
        if laser_collide:
            laser.kill() 
            Animated_explosion(explosion_frames, laser.rect.midtop, all_group)
            explosion_sound.play()

def score():
    # Score
    current_time = pygame.time.get_ticks()//100
    score_surf = font.render(str(current_time),True,'white')
    score_rect = score_surf.get_frect(midbottom = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 50))
    display_surface.blit(score_surf, score_rect)
    
    # Border
    pygame.draw.rect(display_surface, 'white', score_rect.inflate(10,10).move(0,-7),2,10)
    
# General setup
pygame.init()
WINDOW_WIDTH,WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))

pygame.display.set_caption('Game')
icon_surface = pygame.image.load(join('Pygame','images', 'player.png'))
pygame.display.set_icon(icon_surface)

running = True
clock = pygame.time.Clock()

#import recurring images
star_surf = pygame.image.load(join('Pygame','images', 'star.png')).convert_alpha()
laser_surface = pygame.image.load(join('Pygame','images','laser.png')).convert_alpha()
meteor_surface = pygame.image.load(join('Pygame','images','meteor.png')).convert_alpha()
font = pygame.font.Font(join('Pygame','images','Oxanium-Bold.ttf'),25)
explosion_frames = [pygame.image.load(join('Pygame','images','explosion',f'{i}.png')).convert_alpha() for i in range(21)]

# Importing the sounds
laser_sound = pygame.mixer.Sound(join('Pygame','audio','laser.wav'))
laser_sound.set_volume(0.2)
explosion_sound = pygame.mixer.Sound(join('Pygame','audio','explosion.wav'))
explosion_sound.set_volume(0.2)
# damage_sound = pygame.mixer.Sound(join('Pygame','audio','damage.ogg'))
game_sound = pygame.mixer.Sound(join('Pygame','audio','game_music.wav'))
game_sound.set_volume(0.1)
game_sound.play()


# Game object 
all_group = pygame.sprite.Group()
meteor_sprite = pygame.sprite.Group()
laser_sprite = pygame.sprite.Group()

# laser = Laser(all_group,None,None)
for i in range(20):
    star = Star(all_group,star_surf)
player = Player(all_group)

meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event,800)

# Game loop
while running:
    # Controling the framerate in seconds 
    dt = clock.tick(60) / 1000
    
    
    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            x,y = randint(0,WINDOW_WIDTH),randint(-100,-50)
            Meteor(meteor_surface,(x,y),(all_group, meteor_sprite))
    
    # Drawing surface
    display_surface.fill('midnightblue')
    
    # Update
    all_group.update(dt)
    collisions()
        
    # Display 
    all_group.draw(display_surface)
    score()
    
    pygame.display.update()
pygame.quit()