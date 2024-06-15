import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = [
   (-1, -1, -1),
   (1, -1, -1),
   (1, 1, -1),
   (-1, 1, -1),
   (-1, -1, 1),
   (1, -1, 1),
   (1, 1, 1),
   (-1, 1, 1)
]
faces = [
   (0, 1, 2),
   (0, 2, 3),
   (5, 4, 7),
   (5, 7, 6),
   (4, 0, 3),
   (4, 3, 7),
   (1, 5, 6),
   (1, 6, 2),
   (4, 5, 1),
   (4, 1, 0),
   (3, 2, 6),
   (3, 6, 7)
]

textureCoordinates = ((0, 0), (0, 1), (1, 1), (1, 0))

colors = [
   (1, 0, 0), #Red
   (1, 0.5, 0), #orange
   (1, 1, 0), #yellow
   (0, 1, 0), #green
   (0, 0, 1), #blue
   (0.5, 0, 1) #violet
]


def draw_cube():
    glBegin(GL_TRIANGLES)
    for faceIndex, face in enumerate(faces):
        #glColor3fv(colors[faceIndex // 10])
        for index in face:
            glTexCoord2fv(textureCoordinates[index])
            glVertex3fv(vertices[index])
    glEnd()

def draw_object():
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glColor4d(216, 174,0,0.29)
    #glColor(1, 1, 0)  # yellow
    glScale(1.60, 1.60, 1.60)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0, 0)
    #glColor(1, 0, 0)  # RED
    glColor4d(216, 174,0,0.29)
    glScale(1.50, 1.50, 1.50)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0, 0)
    #glColor(0, 0, 1)  # BLUE
    glColor4d(216, 174,0,0.29)
    glScale(1.30, 1.30, 1.30)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0, 0)
    #glColor(1, 0.5, 0)  # ORANGE
    glColor4d(216, 174,0,0.29)
    glScale(1.10, 1.10, 1.10)
    draw_cube()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0, 0)
    glColor(0.5, 1.0, 0.5)  #green
    #glColor4d(216, 174,0,0.3)
    glScale(1, 1, 1)
    draw_cube()
    glPopMatrix()


def main():
    pygame.init()
    display = (1500, 1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("04 lab 1")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0, 0, -5)

   #glEnable(GL_DEPTH_TEST)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)
                if event.button == 5:
                    glTranslatef(0, 0, -1.0)


        #glRotatef(1, 1, 1, 0) #side rotate
        glRotatef(1, -1, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glScale(1,1,1);
        #draw_cube()
        draw_object()
        pygame.display.flip()
        pygame.time.wait(1)


main()