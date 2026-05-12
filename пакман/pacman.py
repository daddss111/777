import pygame

class Pacman:
    def __init__(self, x, y):
        
        self.image = pygame.image.load('image/pacman/pacman.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3.5

    def update(self, keys, walls):
        old_x, old_y = self.rect.x, self.rect.y
        
        if keys[pygame.K_LEFT]:  self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]:    self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:  self.rect.y += self.speed

        
        for wall in walls:
            if self.rect.colliderect(wall):
                    self.rect.x, self.rect.y = old_x, old_y 

    def draw(self, window):
            
            window.blit(self.image, self.rect)