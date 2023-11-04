import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x, y, next_level, health, damage, crushing_armor, stabbing_armor, chopping_armor, previous_map, battle_background):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health
        self.damage = damage
        self.crushing_armor = crushing_armor
        self.stabbing_armor = stabbing_armor
        self.chopping_armor = chopping_armor
        self.next_level = next_level
        self.previous_map = previous_map
        self.battle_background = battle_background