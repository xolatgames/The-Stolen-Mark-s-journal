from clear import Clear
from map import Map

class Win():
    def __init__(self):
        Clear.__init__(self)

        self.battle = False

        self.stats["gold"] += 10

        Map.__init__(self, self.next_map)