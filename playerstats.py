class PlayerStats():
    def __init__(self):
        self.stats = {
            "health":10,
            "max_health":10,
            "mana":0,
            "max_mana":0,
            "intelligent":1,
            "gold":10,
            "crushing_damage":0,
            "stabbing_damage":0,
            "chopping_damage":0,
            "magic_damage":0,
            "armor":0
        }

        self.show_the_stats = False