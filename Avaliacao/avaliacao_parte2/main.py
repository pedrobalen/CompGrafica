import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import math

from cube import Cube
from triangle import Triangle
from pyramid import Pyramid

position = [0, 0, -5]
rotation = [0, 0, 0]
zoom = -5

cube_position = [0, 0, 0]
triangle_position = [0, 0, 0]
pyramid_position = [0, 0, 0]

def handle_keys(option, keys, move_speed=0.1, rot_speed=2, zoom_speed=0.5):
    global position, rotation, zoom
    global cube_position, triangle_position, pyramid_position
    
    if option in [1, 2, 3, 4, 5]:
        if keys[pygame.K_w]:
            position[1] += move_speed
        if keys[pygame.K_s]:
            position[1] -= move_speed
        if keys[pygame.K_a]:
            position[0] -= move_speed
        if keys[pygame.K_d]:
            position[0] += move_speed
        
        if keys[pygame.K_q]:
            rotation[0] += rot_speed
        if keys[pygame.K_e]:
            rotation[0] -= rot_speed
        if keys[pygame.K_r]:
            rotation[1] += rot_speed
        if keys[pygame.K_f]:
            rotation[1] -= rot_speed
        
        if keys[pygame.K_z]:
            zoom += zoom_speed
        if keys[pygame.K_x]:
            zoom -= zoom_speed
    
    elif option == 6:
        if keys[pygame.K_i]:
            cube_position[1] += move_speed
        if keys[pygame.K_k]:
            cube_position[1] -= move_speed
        if keys[pygame.K_j]:
            cube_position[0] -= move_speed
        if keys[pygame.K_l]:
            cube_position[0] += move_speed
        
       
        if keys[pygame.K_g]:
            triangle_position[1] += move_speed
        if keys[pygame.K_b]:
            triangle_position[1] -= move_speed
        if keys[pygame.K_v]:
            triangle_position[0] -= move_speed
        if keys[pygame.K_n]:
            triangle_position[0] += move_speed
        
        
        if keys[pygame.K_UP]:
            pyramid_position[1] += move_speed
        if keys[pygame.K_DOWN]:
            pyramid_position[1] -= move_speed
        if keys[pygame.K_LEFT]:
            pyramid_position[0] -= move_speed
        if keys[pygame.K_RIGHT]:
            pyramid_position[0] += move_speed
        
        
        if keys[pygame.K_z]:
            zoom += zoom_speed
        if keys[pygame.K_x]:
            zoom -= zoom_speed
        if keys[pygame.K_q]:
            rotation[0] += rot_speed
        if keys[pygame.K_e]:
            rotation[0] -= rot_speed
        if keys[pygame.K_r]:
            rotation[1] += rot_speed
        if keys[pygame.K_f]:
            rotation[1] -= rot_speed

def setup_viewport(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, zoom)

def render_scene(option):
    cube = Cube()
    triangle = Triangle()
    pyramid = Pyramid()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, zoom)
    glTranslatef(position[0], position[1], position[2])
    glRotatef(rotation[0], 1, 0, 0)
    glRotatef(rotation[1], 0, 1, 0)
    
    #cubo
    if option == 1:
        cube.draw()
    
    #triangulo
    elif option == 2:
        triangle.draw()
    
    #cubo + triangulo
    elif option == 3:
        cube.draw(-1.5, 0, 0)
        triangle.draw(1.5, 0, 0)
    
    #piramide
    elif option == 4:
        pyramid.draw()
    
    #cubo + triagulo + piramide
    elif option == 5:
        cube.draw(-2.5, 0, 0)
        triangle.draw(0, 0, 0)
        pyramid.draw(2.5, 0, 0)
    
    #controle individual
    elif option == 6:
        glPushMatrix()
        #rotacao global
        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)

        #cubo
        glPushMatrix()
        glTranslatef(-2.5 + cube_position[0], cube_position[1], cube_position[2])
        cube.draw()
        glPopMatrix()
        
        #triangulo
        glPushMatrix()
        glTranslatef(triangle_position[0], triangle_position[1], triangle_position[2])
        triangle.draw()
        glPopMatrix()
        
        #piramide
        glPushMatrix()
        glTranslatef(2.5 + pyramid_position[0], pyramid_position[1], pyramid_position[2])
        pyramid.draw()
        glPopMatrix()
        
        glPopMatrix()

def reset_variables():
    global position, rotation, zoom
    global cube_position, triangle_position, pyramid_position
    
    position = [0, 0, -5]
    rotation = [0, 0, 0]
    zoom = -5
    
    cube_position = [0, 0, 0]
    triangle_position = [0, 0, 0]
    pyramid_position = [0, 0, 0]

def show_menu():
    while True:
        print("\n===== Menu de Opções =====")
        print("1 - Cubo")
        print("2 - Triângulo")
        print("3 - Cubo + Triângulo")
        print("4 - Pirâmide")
        print("5 - Cubo + Triângulo + Pirâmide")
        print("6 - Controle individual")
        print("0 - Sair")
        print("========================")
        
        try:
            option = int(input("Escolha uma opção: "))
            if option == 0:
                sys.exit()
            elif option in [1, 2, 3, 4, 5, 6]:
                print_controls(option)
                return option
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

def print_controls(option):
    print("\n===== Controles =====")
    
    if option in [1, 2, 3, 4, 5]:
        print("Movimentação:")
        print("W, S → cima / baixo")
        print("A, D → esquerda / direita")
        print("Rotação:")
        print("Q, E → rotacionar eixo X")
        print("R, F → rotacionar eixo Y")
        print("Zoom:")
        print("Z, X → zoom in / out")
    
    elif option == 6:
        print("Controles individuais:")
        print("Cubo:")
        print("I, K → cima / baixo")
        print("J, L → esquerda / direita")
        print("Triângulo:")
        print("G, B → cima / baixo")
        print("V, N → esquerda / direita")
        print("Pirâmide:")
        print("↑, ↓ → cima / baixo")
        print("←, → → esquerda / direita")
        print("Controles globais:")
        print("Z, X → zoom in / out")
        print("Q, E → rotacionar eixo X")
        print("R, F → rotacionar eixo Y")
    
    print("ESC → voltar ao menu")
    print("=====================")
    input("Pressione Enter para continuar...")

def run_opengl_window(option):
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Avaliação 2")
    setup_viewport(display[0], display[1])
    glEnable(GL_DEPTH_TEST)
    
    reset_variables()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return None 
        
        keys = pygame.key.get_pressed()
        handle_keys(option, keys)
        render_scene(option)
        pygame.display.flip()
        pygame.time.wait(10)

def main():
    pygame.init()
    pygame.quit()  
    while True:
        option = show_menu() 
        if option == 0:
            sys.exit()
        
        run_opengl_window(option)

if __name__ == "__main__":
    main()