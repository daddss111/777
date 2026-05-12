import pygame
from pacman import Pacman
from ghost import Ghost
import time

pygame.init()

pygame.display.set_caption('pacman')
window = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load('image/bg/bg.jpg'), (800, 800))
pacman = Pacman(450, 450)

ghosts = [
    Ghost(500, 140, 'image/ghost/ghost.png'),
    Ghost(150, 650, 'image/ghost/ghost2.png')
]

matrix = [
    "11111111111111111111", # 1
    "10000000011000000001", # 2
    "10110111011011101101", # 3
    "10000000000000000001", # 4 
    "10110101111110101101", # 5
    "10000100011000100001", # 6
    "11110111011011101111", # 7 
    "11110100000000101111", # 8 
    "11110101100110101111", # 9
    "10000001000010000001", # 10
    "11110101111110101111", # 11
    "11110100000000101111", # 12
    "11110100111110101111", # 13 
    "10000000011000000001", # 14
    "10010111011011101101", # 15 
    "11010000000000001001", # 16
    "10000100011000100001", # 17
    "10111111011011111101", # 18
    "10000000000000000001", # 19
    "11111111111111111111", # 20
]

walls = []
for row_index, row in enumerate(matrix):
    for col_index, char in enumerate(row):
        if char == "1":
                        
            wall_rect = pygame.Rect(col_index * 40 + 8, row_index * 40 + 8, 24, 24)
            walls.append(wall_rect)


dots = []
for row_index, row in enumerate(matrix):
    for col_index, char in enumerate(row):
        if char == "0":
            
            dot_rect = pygame.Rect(col_index * 40 + 18, row_index * 40 + 18, 4, 4)
            dots.append(dot_rect)

score = 0 

pygame.font.init()
font = pygame.font.SysFont('Arial', 24, bold=True)

win_font = pygame.font.SysFont('Arial', 72, bold=True)
game_over = False 
message = ""

while True:
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                
                game_over = False
                score = 0
                pacman.rect.x, pacman.rect.y = 450, 450 
                
    
    if not game_over:
        window.blit(background, (0, 0))

        for dot in dots[:]:
            pygame.draw.circle(window, (255, 255, 100), dot.center, 4)
            if pacman.rect.colliderect(dot):
                dots.remove(dot)
                score += 1

        if len(dots) == 0:
            game_over = True
            message = "Победа"

        keys = pygame.key.get_pressed()
        pacman.update(keys, walls)
        pacman.draw(window)

        for ghost in ghosts:
            ghost.move(walls)
            ghost.draw(window)
            if pacman.rect.colliderect(ghost.rect):
                game_over = True
                message = "Игра закончена"

        score_img = font.render(f"Счёт: {score}", True, (155, 0, 205))
        window.blit(score_img, (20, 20))
    else:
        window.blit(background, (0, 0))
        color = (0, 255, 0) if message == "Победа" else (255, 0, 0)
        end_text = win_font.render(message, True, color)
        window.blit(end_text, (800 // 2 - 150, 800 // 2 - 50)) 
        
        pygame.display.update()
        pygame.time.delay(3000) 
        
        pygame.quit()
        exit()

    
    pygame.display.update()
    clock.tick(60)