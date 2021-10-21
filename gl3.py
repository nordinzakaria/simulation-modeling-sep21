import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500

def square():
    for i in range(3):
        glBegin(GL_QUADS)
        glVertex2f(5, 5)
        glVertex2f(250, 5)
        glVertex2f(250, 250)
        glVertex2f(5 , 250)
        glEnd()

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
