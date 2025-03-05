import numpy as np
import matplotlib.pyplot as plt

#
def rotacao(pontos, angulo):
    pontos_rotacionados = []
    angulo_rad = np.radians(angulo) 
    cos_theta = np.cos(angulo_rad)
    sin_theta = np.sin(angulo_rad)
    
    for ponto in pontos:
        x_r = ponto[0] * cos_theta - ponto[1] * sin_theta
        y_r = ponto[0] * sin_theta + ponto[1] * cos_theta
        pontos_rotacionados.append((x_r, y_r))
    
    return pontos_rotacionados

# Pontos originais
p1 = (2, 2)
p2 = (4, 4)
angulo = 45

pontos_rotacionados = rotacao([p1, p2], angulo)

plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'bo-', label='Pontos originais')
plt.plot([ponto[0] for ponto in pontos_rotacionados], 
         [ponto[1] for ponto in pontos_rotacionados], 'ro-', label='Pontos rotacionados')

# Configurações do gráfico
plt.xlabel('X')
plt.ylabel('Y') 
plt.title('Rotação de pontos no plano cartesiano')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()
