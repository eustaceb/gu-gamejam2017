import pygame
import sys
from world import *

pygame.init()
if len(sys.argv) != 3:
    width, height = 800, 600
else:
    width, height = sys.argv[1], sys.argv[2]

screen = pygame.display.set_mode((width,height))

game_world = World(screen) 

while True:
    for event in pygame.event.get():
        exit = game_world.process_event(event)
        if (not exit): sys.exit()

    game_world.update()
    game_world.render(screen)

print(width, height)
print("Hello world")
