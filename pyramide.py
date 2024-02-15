import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# les nodes / sommet / vertex
vertices = (
    (-1,0,-1),
    (1,0,-1),
    (1,0,1),
    (-1,0,1),
    (0,2,0),
    (0,-2,0)
)

# les arretes / edge
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,4),
    (4,1),
    (4,3),
    (5,0),
    (5,1),
    (5,2),
    (5,3)
)
# fonction permettant de générer le cube


def pyramide():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 1, 1, 1) # rotation de la vue (angle,x,y,z)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        pyramide()
        pygame.display.flip()
        pygame.time.wait(10) # temps entre chaque frame (surement en miliseconde)


main()
