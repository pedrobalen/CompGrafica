import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a escala dos pontos
def escala(pontos, Sx, Sy):
    pontos_escalados = []
    for ponto in pontos:
        x_u = ponto[0] * Sx
        y_u = ponto[1] * Sy
        pontos_escalados.append((x_u, y_u))
    return pontos_escalados

# Pontos originais
p1 = (1, 1)
p2 = (2, 2)
p3 = (3, 3)
# Fatores de escala
Sx = 2
Sy = 2

# Calcular a escala dos pontos
pontos_escalados = escala([p1, p2, p3], Sx, Sy)

# Plotar os pontos originais e os pontos escalados
plt.plot([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], 'bo-', label='Pontos originais')
plt.plot([ponto[0] for ponto in pontos_escalados], 
         [ponto[1] for ponto in pontos_escalados], 'ro-', label='Pontos escalados')

# Configurações do gráfico
plt.xlabel('X')
plt.ylabel('Y') 
plt.title('Escala de pontos no plano cartesiano')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()
