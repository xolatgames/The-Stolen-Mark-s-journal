import pygame

class ShowTheEnemyStats():
    def __init__(self):
        self.enemy_panel = pygame.Surface((256, 160))
        self.enemy_panel.fill("White")

        self.screen.blit(self.enemy_panel, (32, 512-172))

        self.screen.blit(self.font.render("Health: " + str(self.enemy_stats["health"]), True, "Black"), (36, 512-168))
        self.screen.blit(self.font.render("Damage: " + str(self.enemy_stats["damage"]), True, "Black"), (36, 512-168+20))
        self.screen.blit(self.font.render("Against Crushing: " + str(self.enemy_stats["crushing_armor"]), True, "Black"), (36, 512-168+40))
        self.screen.blit(self.font.render("Against Stabbing: " + str(self.enemy_stats["stabbing_armor"]), True, "Black"), (36, 512-168+60))
        self.screen.blit(self.font.render("Against Chopping: " + str(self.enemy_stats["chopping_armor"]), True, "Black"), (36, 512-168+80))