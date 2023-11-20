import pygame
from clear import Clear

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player_down.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hspeed = 0
        self.vspeed = 0
        self.speed = 4
    
    def update(self, walls):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.image = pygame.image.load("images/player_left.png")
            self.hspeed = -self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.image = pygame.image.load("images/player_right.png")
            self.hspeed = self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.image = pygame.image.load("images/player_up.png")
            self.vspeed = -self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.image = pygame.image.load("images/player_down.png")
            self.vspeed = self.speed
        
        self.rect.x += self.hspeed

        self.collisionWalls(self.hspeed, 0, walls)

        self.hspeed = 0

        self.rect.y += self.vspeed

        self.collisionWalls(0, self.vspeed, walls)

        self.vspeed = 0

    def collisionWalls(self, hspeed , vspeed, walls):
        for i in walls:
            if pygame.sprite.collide_rect(self, i):
                if hspeed < 0:
                    self.rect.left = i.rect.right
                if hspeed > 0:
                    self.rect.right = i.rect.left
                if vspeed < 0:
                    self.rect.top = i.rect.bottom
                if vspeed > 0:
                    self.rect.bottom = i.rect.top
    
    def collisionTrigger(self, triggers):
        for i in triggers:
            if pygame.sprite.collide_rect(self, i):
                return i
                    
    
    def collisionItemStats(self, items, stats):
        self.stats = stats

        for i in items:
            if pygame.sprite.collide_rect(self, i):
                if i.price <= self.stats["gold"]:
                    self.stats["health"] += i.health
                    self.stats["max_health"] += i.max_health

                    if self.stats["health"] > self.stats["max_health"]:
                        self.stats["health"] = self.stats["max_health"]

                    self.stats["mana"] += i.mana
                    self.stats["max_mana"] += i.max_mana

                    if self.stats["mana"] > self.stats["max_mana"]:
                        self.stats["mana"] = self.stats["max_mana"]

                    self.stats["intelligent"] += i.intelligent
                    self.stats["crushing_damage"] += i.crushing_damage
                    self.stats["stabbing_damage"] += i.stabbing_damage
                    self.stats["chopping_damage"] += i.chopping_damage
                    self.stats["magic_damage"] += i.magic_damage
                    self.stats["armor"] += i.armor
                    self.stats["gold"] -= i.price

                    return self.stats
    

    def destroyCollisionItem(self, items):
        for i in items:
            if pygame.sprite.collide_rect(self, i):
                if i.price <= self.stats["gold"]:
                    return i

    
    def collisionEnemy(self, enemies, main):
        for i in enemies:
            if pygame.sprite.collide_rect(self, i):
                main.enemy_stats["health"] = i.health
                main.enemy_stats["damage"] = i.damage
                main.enemy_stats["crushing_armor"] = i.crushing_armor
                main.enemy_stats["stabbing_armor"] = i.stabbing_armor
                main.enemy_stats["chopping_armor"] = i.chopping_armor

                main.previous_map = i.previous_map
                main.previous_health = main.stats["health"]
                main.battle_background = i.battle_background
                main.next_map = i.next_level
                main.enemy_image = i.image

                return True