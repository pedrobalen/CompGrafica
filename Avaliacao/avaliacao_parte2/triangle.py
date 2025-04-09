from OpenGL.GL import *
class Triangle:
    def __init__(self):
        self.vertices = (
            (0, 1, 0),
            (-1, -1, 0),
            (1, -1, 0)
        )
        
        self.color = (1, 0.5, 0.2)  
        
    def draw(self, x_offset=0, y_offset=0, z_offset=0):
        glPushMatrix()
        glTranslatef(x_offset, y_offset, z_offset)
        
        glBegin(GL_TRIANGLES)
        glColor3fv(self.color)
        for vertex in self.vertices:
            glVertex3fv(vertex)
        glEnd()
        
        glColor3f(0, 0, 0)
        glBegin(GL_LINE_LOOP)
        for vertex in self.vertices:
            glVertex3fv(vertex)
        glEnd()
        
        glPopMatrix()