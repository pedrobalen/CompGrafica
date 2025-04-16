# Importação das bibliotecas necessárias
import pygame                            
from pygame.locals import *              
from OpenGL.GL import *                  
from OpenGL.GLU import *                 
from PIL import Image                    

# Variáveis globais de posição e rotação da câmera
camera_x, camera_y, camera_z = 0, 0, -10  
rot_x, rot_y = 0, 0                       

# Função que carrega uma imagem e a transforma em textura OpenGL
def load_texture(filename):
    try:
        img = Image.open(filename)                           
        img = img.transpose(Image.FLIP_TOP_BOTTOM)           
        img_data = img.convert("RGBA").tobytes()             
        width, height = img.size                             

        tex_id = glGenTextures(1)                            
        glBindTexture(GL_TEXTURE_2D, tex_id)                 
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)      
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)      
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)  
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)  

        return tex_id
    except:
        print(f"Erro ao carregar textura: {filename}")
        return None

# Função que desenha um cubo com textura aplicada
def draw_textured_cube():
    glBegin(GL_QUADS)

    # FACE TRASEIRA (fundo do cubo)
    glTexCoord2f(0, 0); glVertex3fv(cube_vertices[0])
    glTexCoord2f(1, 0); glVertex3fv(cube_vertices[1])
    glTexCoord2f(1, 1); glVertex3fv(cube_vertices[2])
    glTexCoord2f(0, 1); glVertex3fv(cube_vertices[3])

    # FACE FRONTAL (frente do cubo)
    glTexCoord2f(0, 0); glVertex3fv(cube_vertices[4])
    glTexCoord2f(1, 0); glVertex3fv(cube_vertices[5])
    glTexCoord2f(1, 1); glVertex3fv(cube_vertices[6])
    glTexCoord2f(0, 1); glVertex3fv(cube_vertices[7])

    # FACE INFERIOR (base)
    glTexCoord2f(0, 0); glVertex3fv(cube_vertices[0])
    glTexCoord2f(1, 0); glVertex3fv(cube_vertices[1])
    glTexCoord2f(1, 1); glVertex3fv(cube_vertices[5])
    glTexCoord2f(0, 1); glVertex3fv(cube_vertices[4])

    # FACE SUPERIOR (tampa)
    glTexCoord2f(0, 0); glVertex3fv(cube_vertices[3])
    glTexCoord2f(1, 0); glVertex3fv(cube_vertices[2])
    glTexCoord2f(1, 1); glVertex3fv(cube_vertices[6])
    glTexCoord2f(0, 1); glVertex3fv(cube_vertices[7])

    # FACE DIREITA (lado direito do cubo)
    glTexCoord2f(0, 0); glVertex3fv(cube_vertices[1])
    glTexCoord2f(1, 0); glVertex3fv(cube_vertices[2])
    glTexCoord2f(1, 1); glVertex3fv(cube_vertices[6])
    glTexCoord2f(0, 1); glVertex3fv(cube_vertices[5])

    # FACE ESQUERDA (lado esquerdo do cubo)
    glTexCoord2f(0, 0); glVertex3fv(cube_vertices[0])
    glTexCoord2f(1, 0); glVertex3fv(cube_vertices[3])
    glTexCoord2f(1, 1); glVertex3fv(cube_vertices[7])
    glTexCoord2f(0, 1); glVertex3fv(cube_vertices[4])

    glEnd()

    # Função para desenhar o chão com textura de grama
def draw_ground(tex_id):
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glPushMatrix()
    glTranslatef(0, -2, 0)  # Posiciona o chão em y = -2
    glScalef(10, 0.1, 10)   # Faz um plano grande e achatado

    glBegin(GL_QUADS)

    # Base com coordenadas de textura
    glTexCoord2f(0, 0); glVertex3f(-1, -1, -1)
    glTexCoord2f(5, 0); glVertex3f(1, -1, -1)
    glTexCoord2f(5, 5); glVertex3f(1, -1, 1)
    glTexCoord2f(0, 5); glVertex3f(-1, -1, 1)

    glEnd()
    glPopMatrix()

#funcao para desenhar parede
def draw_brick_wall(tex_id):
    glBindTexture(GL_TEXTURE_2D, tex_id)

    glBegin(GL_QUADS)

    # Desenha uma parede com textura de tijolo
    glTexCoord2f(0, 0); glVertex3f(-5, -2, 5)  # Inferior esquerdo
    glTexCoord2f(5, 0); glVertex3f(5, -2, 5)   # Inferior direito
    glTexCoord2f(5, 5); glVertex3f(5, 5, 5)    # Superior direito
    glTexCoord2f(0, 5); glVertex3f(-5, 5, 5)   # Superior esquerdo

    glEnd()


# Lista de coordenadas 3D dos vértices do cubo
# Cada vértice é representado por uma tupla (x, y, z)
# Observação: o cubo tem 8 vértices no total
cube_vertices = [
    (-1, -1, -1),  # 0
    ( 1, -1, -1),  # 1
    ( 1,  1, -1),  # 2
    (-1,  1, -1),  # 3
    (-1, -1,  1),  # 4
    ( 1, -1,  1),  # 5
    ( 1,  1,  1),  # 6
    (-1,  1,  1)   # 7
]

def init_opengl(display):
    glEnable(GL_DEPTH_TEST)                 
    glEnable(GL_TEXTURE_2D)                 

    # Define iluminação
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (0.0, 0.0, 1.0, 1.0))
    glEnable(GL_LIGHTING)                   
    glEnable(GL_LIGHT0)                     
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 2, -10, 1))          
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1))     
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1))    

    # Define propriedades do material
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
    glMaterialf(GL_FRONT, GL_SHININESS, 80)

    # Define projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    pygame.init()                                          
    display = (800, 600)                                   
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)   

    init_opengl(display)                                   
    tex_id = load_texture("textura.jpg")                   
    wood_tex_id = load_texture("madeira.jpg")  #madeira
    grass_tex_id = load_texture("grama.jpg")  # grama
    brick_tex_id = load_texture("tijolo.jpg")  #tijolo
    metal_tex_id = load_texture("metal.jpg")  #metal

    clock = pygame.time.Clock()                            
    global camera_x, camera_y, camera_z, rot_x, rot_y      

    running = True
    while running:
        clock.tick(60)                                     

        for event in pygame.event.get():                   
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()                    

        # Controles da câmera
        if keys[K_w]: camera_z += 0.1                      
        if keys[K_s]: camera_z -= 0.1                      
        if keys[K_a]: camera_x += 0.1                      
        if keys[K_d]: camera_x -= 0.1                      

        if keys[K_q]: rot_y -= 1                           
        if keys[K_e]: rot_y += 1                           
        if keys[K_r]: rot_x -= 1                           
        if keys[K_f]: rot_x += 1                           

        # Configuração da câmera
        target_x = camera_x        
        target_y = camera_y        
        target_z = camera_z + 1    

        glLoadIdentity()
        gluLookAt(camera_x, camera_y, camera_z,  
                  target_x, target_y, target_z,  
                  0, 1, 0)                       
        
        glRotatef(rot_x, 1, 0, 0)                                
        glRotatef(rot_y, 0, 1, 0)                                

        # Limpa buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # cubo madeira
        glPushMatrix()
        glTranslatef(-3, -1, 0)  # posição base
        glBindTexture(GL_TEXTURE_2D, wood_tex_id)
        draw_textured_cube()
        glPopMatrix()

        # cubo metal
        glPushMatrix()
        glTranslatef(-3, 1, 0)  # 2 unidades acima
        glBindTexture(GL_TEXTURE_2D, metal_tex_id)
        draw_textured_cube()
        glPopMatrix()

        # cubo original
        glPushMatrix()
        glTranslatef(-3, 3, 0)  # mais 2 unidades acima
        glBindTexture(GL_TEXTURE_2D, tex_id)
        draw_textured_cube()
        glPopMatrix()
        
        # Desenha o chão com textura de grama
        draw_ground(grass_tex_id)    
        
        #Desenha parede de tijolo
        draw_brick_wall(brick_tex_id)

   



        pygame.display.flip()

    pygame.quit()

main()