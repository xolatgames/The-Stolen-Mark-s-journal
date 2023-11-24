import pygame

class Objects():
    def __init__(self):
        self.players = []
        self.walls = []
        self.triggers = []
        self.items = []
        self.enemies = []

        self.sprites = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()