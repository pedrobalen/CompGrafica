from OpenGL.GL import *

class Pyramid:
    def __init__(self):
        self.vertices = (
            (0, 1, 0),    
            (1, -1, 1),   
            (-1, -1, 1),  
            (-1, -1, -1),  
            (1, -1, -1)    
        )
        
        self.faces = (
            (0, 1, 2),   
            (0, 2, 3),   
            (0, 3, 4),   
            (0, 4, 1),   
            (1, 2, 3, 4) 
        )
        
        self.colors = (
            (1, 0, 0),
            (0, 1, 0),
            (0, 0, 1),
            (1, 1, 0),
            (1, 0, 1)
        )
    
    def draw(self, x_offset=0, y_offset=0, z_offset=0):
        glPushMatrix()
        glTranslatef(x_offset, y_offset, z_offset)
        
        glBegin(GL_TRIANGLES)
        for i, face in enumerate(self.faces[:4]):  
            glColor3fv(self.colors[i])
            for vertex in face:
                glVertex3fv(self.vertices[vertex])
        glEnd()
        
        
        glBegin(GL_QUADS)
        glColor3fv(self.colors[4])
        for vertex in self.faces[4]:
            glVertex3fv(self.vertices[vertex])
        glEnd()
        
        
        glColor3f(0, 0, 0)
        glBegin(GL_LINES)
        
        for i in range(1, 5):
            glVertex3fv(self.vertices[i])
            if i < 4:
                glVertex3fv(self.vertices[i+1])
            else:
                glVertex3fv(self.vertices[1])  
        
        
        for i in range(1, 5):
            glVertex3fv(self.vertices[0])
            glVertex3fv(self.vertices[i])
        glEnd()
        
        glPopMatrix()