from math import ceil
import random

class Snake:
    # LEFT  = [0, -1]
    # RIGHT = [0, 1]
    # UP    = [-1, 0]
    # DOWN  = [1, 0]
    LEFT = [-1, 0]
    RIGHT = [1, 0]
    UP = [0, -1]
    DOWN = [0, 1]
    obstacles = []



    def __init__(self, height, width):
        # height and width must be divisible by 10
        center = [ceil(height/2), random.randint(1,width-1)]
        # start with length 3
        self.cells = [center, [center[0]+1, center[1]], [center[0]+2, center[1]]]
        self.direction = Snake.RIGHT
        self.last_direction = Snake.RIGHT
        self.height = height
        self.width = width
        self.obstacles = []
        self.speed = 5

    # check whether snake is dead or not
    def is_dead(self,opponent=[]):
        if self.cells[-1] in self.obstacles or self.cells[-1] in self.cells[:-1] or self.cells[-1] in opponent:
            return True
        else:
            return False

    # check if snake will die if moving along the dir, used by AI
    def will_die(self,dir,opponent=[]):
        nextStep = [self.cells[-1][0]+dir[0],self.cells[-1][1]+dir[1]]
        if nextStep in self.obstacles or nextStep in self.cells[:-1] or nextStep in opponent:
            return True
        else:
            return False

    # return 0 if nothing happen
    # return 1 if got food
    # return 2 if got wormhole
    def tick(self, food, wormhole):
        if wormhole == self.cells[-1]: #already in the wormhole
            self.cells.pop(0)
            return 2
        self.cells.append(list(map(lambda x, y: x + y, self.cells[-1], self.direction)))
        self.last_direction = self.direction
        if food == self.cells[-1]:
            return 1  # got food, no need to decrease length
        else:
            self.cells.pop(0)
            return 0

    # turn snake around in specific direction
    def turn(self, direction):
        if direction == list(map(lambda x: -x, self.last_direction)):
            return False # snake wants to fold over
        self.direction = direction
        return True

    # when snake hit the wall, teleport to another side
    def teleport_wall(self):
        if self.cells[-1][0] == 0:
            self.cells[-1] = [self.height-2, self.cells[-1][1]]

        if self.cells[-1][1] == 0:
            self.cells[-1] = [self.cells[-1][0], self.width-2]

        if self.cells[-1][0] == (self.height-1):
            self.cells[-1] = [1, self.cells[-1][1]]

        if self.cells[-1][1] == (self.width-1):
            self.cells[-1] = [self.cells[-1][0], 1]
        return 0


    def add_obstcles(self,level):
        y0 = random.randint(1, self.height - 1)
        x0 = random.randint(1, self.width - 1)

        if level%3 ==0 : # horizontal
            for i in range(y0,min(y0+level,self.height - 1),1):
                self.obstacles.append([x0,i])

        elif level%5 == 0: # T-shape
            for i in range(y0, max(y0-level,0), -1):
                self.obstacles.append([x0, i])
            for i in range(x0, max(x0-level,0), -1):
                self.obstacles.append([i, y0+1])

        else: # horizontal
            for i in range(x0,min(x0+level,self.width-1),1):
                self.obstacles.append([i, y0])


    def get_cells(self):
	    return self.cells
