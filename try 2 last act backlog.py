import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

verticies = [
    (1, 1, 1),  # top right outer       0
    (1, -1, 1),  # bottom right outer    1
    (-1, 1, 1),  # top left outer        2
    (-1, -1, 1),  # bottom left outer    3
]

edges = [
    (0, 1, 3, 2)
]

tex_coords = (
    (0, 1), (0, 0), (1, 0), (1, 1)
)


def Cube_test():
    glBegin(GL_QUADS)
    for edge in edges:
        for i, vertex in enumerate(edge):
            glTexCoord2fv(tex_coords[i])
            glVertex3fv(verticies[vertex])
    glEnd()


def add_texture_based(texture_data, width, height):
    texID = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)

    return texID


def draw_object(texture_based1, texture_based2):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBindTexture(GL_TEXTURE_2D, texture_based1)
    glPushMatrix()
    Cube_test()
    glPopMatrix()

    # 2nd face (rotated 90 degrees around y-axis)
    glBindTexture(GL_TEXTURE_2D, texture_based1)
    glPushMatrix()
    glRotatef(90, 0, 1, 0)
    Cube_test()
    glPopMatrix()

    # 3rd face (rotated -90 degrees around x-axis)
    glBindTexture(GL_TEXTURE_2D, texture_based2)
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)
    Cube_test()
    glPopMatrix()

    # 4th face (rotated 180 degrees around y-axis)
    glBindTexture(GL_TEXTURE_2D, texture_based1)
    glPushMatrix()
    glRotatef(180, 0, 1, 0)
    Cube_test()
    glPopMatrix()

    # 5th face (rotated -90 degrees around y-axis)
    glBindTexture(GL_TEXTURE_2D, texture_based2)
    glPushMatrix()
    glRotatef(-90, 0, 1, 0)
    Cube_test()
    glPopMatrix()

    # 6th face (rotated 90 degrees around x-axis)
    glBindTexture(GL_TEXTURE_2D, texture_based1)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    Cube_test()
    glPopMatrix()

    #Another Cube
    #-------------------------------------#
    glBindTexture(GL_TEXTURE_2D, texture_based1)
    glPushMatrix()
    glTranslatef(2, 2, 2)
    Cube_test()
    glPopMatrix()

    # 2nd face (rotated 90 degrees around y-axis)
    glBindTexture(GL_TEXTURE_2D, texture_based1)
    glPushMatrix()
    glTranslatef(2, 2, 2)
    glRotatef(90, 0, 1, 0)
    Cube_test()
    glPopMatrix()

    # 3rd face (rotated -90 degrees around x-axis)
    glBindTexture(GL_TEXTURE_2D, texture_based2)
    glPushMatrix()
    glTranslatef(2, 2, 2)
    glRotatef(-90, 1, 0, 0)
    Cube_test()
    glPopMatrix()

    # 4th face (rotated 180 degrees around y-axis)
    glBindTexture(GL_TEXTURE_2D, texture_based1)
    glPushMatrix()
    glTranslatef(2, 2, 2)
    glRotatef(180, 0, 1, 0)
    Cube_test()
    glPopMatrix()

    # 5th face (rotated -90 degrees around y-axis)
    glBindTexture(GL_TEXTURE_2D, texture_based2)
    glPushMatrix()
    glTranslatef(2, 2, 2)
    glRotatef(-90, 0, 1, 0)
    Cube_test()
    glPopMatrix()

    # 6th face (rotated 90 degrees around x-axis)
    glBindTexture(GL_TEXTURE_2D, texture_based1)
    glPushMatrix()
    glTranslatef(2, 2, 2)
    glRotatef(90, 1, 0, 0)
    Cube_test()
    glPopMatrix()


def main():
    pygame.init
    display = (1000, 700)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Animation Python")

    # Set up animation parameters
    start_time = pygame.time.get_ticks()
    animation_duration = 20000  # 20 seconds

    # Load textures
    texture_surface1 = pygame.image.load('cube1.jpg')
    texture_data1 = pygame.image.tostring(texture_surface1, 'RGBA', 1)
    width1, height1 = texture_surface1.get_size()

    texture_surface2 = pygame.image.load('cube2.jpg')
    texture_data2 = pygame.image.tostring(texture_surface2, 'RGBA', 1)
    width2, height2 = texture_surface2.get_size()

    texture_id1 = add_texture_based(texture_data1, width1, height1)
    texture_id2 = add_texture_based(texture_data2, width2, height2)

    glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))  # point light from the left, top, front
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)
                if event.button == 5:
                    glTranslatef(0, 0, -1.0)

        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time

        if elapsed_time <= 2000:
            draw_object(texture_id1, texture_id1)
        elif elapsed_time <= 4000:
            draw_object(texture_id2, texture_id2)
        elif elapsed_time <= 5000:
            draw_object(texture_id1, texture_id1)
        elif elapsed_time <= 8000:
            draw_object(texture_id2, texture_id2)
        elif elapsed_time <= 10000:
            draw_object(texture_id1, texture_id1)
        elif elapsed_time <= 15000:
            draw_object(texture_id2, texture_id2)
        elif elapsed_time <= 20000:
            draw_object(texture_id1, texture_id1)
        else:
            pygame.quit()
            quit()

        """       
        elif elapsed_time >= animation_duration:
           pygame.quit()
           quit()
        """

        glRotatef(1, 2, 3, 1)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        pygame.display.flip()
        pygame.time.wait(10)


main()
