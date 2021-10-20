import threading
import time
import random
from queue import Queue


cusQ = Queue(maxsize = 3)
simTime = 0
simEnd = 20
cusIndex = 0 

class IceCreamServer(threading.Thread):
    def __init__(self, serverID, numIceCream):
        threading.Thread.__init__(self)
        self.serverID = serverID
        self.numIceCream = numIceCream
        self.busy = False
        self.customer = None
        
    def run(self):
        global simTime, simEnd, cusQ

        while simTime < simEnd:
            print('Server ', self.serverID, ' is running')

            time.sleep(1)
            if self.busy == True:
                if self.customer.status != IceCreamCustomer.DONE:
                    print('Server ', self.serverID, ' is busy wih customer ', self.customer.username, ' of status ', self.customer.status)
                else:
                    self.busy = False
                    self.customer = None
                    
            else:
                if cusQ.empty() == False:
                    self.customer = cusQ.get()
                    print('serving customer ', self.customer.username)
                    self.customer.status = IceCreamCustomer.BEING_SERVED
                    self.busy = True
        

class IceCreamCustomer (threading.Thread):  # User is a Thread
    IN_QUEUE = 0
    BEING_SERVED = 1
    DONE = 2

    def __init__(self, username, numIceCream):
        threading.Thread.__init__(self)
        self.username = username
        self.numIceCream = numIceCream
        self.status = IceCreamCustomer.IN_QUEUE
        print('Customer ', self.username, ' created')
        
    def run(self):
        global simTime, simEnd
        
        while self.status != IceCreamCustomer.DONE and simTime < simEnd:
            
            if self.status == IceCreamCustomer.IN_QUEUE:
                time.sleep(1)
                print('Time ', simTime, ': ', self.username, ' still in queue ')
                continue
          
            # this loop only when customer is being served
            if self.status == IceCreamCustomer.BEING_SERVED:
                for i in range(self.numIceCream):
                    time.sleep(1)
                    print('Time ', simTime, ': ', self.username, ' decided on flavor for ice cream ', i)
                    
                self.status = IceCreamCustomer.DONE
        
 
'''
server0 = IceCreamServer(0, 30)
server0.start()

# simulation loop
while simTime < simEnd:

    numCustomers = random.randint(0, 3)
    print('Num of new customer at time ', simTime, ': ', numCustomers)
    for c in range(numCustomers):
        cusObj = IceCreamCustomer("AJ"+str(cusIndex), 3)
        cusIndex = cusIndex + 1
        cusQ.put(cusObj)
        cusObj.start()
        
    # increment simulation time
    simTime = simTime + 1
    time.sleep(2)
    print('Queue size at time ', simTime, ': ', cusQ.qsize())
'''
