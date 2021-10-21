import threading
import time
import random
from queue import Queue

import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500


cusQ = Queue(maxsize = 3)
simTime = 0
simEnd = 20
simDelay = 3
delay = 0
cusIndex = 0


#from sim2 import IceCreamServer, IceCreamCustomer
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


def drawQ():

    # a single rectangle for the queue area
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(400, 100)
    glVertex2f(400, 200)
    glVertex2f(100, 200)
    glEnd()

    obj = list(cusQ.queue)
    glBegin(GL_QUADS)
    w = 0
    for cus in obj:
        glColor3f(cus.numIceCream / 5.0,0,0)
        glVertex2f(110 + w, 120)
        glVertex2f(160 + w, 120)
        glVertex2f(160 + w, 180)
        glVertex2f(110 + w, 180)
        w = w + 60
    glEnd()


def square():

    offset = 0
    for i in range(3):
        glBegin(GL_QUADS)
        glVertex2f(50 + offset, 5)
        glVertex2f(150 + offset, 5)
        glVertex2f(150 + offset, 250)
        glVertex2f(50 + offset, 250)
        glEnd()
        offset = offset + 110

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
           # left    # right   # bottom    # top    # front   # back
    glOrtho(0.0,     500,      0.0,        500,     0.0,      1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1.0, 0.0, 0.0)
    drawQ()
    glutSwapBuffers()


def simLoop():
    global simTime, simEnd, cusQ, cusIndex

    if simTime > simEnd:
        print('simTime: ', simTime, ', simEnd: ', simEnd)
        return

    numCustomers = random.randint(0, 3)
    print('Num of new customer at time ', simTime, ': ', numCustomers)
    for c in range(numCustomers):
        cusObj = IceCreamCustomer("AJ"+str(cusIndex), random.randint(0, 5))
        cusIndex = cusIndex + 1
        cusQ.put(cusObj)
        cusObj.start()
        
    # increment simulation time
    simTime = simTime + 1
    print('Queue size at time ', simTime, ': ', cusQ.qsize())

    glutPostRedisplay()
    time.sleep(1)




server0 = IceCreamServer(0, 30)
server0.start()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)  # declare showScreen as the function to call whenever the windows needs to be drawn/redrawn
glutIdleFunc(simLoop)  # declare what will be be called continuously, when the system is idle
glutMainLoop()
