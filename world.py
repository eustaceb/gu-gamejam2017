import pygame
class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = None
        self.x_velocity = 0
        self.y_velocity = 0
    def setSprite(self, sprite):
        self.sprite = sprite
    
    def render(self, screen):
        screen.blit(self.sprite, (self.x, self.y))
    

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

class World:
    def __init__(self, screen):
        self.entities = []
        self.tilemap = {}
        ball_sprite = pygame.image.load("test.gif")
        ball = Entity(400,300)
        ball.setSprite(ball_sprite)
        self.entities.append(ball)
    
    def render(self, screen):
        screen.fill((0,0,0))
        for ent in self.entities:
            ent.render(screen)
        pygame.display.flip()

    def update(self):
        for ent in self.entities:
            ent.update()

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False 
            elif event.key == pygame.K_d:
                self.entities[0].x_velocity = 10/60.0
            elif event.key == pygame.K_a:
                self.entities[0].x_velocity = -10/60.0 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.entities[0].x_velocity = 0
            elif event.key == pygame.K_a:
                self.entities[0].x_velocity = 0
        return True
            
            
