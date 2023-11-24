import pygame
from giveup import GiveUp
from win import Win

class Battle():
    def __init__(self, battle_background):
        self.screen.blit(pygame.image.load(battle_background), (0, 0))

        self.screen.blit(pygame.image.load("images/player_right.png"), (64, 240))

        self.screen.blit(self.enemy_image, (736 - 96, 240))

        enemy_panel = pygame.Surface((256, 160))
        enemy_panel.fill("White")

        self.screen.blit(enemy_panel, (32, 512-188))

        self.screen.blit(self.font.render("Health: " + str(self.enemy_stats["health"]), True, "Black"), (36, 512-184))
        self.screen.blit(self.font.render("Damage: " + str(self.enemy_stats["damage"]), True, "Black"), (36, 512-184+20))
        self.screen.blit(self.font.render("Against Crushing: " + str(self.enemy_stats["crushing_armor"]), True, "Black"), (36, 512-184+40))
        self.screen.blit(self.font.render("Against Stabbing: " + str(self.enemy_stats["stabbing_armor"]), True, "Black"), (36, 512-184+60))
        self.screen.blit(self.font.render("Against Chopping: " + str(self.enemy_stats["chopping_armor"]), True, "Black"), (36, 512-184+80))

        if self.stats["health"] <= 0:
            GiveUp.__init__(self)
        
        if self.enemy_stats["health"] <= 0:
            Win.__init__(self)