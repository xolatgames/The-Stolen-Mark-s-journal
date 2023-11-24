import pygame
from giveup import GiveUp
from win import Win
from showtheenemystats import ShowTheEnemyStats

class Battle():
    def __init__(self, battle_background):
        self.hint = "Press: 1 - Crushing, 2 - Stabbing, 3 - Chopping, 4 - Magic. Esc - Leave the Battle"

        self.screen.blit(pygame.image.load(battle_background), (0, 0))

        self.screen.blit(pygame.image.load("images/player_right.png"), (64, 240))

        self.screen.blit(self.enemy_image, (736 - 96, 240))

        self.show_the_stats = True

        ShowTheEnemyStats.__init__(self)

        if self.stats["health"] <= 0:
            GiveUp.__init__(self)
        
        if self.enemy_stats["health"] <= 0:
            Win.__init__(self)