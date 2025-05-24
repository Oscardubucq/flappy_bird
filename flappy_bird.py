import pygame
from pygame.locals import *
import random
pygame.init()
clock = pygame.time.Clock()
fps = 60
screen_width = 864
screen_height = 936
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')
#define font
font = pygame.font.SysFont('Bauhaus 93', 60)
#define game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False
#load images
bg = pygame.image.load('images/ville.png')
ground_img = pygame.image.load('images/campagne.png')
botton_img = pygame.image.load('images/restart.png')

def draw_text(text, font, color, x, y):
    textobj = font.render(text, True, color)
    screen.blit(textobj, (x, y))

def reset_game():
    pipe_group.empty()
    bird.rect.x = 100
    bird.rect.y = int(screen_height / 2)
    score = 0
    return score

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            img = pygame.image.load(f'images/bird{num}.png').convert_alpha()
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.vel = 0
        self.clicked = False
    
    def update(self):
        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < screen_height - 150:
                self.rect.y += int(self.vel)
        
        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            
            flapp_speed = 5
            self.counter += 1
            if self.counter >= flapp_speed:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]
            
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        
        else:
            self.image = pygame.transform.scale(self.images[0], (self.images[0].get_width() * 2, self.images[0].get_height() * 2))
                