import pygame, random, sys, time

pygame.init()
Clock = pygame.time.Clock()

ScreenWidth = 600
ScreenHeight = 600

pygame.display.set_caption("Pygame RPG")
game_window = pygame.display.set_mode((ScreenWidth,ScreenHeight))


while True:

    pygame.display.flip()
    Clock.tick(60)