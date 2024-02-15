import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# les nodes / sommet / vertex
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# les arretes / edge
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

# fonction permettant de générer le cube


def cube(x =0, y=0, z=0):
    """"
    glBegin(GL_QUADS)

    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()
"""
    vertices = [
        [1, -1, -1],        [1, 1, -1],        [-1, 1, -1],        [-1, -1, -1],
        [1, -1, 1],        [1, 1, 1],        [-1, -1, 1],        [-1, 1, 1]
    ]

    # les arretes / edge
    for e in vertices:
            e[0] += x
            e[1] += y
            e[2] += z
    glBegin(GL_LINES)
    for edge in edges:

        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 100.0)
    # (fov,ratio,distance de disparition proche , distance de disparition loin )
    glTranslatef(0.0, 0.0, -50) # position


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(0.5, 1, 1, 1) # rotation de la vue (angle,x,y,z)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for i in range(-3, 3):
            for j in range(-3, 3):
                for k in range(-3, 3):
                    cube(y=-3*j,z=-3*i,x = -3*k)


        pygame.display.flip()
        pygame.time.wait(10) # temps entre chaque frame (surement en miliseconde)


main()
