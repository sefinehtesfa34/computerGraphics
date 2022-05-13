import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np
import numpy as np

def rotationMatrix(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian), -np.sin(radian)],
        [np.sin(radian), np.cos(radian)],
    ])

    return mat



def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-10.0, 10.0, -5.0, 5.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_STRIP)
    # X-AXIS (from (-100, 0) to (100, 0))
    glColor3f(1.0,1.0,1.0)
    glVertex2f(-100.0, 0.0)
    glVertex2f(100.0, 0.0)
    glEnd()
    # Y-AXIS (from (0, 100) to (0, -100))
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(0.0, 100.0)
    glVertex2f(0.0, -100.0)
    glEnd()
    
    p0 = np.array([0.6, 0.4])
    v1 = np.array([-1.2, 0])
    t = 1
    mat=rotationMatrix(30)
    v1f = (p0 + v1*0)
    v2f = (p0 + v1*t)
    v3f = (-1 * v2f)
    v4f = (-1*v1f)
    
    v1f=np.dot(v1f,mat)
    v2f=np.dot(v2f,mat)
    v3f=np.dot(v3f,mat)
    v4f=np.dot(v4f,mat)

    glColor3f(1.0, 0.0, 0.0)
    
    glBegin(GL_LINE_LOOP)
    glVertex2f(v1f[0], v1f[1])
    glVertex2f(v2f[0], v2f[1])
    glVertex2f(v4f[0], v4f[1])
    glVertex2f(v3f[0], v3f[1])

    glEnd()
    glFlush()

def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        draw()
        
        pygame.display.flip()
        pygame.time.wait(10)
        


main()