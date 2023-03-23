world = {
    (2,0) : 'P',
    (0,2) : 'W',
    (1,2) : 'G',
    (2,2) : 'P',
    (3,3) : 'P'
}

class Agent:
    left_turn = {'North' : 'West', 'West' : 'South', 'South' : 'East', 'East' : 'North'}
    right_turn = {'North' : 'East', 'East' : 'South', 'South' : 'West', 'West' : 'North'}
    move_forward = {'North' : (0,1), 'South' : (0,-1), 'East' : (1,0), 'West': (-1,0)}
    dir_moves = {
                    ('North','South') : ('Right','Right'), ('South','North') : ('Right','Right'),
                    ('East','West') : ('Left','Left'), ('West','East') : ('Left','Left'),
                    ('North','East') : ('Right',), ('East','North') : ('Left',),
                    ('North','West') : ('Left',), ('West','North') : ('Right',),
                    ('South','West') : ('Right',), ('West','South') : ('Left',),
                    ('South','East') : ('Left',), ('East','South') : ('Right',),
                    ('North','North') : (), ('South','South') : (),
                    ('East','East') : (), ('West','West') : ()
                }

    def __init__(self,world):
        self.world = world
        self.haveGold = False
        self.know_base = {}
        self.direction = 'East'
        self.arrow = 1
        self.score = 0
        self.position = (0,0)
        self.size = 4
        self.neighbours = set()
        self.alive = True
    
        for i in range(self.size):
            for j in range(self.size):
                self.know_base[(i,j)] = set()

    def print_kb(self):
        print('Knowledge Base : ')
        for i in range(self.size):
            for j in range(self.size):
                print(f'({i},{j}) : {self.know_base[(i,j)]}')
    
    def sense(self):
        wumpus_set = set()
        for i in self.neighbour(self.position):
            if i in self.world:
                if self.world[i] == 'P':
                    self.know_base[self.position].add('B')
                if self.world[i] == 'W':
                    self.know_base[self.position].add('S')
                    wumpus_set.add(i)
        if len(wumpus_set) == 0:
            self.know_base[self.position].discard('S')
        if self.position in self.world:
            if self.world[self.position] == 'G':
                self.haveGold = True
                self.score += 1000
                self.grab()
            if self.world[self.position] == 'W':
                self.score -= 1000
                self.alive = False
                self.dead()
            if self.world[self.position] == 'P':
                self.score -= 1000
                self.alive = False
                self.dead()

    def neighbour(self,position):
        self.neighbours = set()
        if position[0] > 0:
            self.neighbours.add((position[0]-1,position[1]))
        if position[0] < self.size-1:
            self.neighbours.add((position[0]+1,position[1]))
        if position[1] > 0:
            self.neighbours.add((position[0],position[1]-1))
        if position[1] < self.size-1:
            self.neighbours.add((position[0],position[1]+1))
        return self.neighbours
    
    def ok_neighbour(self):
        ok_neighbours = []
        for i in self.neighbours:
            if 'OK' in self.know_base[i] and 'V' not in self.know_base[i]:
                ok_neighbours.append(i)
        for i in self.neighbours:
            if i not in ok_neighbours:
                if 'OK' in self.know_base[i] and 'V' in self.know_base[i]:
                    ok_neighbours.append(i)
        return ok_neighbours
    
    def turn_left(self):
        self.direction = self.left_turn[self.direction]
        self.score -= 1

    def turn_right(self):
        self.direction = self.right_turn[self.direction]
        self.score -= 1

    def move(self):
        new_x = self.position[0]+self.move_forward[self.direction][0]
        new_y = self.position[1]+self.move_forward[self.direction][1]
        print('      New position : ',(new_x,new_y))
        if self.direction == 'North' and self.position[1] == self.size-1:
            print("Out of bounds, Agent can't move forward")
        elif self.direction == 'South' and self.position[1] == 0:
            print("Out of bounds, Agent can't move forward")
        elif self.direction == 'East' and self.position[0] == self.size-1:
            print("Out of bounds, Agent can't move forward")
        elif self.direction == 'West' and self.position[0] == 0:
            print("Out of bounds, Agent can't move forward")
        else :
            self.position = (new_x,new_y)
            self.score -= 1
        
    def grab(self):
        if self.haveGold:
            print('      The agent has gold, Grabbed gold')
            print('      Now we have to move back to the starting position\n')

    def shoot(self):
        return self.arrow
    
    def movable_direction(self,neighbour):
        if neighbour[0] == self.position[0]:
            if neighbour[1] == self.position[1]+1:
                return 'North'
            else :
                return 'South'
        else :
            if neighbour[0] == self.position[0]+1:
                return 'East'
            else :
                return 'West'

    def dead(self):
        if not self.alive:
            print('The agent is dead')
            print('Score : ',self.score)

def analyze_wumpus(agent,neighbours):
    total_NW = 0
    for i in neighbours:
        if 'NW' in agent.know_base[i]:
            total_NW += 1
    if len(neighbours) - total_NW == 1:
        for i in neighbours:
            if 'W?' in agent.know_base[i]:
                agent.know_base[i].add('W')
                agent.know_base[i].remove('W?')
                shot = agent.shoot()
                if shot:
                    print('\n      >--> : The agent shot the wumpus')
                    direction = agent.movable_direction(i)
                    dir_moves = agent.dir_moves[(agent.direction,direction)]
                    agent.arrow = 0
                    agent.score -= 10
                    for i in dir_moves:
                        if i == 'Left':
                            agent.turn_left()
                        else :
                            agent.turn_right()
                    agent.know_base[i].discard('W')
                    agent.know_base[i].add('NW')
                    agent.know_base[i].add('OK')
                    world.pop(i)
                    return True
                else :
                    print('\n      X : No arrow left to shoot the wumpus')
    return False


def analyze_pit(agent,neighbours):
    total_NP = 0
    for i in neighbours:
        if 'NP' in agent.know_base[i]:
            total_NP += 1
    if len(neighbours) - total_NP == 1:
        for i in neighbours:
            if 'P?' in agent.know_base[i]:
                agent.know_base[i].add('P')
                agent.know_base[i].remove('P?')

if __name__ == '__main__':
    agent = Agent(world)
    haveGold = False
    start = (0,0)
    agent.position = start
    agent.know_base[start].add('OK')
    step = 1
    go_back_way = []
    print('Initial Score : ',agent.score)
    while agent.alive:
        if agent.position not in go_back_way:
            go_back_way.insert(0,agent.position)
        print(f'Step-{step} :',)
        agent.sense()
        agent.know_base[agent.position].add('V')
        if agent.haveGold:
            haveGold = True
            break

        neighbours = agent.neighbour(agent.position)
        print('      Cureent Position: ',agent.position)
        print('      Current Configuration',agent.know_base[agent.position])
        print('      Neighbours :', agent.neighbours)
        print('\n      Neigbours Configuration before analysis : ')
        for i in neighbours:
            print('         ',i,agent.know_base[i])

        if 'B' in agent.know_base[agent.position]:
            for i in neighbours:
                if 'OK' not in agent.know_base[i] and 'V' not in agent.know_base[i]:
                    agent.know_base[i].add('P?')
        if 'B' not in agent.know_base[agent.position]:
            for i in neighbours:
                agent.know_base[i].add('NP')
        if 'S' in agent.know_base[agent.position]:
            for i in neighbours:
                if 'OK' not in agent.know_base[i] and 'V' not in agent.know_base[i]:
                    agent.know_base[i].add('W?')
        if 'S' not in agent.know_base[agent.position]:
            for i in neighbours:
                agent.know_base[i].add('NW')
        for i in neighbours:
            if 'NP' in agent.know_base[i] and 'NW' in agent.know_base[i]:
                agent.know_base[i].add('OK')
        for i in neighbours:
            if 'NP' in agent.know_base[i] and 'P?' in agent.know_base[i]:
                agent.know_base[i].remove('P?')
                agent.know_base[i].add('OK')
        for i in neighbours:
            if 'NW' in agent.know_base[i] and 'W?' in agent.know_base[i]:
                agent.know_base[i].remove('W?')
                agent.know_base[i].add('OK')

        analyze_pit(agent,neighbours)
        shot = analyze_wumpus(agent,neighbours)
        if shot:
            print('      Current Score : ',agent.score,'\n')

        print('      Neigbours Configuration after analysis : ')
        for i in neighbours:
            print('         ',i,agent.know_base[i])
        print()
        
        ok_neighbours = agent.ok_neighbour()
        selected_neighbour = ok_neighbours[0]

        print("      OK Neighbours : ", *ok_neighbours)
        print("      Selected 'OK neighbour': ",selected_neighbour,'\n')

        direction = agent.movable_direction(selected_neighbour)
        dir_moves = agent.dir_moves[(agent.direction,direction)]
        if len(dir_moves) == 2:
            go_back_way.pop(0)

        print('      Current Direction :',agent.direction)
        print('      Direction to move :',direction,'\n')
        print('      Moves : ',end = '')
        for j in dir_moves:
            if j == 'Left':
                print('Turn Left -> ',end = '')
            if j == 'Right':
                print('Turn Right -> ',end = '')
        print('Move Forward')

        for i in dir_moves:
            if i == 'Left':
                agent.turn_left()
            else :
                agent.turn_right()
        agent.move()
        print('      Current Score : ',agent.score,'\n')

        print()
        step += 1

    print('      The way to go back is : ', end=' ')
    for i in range(len(go_back_way)-1):
        print(go_back_way[i],end=' -> ')
    print(go_back_way[-1],'\n')
    step += 1
    go_back_way.pop(0)
    if agent.alive:
        for i in go_back_way:
            print(f'Step-{step} :',)
            print('      Cureent Position: ',agent.position)
            direction = agent.movable_direction(i)
            dir_moves = agent.dir_moves[(agent.direction,direction)]
            print('      Current Direction :',agent.direction)
            print('      Direction to move :',direction,'\n')
            print('      Moves : ',end = '')
            for j in dir_moves:
                if j == 'Left':
                    print('Turn Left -> ',end = '')
                if j == 'Right':
                    print('Turn Right -> ',end = '')
            print('Move Forward')

            for i in dir_moves:
                if i == 'Left':
                    agent.turn_left()
                else :
                    agent.turn_right()
            agent.move()
            print()
            step += 1
        print('Exit reached with Total Score : ',agent.score)
    else :
        print('Agent died with Score : ',agent.score)