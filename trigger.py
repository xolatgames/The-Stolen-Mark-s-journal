import pygame

class Trigger(pygame.sprite.Sprite):
    def __init__(self, x, y, action):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/trigger.png")
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.rect.x = x
        self.rect.y = y
        self.action = action