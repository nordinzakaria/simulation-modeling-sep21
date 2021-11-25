import threading
import time
import random
from queue import Queue
import pandas as pd
import numpy as np

simTime = 0
simEnd =20 

class Grid:
    def __init__(self, dim):
        self.width = dim
        self.height = dim

        self.arr = [[None for i in range(dim)] for j in range(dim)]
        self.locks = [[None for i in range(dim)] for j in range(dim)]
        
        for j in range(dim):
            for i in range(dim):
                self.locks[j][i] = threading.Lock()

    def add(self, entity, x, y):
        self.arr[y][x] = entity
        
    def get(self, x, y):
        return self.arr[y][x]
        
    def remove(self, x, y):
        self.arr[y][x] = None

    def print(self):
        for j in range(dim):
            for i in range(dim):
                ag = self.get(i,j)
                if ag == None:
                    print('Grid (',i,',',j,') has nobody')
                else:
                    print('Grid (',i,',',j,') has ', ag.name, ' of type ', ag.identity)


class Entity(threading.Thread):
    Name = 0

    def __init__(self, grid, x, y, identity, tolerance):
        threading.Thread.__init__(self)

            # agent's position
        self.x = x
        self.y = y        

        self.name = Entity.Name
        Entity.Name += 1

            # the grid (the "world") where the agent belongs to
        self.grid = grid 
        
        self.identity = identity
        self.tolerance = tolerance


    def run(self):
        while simTime < simEnd:
            time.sleep(1)

            # assume 0 neighbors of different type            
            num_diffneigh = 0

            # look around the neighborhood
            # count number of diff neighbors
            for i in range(3):
                for j in range(3):
                    nx = self.x + i - 1
                    ny = self.y + j - 1

                    if nx < 0 or ny < 0:
                        continue
                    if nx >= self.grid.width or ny >= self.grid.height:
                        continue
                    if nx == self.x and ny == self.y:
                        continue

                    agent = self.grid.get(i,j)
                    if agent != None:
                        if agent.identity != self.identity:
                            num_diffneigh += 1


            # if too many different neighbors
            if num_diffneigh > self.tolerance:

                found = False
                while True: # look for a new position
                    x = random.randint(0, self.grid.width-1)
                    y = random.randint(0, self.grid.height-1)

                    print('Agent ', self.name, ' looking at position (', x, ',', y, ')')

                    # make sure that no one is looking at the same position
                    self.grid.locks[y][x].acquire()                    
                    if self.grid.get(x, y) == None:
                        self.grid.remove(self.x, self.y)
                        self.x = x
                        self.y = y
                        self.grid.add(self, x, y)
                        found = True
                    self.grid.locks[y][x].release()                         

                    if found == True:
                        break
            else: 
                pass

#the main simulation loop                
theworld = Grid(20) 
numentity = 200

# add agents
for i in range(numentity):

    while True:    
        x = random.randint(0, theworld.width-1)
        y = random.randint(0, theworld.height-1)
        if theworld.get(x,y) == None:
            break

    identity = random.randint(0, 1)
    tolerance = random.randint(0,2)
    
    agent = Entity(theworld, x, y, identity, tolerance)
    print('Adding agent ', agent.name, ' to location (',x,',', y, ')')
    theworld.add(agent, x, y)
    agent.start()

    
# simulation loop
while simTime < simEnd:
    print('Time: ', simTime)       
    # increment simulation time
    simTime = simTime + 1
    time.sleep(1)


