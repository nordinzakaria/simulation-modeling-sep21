import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500


def drawQ():
        # draw a box representing the area of the queue
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(400, 100)
    glVertex2f(400, 200)
    glVertex2f(100, 200)
    glEnd()

        '''
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
        '''

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
    square()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)  # declare showScreen as the function to call whenever the windows needs to be drawn/redrawn
glutIdleFunc(showScreen)  # declare what will be be called continuously, when the system is idle
glutMainLoop()
