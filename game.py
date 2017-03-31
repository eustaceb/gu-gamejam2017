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
    menu = None
    section = game_world

    clock = pygame.time.Clock()
    time_prev = pygame.time.get_ticks()

    while True:
        if section == game_world:
            if game_world.gameover:
                menu = Menu(screen, game_world.player.score, game_world.won)
                menu.set_background(game_world.get_screen())
                section = menu
                continue

        for event in pygame.event.get():
            running = section.process_event(event)
            if running == -1:
                sys.exit()
            elif running == 1:
                game_world = World(screen, resources)
                section = game_world
                continue

        time_now = pygame.time.get_ticks()
        if (time_now - time_prev) >= 1000/60.0:
            section.update(time_now)
            pygame.display.update((0,0,width,height))
            section.render(screen)
            time_prev = time_now

if __name__ == "__main__":
    main()
