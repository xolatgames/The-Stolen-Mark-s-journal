import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, image, x, y, health, max_health, mana, max_mana, intelligent, crushing_damage, stabbing_damage, chopping_damage, armor, magic_damage, price):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health
        self.max_health = max_health
        self.mana = mana
        self.max_mana = max_mana
        self.intelligent = intelligent
        self.crushing_damage = crushing_damage
        self.stabbing_damage = stabbing_damage
        self.chopping_damage = chopping_damage
        self.armor = armor
        self.magic_damage = magic_damage
        self.price = price