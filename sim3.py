import threading
import time
import random
import numpy as np
from queue import Queue


cusList = []

simTime = 0
simEnd = 20
cusIndex = 0 

class IceCreamCustomer (threading.Thread):  # User is a Thread

    def __init__(self, name, icecreamBrand, reputation, location):
        threading.Thread.__init__(self)
        self.name = name
        self.icecreamBrand = icecreamBrand
        self.reputation = reputation

        self.location = location
        print('Customer ', self.name, ' created')
        
    def run(self):
        global simTime, simEnd
        
        while simTime < simEnd:
            for customer in cusList:



                if self.reputation > customer.reputation:
                    continue
                else:
                    print('Customer ', self.name, ' changing preference to ', self.icecreamBrand)
                    self.icecreamBrand = customer.icecreamBrand

            time.sleep(1)
        
 
numCustomers = 5
for c in range(numCustomers):

    loc = 

    cusObj = IceCreamCustomer("AJ"+str(cusIndex), random.randint(1, 5), random.randint(1,10))
    cusIndex = cusIndex + 1

    cusList.append(cusObj)
    cusObj.start()


# simulation loop
while simTime < simEnd:

    # increment simulation time
    simTime = simTime + 1
    time.sleep(2)
