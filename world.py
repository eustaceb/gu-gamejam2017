import pygame

from game_objects.Cthulhu import Cthulhu
from game_objects.Entity import *
from game_objects.Player import *
import pygame, csv
from Resource import *
from TileMap import *
from Map import *
from game_objects.House import *
from collections import deque

from game_objects.Sheep import Sheep
from game_objects.Villager import Villager


class World:
    def __init__(self, screen, resources):
        self.font = pygame.font.SysFont("Arial", 25)
        self.tilemaps = {}
        self.gameover = False
        self.entities = []
        self.genentities = Group()
        self.bullets = pygame.sprite.Group()
        self.resources = resources
        #self.tilemap = TileMap("map1.csv", self.resources)
        self.map = Map()
        self.player, self.tilemaps, self.entities = self.map.load_map(filename="map2.txt", resources=self.resources)

        self.generate_entities()

        # Set player and world for turrets; house images for houses
        house_images = [resources["h1"].image, resources["h2"].image, resources["h3"].image,
                        resources["h4"].image, resources["h5"].image]
        for i in range(len(self.entities)):
            if isinstance(self.entities[i], Turret):
                self.entities[i].set_player(self.player)
                self.entities[i].set_world(self)
            elif isinstance(self.entities[i], House):
                self.entities[i].set_images(house_images)

        self.camera = pygame.Rect(0,0, screen.get_width(), screen.get_height())
        self.bg_surface = pygame.Surface(screen.get_size())


    def generate_entities(self):
        citiness = random.randint(40, 150)
        x_positions = range(1,200)
        random.shuffle(x_positions)
        self.houses = Group()
        self.turrets = Group()
        self.NPCs = Group()

        for item in range(0,citiness):
            if random.randint(0,1)==0:
                self.houses.add(House(320+x_positions[item]*64,382,player=self.player))
            else:
                turret = Turret(320+x_positions[item]*64,390,player=self.player)
                turret.set_world(self)
                self.turrets.add(turret)

            self.NPCs.add(Villager(320+x_positions[item]*64,382,player=self.player))

        for item in range(citiness, len(x_positions)):
            if(item%3==0):
                self.NPCs.add(Sheep(320+x_positions[item]*64,382,player=self.player))

        self.NPCs.add(Cthulhu(320+x_positions[len(x_positions)-1]*64,123,player=self.player))
        self.genentities.add(self.houses)
        self.genentities.add(self.turrets)
        self.genentities.add(self.NPCs)

    def render(self, screen):
        screen.fill((0,0,0))
        #print(self.tilemaps.keys())
        if "bg" in self.tilemaps:
            self.tilemaps["bg"].draw(self.bg_surface)
        screen.blit(self.bg_surface, screen.get_rect())
        # Moved from self.map.render
        for k,tilemap in self.tilemaps.iteritems():
            if k=="bg":continue
            tilemap.render(screen, self.camera)

        camera_sprite = Sprite()
        camera_sprite.rect = self.camera

        for ent in pygame.sprite.spritecollide(camera_sprite, self.genentities, False):
            ent.render(screen, self.camera)
        for ent in self.entities:
            ent.render(screen, self.camera)
        for bomb in self.player.bombs:
            bomb.render(screen, self.camera)
        for bul in self.bullets:
            bul.render(screen, self.camera)

        self.player.render(screen, self.camera)

        health_text = self.font.render("Health: " + str(self.player.health), 1, (255, 0, 0))
        score_text = self.font.render("Score: " + str(self.player.score), 1, (255, 0, 0))
        tractor_text = self.font.render("Tractor beam: " + str(self.player.tractor_beam.capacity) + "%", 1, (255, 0, 0))
        screen.blit(health_text, (0, 0))
        screen.blit(score_text, (0, 25))
        screen.blit(tractor_text, (0, 50))

    def update(self, time_now):
        self.player.update(tilemap=self.map.tilemaps.itervalues(), entities=self.entities,
                           bullets=self.bullets, current_tick=time_now)
        if self.player.health < 1:
            self.gameover = True
            return
        camera_sprite = Sprite()
        camera_sprite.rect = Rect(self.camera)
        center = camera_sprite.rect.center
        camera_sprite.rect.inflate_ip(300,0)
        camera_sprite.rect.center = center

        for ent in self.entities:
            ent.update(tilemap=self.map.tilemaps.itervalues(), tick=time_now, entities=self.entities, camera=self.camera, npcs=self.NPCs, houses=self.houses, turrets=self.turrets)

        for ent in pygame.sprite.spritecollide(camera_sprite, self.genentities, False):
            ent.update(tilemap=self.map.tilemaps.itervalues(), bullets=self.bullets, tick=time_now, entities=self.entities, camera=self.camera, world=self)
        for bul in self.bullets:
            bul.update()
        for bomb in self.player.bombs:
            bomb.update(tilemap=self.map.tilemaps.itervalues(), camera=self.camera , entities=self.entities)
        cam_x,cam_y = self.camera.center 
        cam_x = cam_x + (self.player.rect.centerx-cam_x)*0.1
        cam_y = cam_y + (self.player.rect.centery-cam_y)*0.1
        self.camera.center = cam_x, cam_y

        scottys = pygame.sprite.spritecollide(self.player, self.NPCs, False)

        for scotty in scottys:
            if scotty.__class__ != Cthulhu:
                if(self.player.tractor_beam.enabled):
                    self.player.score += 10
                    self.NPCs.remove(scotty)
                    self.genentities.remove(scotty)

        if len(self.bullets) > 0:  # Pop one by one, no need to iterate over the whole list due to freq updates
            frst = self.bullets.sprites()[0]
            if frst.gone(time_now):
                self.bullets.remove(frst)

    def get_screen(self):
        return self.bg_surface

    def process_event(self, event):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or event.type == pygame.QUIT:
            return "quit"
        if self.gameover:
            self.gameover = False
            return "gameover"
        return "ok"

