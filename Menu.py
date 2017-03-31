import pygame


class Menu:
    def __init__(self, screen, score, won):
        self.restart = False
        self.font_size = 64
        self.char_w = 36
        self.font = pygame.font.SysFont("Lucida Console", self.font_size)
        self.background = None
        self.draw_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)

        if won:
            self.gover_str = "YOU WIN!!!"
        else:
            self.gover_str = "GAME OVER"
        self.score_str = "SCORE: " + str(score)
        self.restart_str = "RESTART (r)"
        self.quit_str = "QUIT (q)"

        center = (screen.get_width() / 2, screen.get_height() / 2)
        self.gover_text = self.font.render(self.gover_str, 1, (255, 255, 50))
        self.gover_pos = (center[0] - (self.char_w * len(self.gover_str))/2, center[1] - 4*self.font_size)
        self.score_text = self.font.render(self.score_str, 1, (255, 255, 50))
        self.score_pos = (center[0] - (self.char_w * len(self.score_str))/2, center[1] - 3*self.font_size)
        self.restart_text = self.font.render(self.restart_str, 1, (50, 255, 50))
        self.restart_pos = (center[0] - (self.char_w * len(self.restart_str))/2, center[1] - self.font_size)
        self.quit_text = self.font.render(self.quit_str, 1, (255, 50, 50))
        self.quit_pos = (center[0] - (self.char_w * len(self.quit_str))/2, center[1] + self.font_size)

        self.restart_rect = pygame.Rect(self.restart_pos, (len(self.restart_str) * self.char_w, self.font_size))
        self.quit_rect = pygame.Rect(self.quit_pos, (len(self.quit_str) * self.char_w, self.font_size))

        self.restart_light = False
        self.quit_light = False

    def render(self, screen):
        self.draw_surface.blit(self.background, (0, 0))
        self.draw_surface.fill((0, 0, 0, 1))
        screen.blit(self.draw_surface, (0, 0))
        screen.blit(self.gover_text, self.gover_pos)
        screen.blit(self.score_text, self.score_pos)
        screen.blit(self.restart_text, self.restart_pos)
        screen.blit(self.quit_text, self.quit_pos)

    def update(self, time_now):
        if self.restart_rect.collidepoint(pygame.mouse.get_pos()):
            if not self.restart_light:
                self.restart_text = self.font.render(self.restart_str, 1, (150, 255, 150))
                self.restart_light = True
        else:
            if self.restart_light:
                self.restart_text = self.font.render(self.restart_str, 1, (50, 255, 50))
                self.restart_light = False
        if self.quit_rect.collidepoint(pygame.mouse.get_pos()):
            if not self.quit_light:
                self.quit_text = self.font.render(self.quit_str, 1, (255, 150, 150))
                self.quit_light = True
        else:
            if self.quit_light:
                self.quit_text = self.font.render(self.quit_str, 1, (255, 50, 50))
                self.quit_light = False

    def set_background(self, bg):
        self.background = bg

    def process_event(self, event):
        # Key events
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or event.type == pygame.QUIT:
            return -1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            return 1
        # Mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.restart_rect.collidepoint(event.pos[0], event.pos[1]):
                return 1
            if self.quit_rect.collidepoint(event.pos[0], event.pos[1]):
                return -1
        return 0

