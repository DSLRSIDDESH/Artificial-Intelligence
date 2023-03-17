class Block():
    def __init__(self, pos):
        self.p = 0
        self.b = 0
        self.w = 0
        self.s = 0
        self.v = 0
        self.g = 0
        self.k = 0
        if pos.lower() == 'wumpus':
            self.w = 1
        elif pos.lower() == 'pit':
            self.p = 1
        elif pos.lower() == 'gold':
            self.g = 1

class World():
    def __init__(self, world):
        self = world
        for i in range(len(self)):
            for j in range(len(self)):
                if self[i][j].p:
                    if i > 0:
                        self[i-1][j].b = 1
                    if j > 0:
                        self[i][j-1].b = 1
                    if i < len(self):
                        self[i+1][j].b = 1
                    if j < len(self):
                        self[i][j+1].b = 1
                if self[i][j].w:
                    if i > 0:
                        self[i-1][j].s = 1
                    if j > 0:
                        self[i][j-1].s = 1
                    if i < len(self):
                        self[i+1][j].s = 1
                    if j < len(self):
                        self[i][j+1].s = 1
    

if __name__ == '__main__':
    world = [
                [Block(''),Block(''),Block(''),Block('Pit')],
                [Block('Wumpus'),Block('Gold'),Block('Pit'),Block('')],
                [Block(''),Block(''),Block(''),Block('')],
                [Block(''),Block(''),Block(''),Block('')]
            ]
    
    wumpus_world = World(world)
    
    