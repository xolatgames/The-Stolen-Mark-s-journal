import pygame
from map import Map
from battle import Battle
from giveup import GiveUp
from showdialog import ShowDialog
from clear import Clear
from objects import Objects
from playerstats import PlayerStats
from battlestats import BattleStats
from showthestats import ShowTheStats

class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.init()
        self.screen = pygame.display.set_mode((736, 512))
        pygame.display.set_caption("The Stolen Mark's journal")

        pygame.mixer.music.load("sounds/music.ogg")
        pygame.mixer.music.play(-1)

        Objects.__init__(self)
        PlayerStats.__init__(self)
        BattleStats.__init__(self)

        self.font = pygame.font.SysFont(None, 24)
        self.dialog = []
        self.hint = "Press Enter, to resume..."

        self.win = False

        self.carpet = False

        Map.__init__(self, "home.txt")

        self.running = True

        while self.running:
            self.screen.fill("Black")

            for p in self.players:
                p.update(self.walls)

                self.trigger = p.collisionTrigger(self.triggers)

                if (self.trigger):
                    match (self.trigger.action):
                        case 1:
                            self.dialog = ShowDialog.returndialog("journal_has_lost.txt")
                            self.triggers.remove(self.trigger)
                            self.backgrounds.remove(self.trigger)
                        case 2:
                            if len(self.triggers) == 1:
                                Map.__init__(self, "world1.txt")
                        case 3:
                            Map.__init__(self, "level1.txt")
                        case 4:
                            self.dialog = ShowDialog.returndialog("Goshas_quest.txt")
                            self.triggers.remove(self.trigger)
                            self.backgrounds.remove(self.trigger)
                        case 5:
                            Map.__init__(self, "world2.txt")
                        case 6:
                            Map.__init__(self, "level3.txt")
                        case 7:
                            self.dialog = ShowDialog.returndialog("Katyas_quest.txt")
                            self.triggers.remove(self.trigger)
                            self.backgrounds.remove(self.trigger)
                        case 8:
                            self.dialog = ShowDialog.returndialog("Katyas_has_finished_quest.txt")
                            self.triggers.remove(self.trigger)
                            self.backgrounds.remove(self.trigger)
                        case 9:
                            if len(self.triggers) == 1:
                                Map.__init__(self, "level5.txt")
                        case 10:
                            self.dialog = ShowDialog.returndialog("equipment1.txt")
                            self.triggers.remove(self.trigger)
                            self.backgrounds.remove(self.trigger)
                        case 11:
                            self.dialog = ShowDialog.returndialog("equipment2.txt")
                            self.triggers.remove(self.trigger)
                            self.backgrounds.remove(self.trigger)
            
            self.item = p.collisionItemStats(self.items, self.stats)
            if self.item:
                self.stats = self.item

            self.item = p.destroyCollisionItem(self.items)
            if self.item:
                self.items.remove(self.item)
                self.sprites.remove(self.item)

            if (p.collisionEnemy(self.enemies, self)):
                Clear.__init__(self)

                self.battle = True

            self.backgrounds.draw(self.screen)

            if self.carpet == True:
                self.screen.blit(pygame.image.load("images/carpet.png"), (256, 256))
            
            self.sprites.draw(self.screen)

            if self.win:
                self.screen.blit(pygame.image.load("images/battle_background1.png"), (0, 0))

                self.hint = "Press Enter, to resume..."

                self.font_the_end = pygame.font.SysFont(None, 48)

                self.screen.blit(self.font_the_end.render("Конец!", True, "Black"), (320, 256))

            if len(self.dialog) > 0:
                self.screen.blit(self.font.render(self.dialog[0], True, "Black"), (34, 34))
                self.screen.blit(self.font.render(self.dialog[0], True, "White"), (32, 32))
            else:
                self.hint = "Press I, to open stats"
            
            if self.battle:
                Battle.__init__(self, self.battle_background)

            if self.show_the_stats:
                ShowTheStats.__init__(self)

            self.screen.blit(self.font.render(self.hint, True, "Black"), (34, 66))
            self.screen.blit(self.font.render(self.hint, True, "Yellow"), (32, 64))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if len(self.dialog) > 0:
                            del self.dialog[0]

                    if event.key == pygame.K_i:
                        self.show_the_stats = not self.show_the_stats

                    if self.battle:
                        match event.key:
                            case pygame.K_ESCAPE:
                                GiveUp.__init__(self)
                            case pygame.K_1:
                                self.enemy_stats["health"] -= self.stats["crushing_damage"] - self.enemy_stats["crushing_armor"]
                                self.stats["health"] -= self.enemy_stats["damage"] - self.stats["armor"]
                            case pygame.K_2:
                                self.enemy_stats["health"] -= self.stats["stabbing_damage"] - self.enemy_stats["stabbing_armor"]
                                self.stats["health"] -= self.enemy_stats["damage"] - self.stats["armor"]
                            case pygame.K_3:
                                self.enemy_stats["health"] -= self.stats["chopping_damage"] - self.enemy_stats["chopping_armor"]
                                self.stats["health"] -= self.enemy_stats["damage"] - self.stats["armor"]
                            case pygame.K_4:
                                if self.stats["mana"] >= 1:
                                    self.enemy_stats["health"] -= self.stats["magic_damage"]
                                    self.stats["health"] -= self.enemy_stats["damage"] - self.stats["armor"]
                                    self.stats["mana"] -= 1

                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            self.clock.tick(30)
