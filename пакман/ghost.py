import pygame
import random

class Ghost:
    def __init__(self, x, y, color_img):
        
        self.image = pygame.image.load(color_img)
        self.image = pygame.transform.scale(self.image, (25, 25))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        
        self.direction = random.randint(0, 3)
        self.steps = 0 

    def move(self, walls):
        
        old_x, old_y = self.rect.x, self.rect.y

        if self.direction == 0: self.rect.x -= self.speed
        if self.direction == 1: self.rect.x += self.speed
        if self.direction == 2: self.rect.y -= self.speed
        if self.direction == 3: self.rect.y += self.speed
               
        hit_wall = False
        for wall in walls:
            if self.rect.colliderect(wall):
                hit_wall = True
                break
               
        if hit_wall:
            self.rect.x, self.rect.y = old_x, old_y
            self.direction = random.randint(0, 3) 


    def draw(self, window):
        window.blit(self.image, self.rect)