import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definindo os pontos originais do cubo
P1 = (-0.5, -0.5, -0.5)
P2 = (-0.5, -0.5, 0.5)
P3 = (-0.5, 0.5, -0.5)
P4 = (-0.5, 0.5, 0.5)
P5 = (0.5, -0.5, -0.5)
P6 = (0.5, -0.5, 0.5)
P7 = (0.5, 0.5, -0.5)
P8 = (0.5, 0.5, 0.5)

# Definindo as arestas do cubo original
arestas_originais = [
    (P1, P2), (P2, P4), (P4, P3), (P3, P1),
    (P5, P6), (P6, P8), (P8, P7), (P7, P5),
    (P1, P5), (P2, P6), (P3, P7), (P4, P8)
]

# Multiplicando as coordenadas dos pontos por 2 para gerar o cubo maior
P1_novo = tuple(2 * coord for coord in P1)
P2_novo = tuple(2 * coord for coord in P2)
P3_novo = tuple(2 * coord for coord in P3)
P4_novo = tuple(2 * coord for coord in P4)
P5_novo = tuple(2 * coord for coord in P5)
P6_novo = tuple(2 * coord for coord in P6)
P7_novo = tuple(2 * coord for coord in P7)
P8_novo = tuple(2 * coord for coord in P8)

# Definindo as arestas do cubo maior
arestas_maior = [
    (P1_novo, P2_novo), (P2_novo, P4_novo), (P4_novo, P3_novo), (P3_novo, P1_novo),
    (P5_novo, P6_novo), (P6_novo, P8_novo), (P8_novo, P7_novo), (P7_novo, P5_novo),
    (P1_novo, P5_novo), (P2_novo, P6_novo), (P3_novo, P7_novo), (P4_novo, P8_novo)
]

# Plotando os cubos
fig = plt.figure()  # Criando uma figura
ax = fig.add_subplot(projection='3d')  # Adicionando um subplot tridimensional à figura

# Plotando as arestas do cubo original em azul
for aresta in arestas_originais:
    ponto1 = aresta[0]  # Obtendo as coordenadas do primeiro ponto da aresta (x,y,z)
    ponto2 = aresta[1]  # Obtendo as coordenadas do segundo ponto da aresta (x,y,z)
    # Plotando uma linha entre os dois pontos para representar a aresta
    ax.plot([ponto1[0], ponto2[0]], [ponto1[1], ponto2[1]], [ponto1[2], ponto2[2]], 'b')

# Plotando as arestas do cubo maior em vermelho
for aresta in arestas_maior:
    ponto1 = aresta[0]  # Obtendo as coordenadas do primeiro ponto da aresta (x,y,z)
    ponto2 = aresta[1]  # Obtendo as coordenadas do segundo ponto da aresta (x,y,z)
    # Plotando uma linha entre os dois pontos para representar a aresta
    ax.plot([ponto1[0], ponto2[0]], [ponto1[1], ponto2[1]], [ponto1[2], ponto2[2]], 'r')

# Configurações do gráfico 3D
ax.set_xlabel('X')  # Configurando o rótulo do eixo x
ax.set_ylabel('Y')  # Configurando o rótulo do eixo y
ax.set_zlabel('Z')  # Configurando o rótulo do eixo z
ax.set_title('Cubos no Espaço 3D')  # Configurando o título do gráfico
ax.set_xlim(-1.5, 1.5)  # Limites do eixo X
ax.set_ylim(-1.5, 1.5)  # Limites do eixo Y
ax.set_zlim(-1.5, 1.5)  # Limites do eixo Z

# Mostrando o gráfico
plt.show()