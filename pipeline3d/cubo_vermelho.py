import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

P1 = (-0.5, -0.5, -0.5)
P2 = (-0.5, -0.5, 0.5)
P3 = (-0.5, 0.5, -0.5)
P4 = (-0.5, 0.5, 0.5)
P5 = (0.5, -0.5, -0.5)
P6 = (0.5, -0.5, 0.5)
P7 = (0.5, 0.5, -0.5)
P8 = (0.5, 0.5, 0.5)

arestas_originais = [
    (P1, P2), (P2, P4), (P4, P3), (P3, P1),
    (P5, P6), (P6, P8), (P8, P7), (P7, P5),
    (P1, P5), (P2, P6), (P3, P7), (P4, P8)
]

P1_novo = tuple(2 * coord for coord in P1)
P2_novo = tuple(2 * coord for coord in P2)
P3_novo = tuple(2 * coord for coord in P3)
P4_novo = tuple(2 * coord for coord in P4)
P5_novo = tuple(2 * coord for coord in P5)
P6_novo = tuple(2 * coord for coord in P6)
P7_novo = tuple(2 * coord for coord in P7)
P8_novo = tuple(2 * coord for coord in P8)

arestas_maior = [
    (P1_novo, P2_novo), (P2_novo, P4_novo), (P4_novo, P3_novo), (P3_novo, P1_novo),
    (P5_novo, P6_novo), (P6_novo, P8_novo), (P8_novo, P7_novo), (P7_novo, P5_novo),
    (P1_novo, P5_novo), (P2_novo, P6_novo), (P3_novo, P7_novo), (P4_novo, P8_novo)
]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for aresta in arestas_originais:
    ponto1 = aresta[0]
    ponto2 = aresta[1]
    ax.plot([ponto1[0], ponto2[0]], [ponto1[1], ponto2[1]], [ponto1[2], ponto2[2]], 'b')

for aresta in arestas_maior:
    ponto1 = aresta[0]
    ponto2 = aresta[1]
    ax.plot([ponto1[0], ponto2[0]], [ponto1[1], ponto2[1]], [ponto1[2], ponto2[2]], 'r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Cubos no Espaço 3D')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

plt.show()
