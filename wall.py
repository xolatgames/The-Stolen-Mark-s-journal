import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, picture, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y