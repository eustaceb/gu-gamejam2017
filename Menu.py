import pygame


class Menu:
    def __init__(self, screen):
        self.restart = False
        self.font_size = 64
        self.char_w = 36
        self.font = pygame.font.SysFont("Lucida Console", self.font_size)

        gover_str = "GAME OVER"
        restart_str = "RESTART"
        quit_str = "QUIT"

        center = (screen.get_width() / 2, screen.get_height() / 2)
        self.gover_text = self.font.render(gover_str, 1, (255, 255, 50))
        self.gover_pos = (center[0] - (self.char_w * len(gover_str))/2, center[1] - 3*self.font_size)
        self.restart_text = self.font.render(restart_str, 1, (50, 255, 50))
        self.restart_pos = (center[0] - (self.char_w * len(restart_str))/2, center[1] - self.font_size)
        self.quit_text = self.font.render(quit_str, 1, (255, 50, 50))
        self.quit_pos = (center[0] - (self.char_w * len(quit_str))/2, center[1] + self.font_size)

        self.restart_rect = pygame.Rect(self.restart_pos, (len(restart_str) * self.char_w, self.font_size))
        self.quit_rect = pygame.Rect(self.quit_pos, (len(quit_str) * self.char_w, self.font_size))

    def render(self, screen):
        screen.fill((0,0,0))
        screen.blit(self.gover_text, self.gover_pos)
        screen.blit(self.restart_text, self.restart_pos)
        screen.blit(self.quit_text, self.quit_pos)

    def update(self, time_now):
        pass

    def process_event(self, event):
        # Key events
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or event.type == pygame.QUIT:
            return "quit"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            return "restart"
        # Mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.restart_rect.collidepoint(event.pos[0], event.pos[1]):
                return "restart"
            if self.quit_rect.collidepoint(event.pos[0], event.pos[1]):
                return "quit"

        return "ok"

