import pygame

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()

    def run(self, dt: float):
        self.display_surface.fill("white")
        self.sprites.draw(self.display_surface)
        self.sprites.update()