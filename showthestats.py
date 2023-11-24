import pygame

class ShowTheStats():
    def __init__(self):
        self.panel = pygame.Surface((256, 192))
        self.panel.fill("White")
        
        self.screen.blit(self.panel, (736-288, 512-196))

        self.screen.blit(self.font.render("Health: " + str(self.stats["health"]) + "/" + str(self.stats["max_health"]), True, "Black"), (736-284, 512-192))
        self.screen.blit(self.font.render("Mana: " + str(self.stats["mana"]) + "/" + str(self.stats["max_mana"]), True, "Black"), (736-284, 512-192+20))
        self.screen.blit(self.font.render("Intelligent: " + str(self.stats["intelligent"]), True, "Black"), (736-284, 512-192+40))
        self.screen.blit(self.font.render("Gold: " + str(self.stats["gold"]), True, "Black"), (736-284, 512-192+60))
        self.screen.blit(self.font.render("Crushing Damage: " + str(self.stats["crushing_damage"]), True, "Black"), (736-284, 512-192+80))
        self.screen.blit(self.font.render("Stabbing Damage: " + str(self.stats["stabbing_damage"]), True, "Black"), (736-284, 512-192+100))
        self.screen.blit(self.font.render("Chopping Damage: " + str(self.stats["chopping_damage"]), True, "Black"), (736-284, 512-192+120))
        self.screen.blit(self.font.render("Magic Damage: " + str(self.stats["magic_damage"]), True, "Black"), (736-284, 512-192+140))
        self.screen.blit(self.font.render("Armor: " + str(self.stats["armor"]), True, "Black"), (736-284, 512-192+160))