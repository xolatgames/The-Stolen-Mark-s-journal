import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((736, 512))
pygame.display.set_caption("The Stolen Mark's journal")

pygame.mixer.music.load("sounds/music.ogg")
pygame.mixer.music.play(-1)

players = []
walls = []
triggers = []
items = []
enemies = []

stats = {
    "health":10,
    "max_health":10,
    "mana":0,
    "max_mana":0,
    "intelligent":1,
    "gold":10,
    "crushing_damage":0,
    "stabbing_damage":0,
    "chopping_damage":0,
    "armor":0
}

show_the_stats = False

carpet = []

font = pygame.font.SysFont(None, 24)
dialog = []
hint = "Нажмите Enter, чтобы продолжить..."

battle = []

enemy_stats = {
    "health":5,
    "damage":2,
    "crushing_armor":0,
    "stabbing_armor":0,
    "chopping_armor":0
}

previous_map = []
previous_health = []
battle_background = []

win = []

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
    
    def update(self):
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

        self.collisionWalls(self.hspeed, 0)

        self.hspeed = 0

        self.rect.y += self.vspeed

        self.collisionWalls(0, self.vspeed)

        self.vspeed = 0

        self.collisionTrigger()

        self.collisionItem()

        self.collisionEnemy()

    def collisionWalls(self, hspeed , vspeed):
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
    
    def collisionTrigger(self):
        for i in triggers:
            if pygame.sprite.collide_rect(self, i):
                match i.action:
                    case 1:
                        ShowDialog("journal_has_lost.txt")
                        triggers.remove(i)
                        backgrounds.remove(i)
                    case 2:
                        if len(triggers) == 1:
                            Clear()

                            carpet.clear()

                            Map("world1.txt")
                    case 3:
                        Clear()

                        Map("level1.txt")
                    case 4:
                        ShowDialog("Goshas_quest.txt")
                        triggers.remove(i)
                        backgrounds.remove(i)
    
    def collisionItem(self):
        for i in items:
            if pygame.sprite.collide_rect(self, i):
                if i.price <= stats["gold"]:
                    stats["health"] += i.health
                    stats["max_health"] += i.max_health
                    stats["mana"] += i.mana
                    stats["max_mana"] += i.max_mana
                    stats["intelligent"] += i.intelligent
                    stats["crushing_damage"] += i.crushing_damage
                    stats["stabbing_damage"] += i.stabbing_damage
                    stats["chopping_damage"] += i.chopping_damage
                    stats["armor"] += i.armor
                    stats["gold"] -= i.price
                    items.remove(i)
                    sprites.remove(i)
    
    def collisionEnemy(self):
        for i in enemies:
            if pygame.sprite.collide_rect(self, i):
                Clear()

                enemy_stats["health"] = i.health
                enemy_stats["damage"] = i.damage
                enemy_stats["crushing_armor"] = i.crushing_armor
                enemy_stats["stabbing_armor"] = i.stabbing_armor
                enemy_stats["chopping_armor"] = i.chopping_armor

                previous_map.clear()
                previous_map.append(i.previous_map)

                battle_background.clear()
                battle_background.append(i.battle_background)

                battle.append(True)

class Wall(pygame.sprite.Sprite):
    def __init__(self, picture, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Trigger(pygame.sprite.Sprite):
    def __init__(self, x, y, action):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/trigger.png")
        self.rect = pygame.Rect(0, 0, 32, 32)
        self.rect.x = x
        self.rect.y = y
        self.action = action

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/floor.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/grass.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Snow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/snow.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Item(pygame.sprite.Sprite):
    def __init__(self, image, x, y, health, max_health, mana, max_mana, intelligent, crushing_damage, stabbing_damage, chopping_damage, armor, price):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health
        self.max_health = max_health

        if stats["health"] > stats["max_health"]:
            stats["health"] = stats["max_health"]

        self.mana = mana
        self.max_mana = max_mana

        if stats["mana"] > stats["max_mana"]:
            stats["mana"] = stats["max_mana"]

        self.intelligent = intelligent
        self.crushing_damage = crushing_damage
        self.stabbing_damage = stabbing_damage
        self.chopping_damage = chopping_damage
        self.armor = armor
        self.price = price

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

        previous_health.clear()
        previous_health.append(stats["health"])

def Map(level_name):
    level = []

    background = []

    x = y = 0

    file = open("levels/" + level_name, "r")
    map = file.readlines()

    file = open("backgrounds/" + level_name, "r")
    back = file.readlines()

    if level_name == "home.txt":
        carpet.append(True)

    ShowDialog(level_name)

    for line in back:
        background.append(line[:-1])

    for line in map:
        level.append(line[:-1])
    
    for row in background:
        for i in row:
            if i == "F":
                floor = Floor(x, y)
                backgrounds.add(floor)
            if i == "G":
                grass = Grass(x, y)
                backgrounds.add(grass)
            if i == "S":
                snow = Snow(x, y)
                backgrounds.add(snow)
            x += 32
        x = 0
        y += 32

    x = y = 0
    
    for row in level:
        for i in row:
            if i == "P":
                player = Player(x, y)
                players.append(player)
                sprites.add(player)
            elif i == "W":
                wall = Wall("images/wall.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "T":
                wall = Wall("images/tree.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "A":
                wall = Wall("images/snow_tree.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "B":
                wall = Wall("images/bed.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "Q":
                wall = Wall("images/bedside_table.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "E":
                wall = Wall("images/table.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "Y":
                wall = Wall("images/wall_with_the_window.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "F":
                wall = Wall("images/fridge.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "K":
                wall = Wall("images/kitchen_stove.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "S":
                wall = Wall("images/sink.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "D":
                wall = Wall("images/door.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "U":
                wall = Wall("images/bookshelf.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "V":
                wall = Wall("images/village.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "G":
                wall = Wall("images/Gosha.png", x, y)
                walls.append(wall)
                sprites.add(wall)
            elif i == "Z":
                item = Item("images/mana_potion.png", x, y, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1)
                items.append(item)
                sprites.add(item)
            elif i == "X":
                item = Item("images/book.png", x, y, 0, 0, 0, 3, 1, 0, 0, 0, 0, 2)
                items.append(item)
                sprites.add(item)
            elif i == "C":
                item = Item("images/glove.png", x, y, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2)
                items.append(item)
                sprites.add(item)
            elif i == ">":
                item = Item("images/dart.png", x, y, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2)
                items.append(item)
                sprites.add(item)
            elif i == "N":
                item = Item("images/small_axe.png", x, y, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2)
                items.append(item)
                sprites.add(item)
            elif i == "M":
                item = Item("images/leather_armor.png", x, y, 0, 2, 0, 0, 0, 0, 0, 0, 1, 3)
                items.append(item)
                sprites.add(item)
            elif i == "H":
                enemy = Enemy("images/goblin.png", x, y, "battle1.txt", 5, 2, 0, 0, 0, "level1-1.txt", "images/battle_background1.png")
                enemies.append(enemy)
                sprites.add(enemy)
            elif i == "1":
                trigger = Trigger(x, y, 1)
                triggers.append(trigger)
                backgrounds.add(trigger)
            elif i == "2":
                trigger = Trigger(x, y, 2)
                triggers.append(trigger)
                backgrounds.add(trigger)
            elif i == "3":
                trigger = Trigger(x, y, 3)
                triggers.append(trigger)
                backgrounds.add(trigger)
            elif i == "4":
                trigger = Trigger(x, y, 4)
                triggers.append(trigger)
                backgrounds.add(trigger)
            x += 32
        x = 0
        y += 32

def ShowDialog(dial):
    file = open("dialogs/" + dial, "r")
    text = file.readlines()

    for line in text:
        dialog.append(line[:-1])

def Clear():
    players.clear()
    walls.clear()
    triggers.clear()
    items.clear()
    enemies.clear()
    sprites.empty()
    backgrounds.empty()

def Battle():
    screen.blit(pygame.image.load(battle_background[0]), (0, 0))

    screen.blit(pygame.image.load("images/player_right.png"), (64, 240))

    screen.blit(pygame.image.load("images/goblin.png"), (736 - 96, 240))

    enemy_panel = pygame.Surface((256, 160))
    enemy_panel.fill("White")

    screen.blit(enemy_panel, (32, 512-188))

    screen.blit(font.render("Здоровье: " + str(enemy_stats["health"]), True, "Black"), (36, 512-184))
    screen.blit(font.render("Урон: " + str(enemy_stats["damage"]), True, "Black"), (36, 512-184+20))
    screen.blit(font.render("Защита от дробящего: " + str(enemy_stats["crushing_armor"]), True, "Black"), (36, 512-184+40))
    screen.blit(font.render("Защита от колющего: " + str(enemy_stats["stabbing_armor"]), True, "Black"), (36, 512-184+60))
    screen.blit(font.render("Защита от режущего: " + str(enemy_stats["chopping_armor"]), True, "Black"), (36, 512-184+80))

    if stats["health"] <= 0:
        GiveUp()
    
    if enemy_stats["health"] <= 0:
        Win()

def GiveUp():
    stats["health"] = previous_health[0]

    Clear()

    Map(previous_map[0])

    battle.clear()

def Win():
    win.clear()
    win.append(True)

    battle.clear()

    Clear()

sprites = pygame.sprite.Group()

backgrounds = pygame.sprite.Group()

Map("level1.txt")

running = True
while running:
    screen.fill("Black")

    for p in players:
        p.update()

    backgrounds.draw(screen)

    if carpet == [True]:
        screen.blit(pygame.image.load("images/carpet.png"), (256, 256))
    
    sprites.draw(screen)

    if len(dialog) > 0:
        screen.blit(font.render(dialog[0], True, "Black"), (34, 34))
        screen.blit(font.render(dialog[0], True, "White"), (32, 32))
    else:
        hint = "Нажмите I, чтобы открыть характеристики"
    
    panel = pygame.Surface((256, 160))
    panel.fill("White")

    if len(battle) > 0:
        hint = "Используйте клавиши: 1 - дробящий, 2 - колющий, 3 - режущий. Esc - сбежать"

        Battle()
    
    if len(win) > 0:
        screen.blit(pygame.image.load("images/battle_background1.png"), (0, 0))

        hint = "Вы прошли ДЕМО!"

    if show_the_stats:
        screen.blit(panel, (736-288, 512-196))

        screen.blit(font.render("Здоровье: " + str(stats["health"]) + "/" + str(stats["max_health"]), True, "Black"), (736-284, 512-192))
        screen.blit(font.render("Мана: " + str(stats["mana"]) + "/" + str(stats["max_mana"]), True, "Black"), (736-284, 512-192+20))
        screen.blit(font.render("Интеллект: " + str(stats["intelligent"]), True, "Black"), (736-284, 512-192+40))
        screen.blit(font.render("Золото: " + str(stats["gold"]), True, "Black"), (736-284, 512-192+60))
        screen.blit(font.render("Дробящий урон: " + str(stats["crushing_damage"]), True, "Black"), (736-284, 512-192+80))
        screen.blit(font.render("Колющий урон: " + str(stats["stabbing_damage"]), True, "Black"), (736-284, 512-192+100))
        screen.blit(font.render("Рубящий урон: " + str(stats["chopping_damage"]), True, "Black"), (736-284, 512-192+120))
        screen.blit(font.render("Броня: " + str(stats["armor"]), True, "Black"), (736-284, 512-192+140))

    screen.blit(font.render(hint, True, "Black"), (34, 66))
    screen.blit(font.render(hint, True, "Yellow"), (32, 64))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(dialog) > 0:
                    del dialog[0]
            if event.key == pygame.K_i:
                show_the_stats = not show_the_stats
            if len(battle) > 0:
                if event.key == pygame.K_ESCAPE:
                    GiveUp()
                elif event.key == pygame.K_1:
                    enemy_stats["health"] -= stats["crushing_damage"] - enemy_stats["crushing_armor"]
                    stats["health"] -= enemy_stats["damage"] - stats["armor"]
                elif event.key == pygame.K_2:
                    enemy_stats["health"] -= stats["stabbing_damage"] - enemy_stats["stabbing_armor"]
                    stats["health"] -= enemy_stats["damage"] - stats["armor"]
                elif event.key == pygame.K_3:
                    enemy_stats["health"] -= stats["chopping_damage"] - enemy_stats["chopping_armor"]
                    stats["health"] -= enemy_stats["damage"] - stats["armor"]
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(30)
