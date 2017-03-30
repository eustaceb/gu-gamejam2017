import pygame
import sys
import os

from world import *


def load_resources(filename):
    resources = {}
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader, None)
        # id,name,filename,type
        for line in reader:
            res_id, name, filename, res_type = line
            res_id = res_id.strip()
            resources[res_id] = Resource(res_id, name.strip(), filename.strip(), res_type.strip())
    return resources

#
# def load_entity_resources():
#     return {"p" : Resource("p", "player", "assets/ufo.png", "entity")}
#
#
# def load_all_image_resources_as_tiles():
#     resources = {}
#     files = ["./assets/" + f for f in os.listdir("./assets") if f.endswith(".png") or f.endswith(".jpg") or f.endswith("gif") ]
#     print(files)
#     for i,v in enumerate(files):
#         resources[str(i)] = Resource(str(i), v.lstrip("./assets")[:v.index(".")],v,"tile")
#     return resources

def main():
    pygame.init()
    if len(sys.argv) != 3:
        width, height = 800, 600
    else:
        width, height = sys.argv[1], sys.argv[2]

    screen = pygame.display.set_mode((width,height))
    resources = load_resources("resources.csv")
    #resources.update(load_entity_resources())
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
            game_world.update(time_now)
            pygame.display.update((0,0,width,height))
            game_world.render(screen)
            time_prev = time_now

if __name__ == "__main__":
    main()
