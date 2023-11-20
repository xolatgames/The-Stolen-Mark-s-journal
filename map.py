import pygame
from enemy import Enemy
from floor import Floor
from item import Item
from player import Player
from trigger import Trigger
from wall import Wall
from showdialog import ShowDialog

class Map():        
    def __init__(self, level_name):
        self.level = []

        self.background = []

        x = y = 0

        self.file = open("levels/" + level_name, "r")
        self.map = self.file.readlines()

        self.file = open("backgrounds/" + level_name, "r")
        self.back = self.file.readlines()

        if level_name == "final.txt":
            pygame.mixer.music.load("sounds/final.ogg")
            pygame.mixer.music.play(-1)

        self.dialog = ShowDialog.returndialog(level_name)

        for line in self.back:
            self.background.append(line[:-1])

        for line in self.map:
            self.level.append(line[:-1])
        
        self.players = []
        self.walls = []
        self.triggers = []
        self.items = []
        self.enemies = []

        self.sprites = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()

        self.carpet = False

        if level_name == "home.txt":
            self.carpet = True
        
        if level_name == "final.txt":
            self.win = True

        for row in self.background:
            for i in row:
                match i:
                    case "F":
                        floor = Floor("images/floor.png", x, y)
                        self.backgrounds.add(floor)
                    case "G":
                        grass = Floor("images/grass.png", x, y)
                        self.backgrounds.add(grass)
                    case "S":
                        snow = Floor("images/snow.png", x, y)
                        self.backgrounds.add(snow)
                    case "W":
                        snow = Floor("images/water.png", x, y)
                        self.backgrounds.add(snow)
                x += 32
            x = 0
            y += 32

        x = y = 0
        
        for row in self.level:
            for i in row:
                match i:
                    case "P":
                        self.playeri = Player(x, y)
                        self.players.append(self.playeri)
                        self.sprites.add(self.playeri)
                    case "W":
                        self.wall = Wall("images/wall.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "T":
                        self.wall = Wall("images/tree.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "A":
                        self.wall = Wall("images/snow_tree.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "B":
                        self.wall = Wall("images/bed.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "Q":
                        self.wall = Wall("images/bedside_table.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "E":
                        self.wall = Wall("images/table.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "Y":
                        self.wall = Wall("images/wall_with_the_window.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "F":
                        self.wall = Wall("images/fridge.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "K":
                        self.wall = Wall("images/kitchen_stove.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "S":
                        self.wall = Wall("images/sink.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "D":
                        self.wall = Wall("images/door.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "U":
                        self.wall = Wall("images/bookshelf.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "V":
                        self.wall = Wall("images/village.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "G":
                        self.wall = Wall("images/Gosha.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "!":
                        self.item = Item("images/heal_potion.png", x, y, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case "Z":
                        self.item = Item("images/mana_potion.png", x, y, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case "X":
                        self.item = Item("images/book.png", x, y, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 2)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case "C":
                        self.item = Item("images/glove.png", x, y, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case ">":
                        self.item = Item("images/dart.png", x, y, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case "N":
                        self.item = Item("images/small_axe.png", x, y, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case "M":
                        self.item = Item("images/leather_armor.png", x, y, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 3)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case "H":
                        self.enemy = Enemy("images/goblin.png", x, y, "level2.txt", 5, 2, 0, 0, 0, "level1-1.txt", "images/battle_background1.png")
                        self.enemies.append(self.enemy)
                        self.sprites.add(self.enemy)
                    case "O":
                        self.wall = Wall("images/Katya.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "J":
                        self.wall = Wall("images/cat.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case "L":
                        self.enemy = Enemy("images/shaman.png", x, y, "level4.txt", 10, 5, 2, 0, 2, "level3.txt", "images/battle_background2.png")
                        self.enemies.append(self.enemy)
                        self.sprites.add(self.enemy)
                    case "{":
                        self.item = Item("images/bat.png", x, y, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 3)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case "}":
                        self.item = Item("images/blade.png", x, y, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 3)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case ":":
                        self.item = Item("images/axe.png", x, y, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case "'":
                        self.item = Item("images/chainmail.png", x, y, 0, 4, 0, 0, 0, 0, 0, 0, 2, 0, 4)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case "|":
                        self.item = Item("images/scroll.png", x, y, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 4)
                        self.items.append(self.item)
                        self.sprites.add(self.item)
                    case "?":
                        self.wall = Wall("images/book.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case ",":
                        self.wall = Wall("images/apple_tree.png", x, y)
                        self.walls.append(self.wall)
                        self.sprites.add(self.wall)
                    case ";":
                        self.enemy = Enemy("images/snake.png", x, y, "final.txt", 10, 5, 3, 3, 0, "level5.txt", "images/battle_background3.png")
                        self.enemies.append(self.enemy)
                        self.sprites.add(self.enemy)
                    case "1":
                        self.trigger = Trigger(x, y, 1)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                    case "2":
                        self.trigger = Trigger(x, y, 2)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                    case "3":
                        self.trigger = Trigger(x, y, 3)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                    case "4":
                        self.trigger = Trigger(x, y, 4)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                    case "5":
                        self.trigger = Trigger(x, y, 5)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                    case "6":
                        self.trigger = Trigger(x, y, 6)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                    case "7":
                        self.trigger = Trigger(x, y, 7)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                    case "8":
                        self.trigger = Trigger(x, y, 8)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                    case "9":
                        self.trigger = Trigger(x, y, 9)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                    case "-":
                        self.trigger = Trigger(x, y, 10)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                    case "+":
                        self.trigger = Trigger(x, y, 11)
                        self.triggers.append(self.trigger)
                        self.backgrounds.add(self.trigger)
                x += 32
            x = 0
            y += 32
        