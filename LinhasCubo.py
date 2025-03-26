import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) 
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, 800.0 / 600.0, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_square_lines():
    glLoadIdentity()
    glTranslatef(pos_x, pos_y, zoom)
    glRotatef(rotation_x, 1.0, 0.0, 0.0)
    glRotatef(rotation_y, 0.0, 1.0, 0.0)
    glRotatef(theta, 0.0, 0.0, 1.0)
    
    glColor3f(0.0, 0.0, 1.0) 
    glBegin(GL_LINE_LOOP)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    init()

    global pos_x, pos_y, zoom, rotation_x, rotation_y, theta
    pos_x = 0.0
    pos_y = 0.0
    zoom = -6.0
    rotation_x = 0.0
    rotation_y = 0.0
    theta = 0.0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_w:  
                    pos_y += 0.1
                elif event.key == K_s:  
                    pos_y -= 0.1
                elif event.key == K_a: 
                    pos_x -= 0.1
                elif event.key == K_d: 
                    pos_x += 0.1
                elif event.key == K_z:
                    zoom += 0.5
                elif event.key == K_x: 
                    zoom -= 0.5
                elif event.key == K_r: 
                    rotation_x += 5.0
                elif event.key == K_f: 
                    rotation_x -= 5.0
                elif event.key == K_q: 
                    rotation_y -= 5.0
                elif event.key == K_e:
                    rotation_y += 5.0

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_square_lines()
        pygame.display.flip()
        pygame.time.wait(10)
        
        theta += 1  

    pygame.quit() 

if __name__ == "__main__":
    main()