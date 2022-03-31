import pygame, random, sys, time

pygame.init()
Clock = pygame.time.Clock()

ScreenWidth = 1280
ScreenHeight = 720
tile_size = 40

pygame.display.set_caption("Pygame RPG")
game_window = pygame.display.set_mode((ScreenWidth,ScreenHeight))

Player = pygame.Rect((ScreenWidth/2, ScreenHeight/2), (32, 32))
Enemy = pygame.Rect((ScreenWidth/2, 600), (64, 64))

# main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    Clock.tick(60)