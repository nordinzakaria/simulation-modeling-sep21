import OpenGL

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w,h= 500,500

def square():
    glBegin(GL_QUADS)
    glVertex2f(0.5, 0.5)
    glVertex2f(-.0.5, 0.5)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glColor3f(1.0, 0.0, 0.0)
    square()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
