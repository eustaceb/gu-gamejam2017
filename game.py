import pygame
import sys
from world import *


def load_resources(filename):
    resources = {}
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader, None)
        # id,name,filename,type
        for line in reader:
            res_id, name, filename, type = line
            resources[res_id] = Resource(res_id, name, filename, type)
    return resources


def main():
    pygame.init()
    if len(sys.argv) != 3:
        width, height = 800, 600
    else:
        width, height = sys.argv[1], sys.argv[2]

    screen = pygame.display.set_mode((width,height))
    resources = load_resources("resources.csv")
    game_world = World(screen, resources)
    clock = pygame.time.Clock()
    time_prev = pygame.time.get_ticks()
    while True:
        for event in pygame.event.get():
            running = game_world.process_event(event)
            if not running:
                sys.exit()

        time_now = pygame.time.get_ticks()
        if (time_now - time_prev) >= 1000/60.0:
            game_world.update()
            game_world.render(screen)
            time_prev = time_now

    print(width, height)
    print("Hello world")

if __name__ == "__main__":
    main()
