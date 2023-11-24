from map import Map

class GiveUp():
    def __init__(self):
        self.stats["health"] = self.previous_health
        
        self.battle = False

        Map.__init__(self, self.previous_map)