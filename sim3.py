import threading
import time
import random
from queue import Queue


simTime = 0
simEnd = 20
cusIndex = 0 

class IceCreamCustomer (threading.Thread):  # User is a Thread

    def __init__(self, name, icecreamBrand, reputation):
        threading.Thread.__init__(self)
        self.name = username
        self.icecreamBrand = icecreamBrand
        print('Customer ', self.name, ' created')
        
    def run(self):
        global simTime, simEnd
        
        while simTime < simEnd:
              time.sleep(1)
        
 
numCustomers = 5
for c in range(numCustomers):
    cusObj = IceCreamCustomer("AJ"+str(cusIndex), random.randint(1, 5), random.randint(1,10))
    cusIndex = cusIndex + 1

    cusObj.start()


# simulation loop
while simTime < simEnd:

    # increment simulation time
    simTime = simTime + 1
    time.sleep(2)
