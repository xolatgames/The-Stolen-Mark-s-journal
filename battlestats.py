class BattleStats():
    def __init__(self):
        self.battle = False

        self.enemy_stats = {
            "health":5,
            "damage":2,
            "crushing_armor":0,
            "stabbing_armor":0,
            "chopping_armor":0
        }

        self.previous_map = ""
        self.next_map = ""
        self.enemy_image = ""
        self.previous_health = 0
        self.battle_background = ""