import sys
from world import *
from Menu import *


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


def main():
    pygame.init()
    if len(sys.argv) != 3:
        width, height = 800, 600
    else:
        width, height = sys.argv[1], sys.argv[2]

    screen = pygame.display.set_mode((int(width),int(height)),  )
    resources = load_resources("resources.csv")
    game_world = World(screen, resources)
    menu = Menu(screen) # TODO
    clock = pygame.time.Clock()
    time_prev = pygame.time.get_ticks()
    in_menu = False
    while True:
        if in_menu:
            section = menu
        else:
            section = game_world
        for event in pygame.event.get():
            running = section.process_event(event)
            if running == "quit":
                sys.exit()
            elif running == "gameover":
                in_menu = True
            elif running == "restart":
                in_menu = False
                game_world = World(screen, resources)
                continue

        time_now = pygame.time.get_ticks()
        if (time_now - time_prev) >= 1000/60.0:
            section.update(time_now)
            pygame.display.update((0,0,width,height))
            section.render(screen)
            time_prev = time_now

if __name__ == "__main__":
    main()
