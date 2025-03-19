import matplotlib.pyplot as plt

def draw_circle(radius):
    # Inicializa as coordenadas iniciais
    x = 0
    y = radius
    p = 1 - radius  # Calcula o parâmetro de decisão inicial
    # Lista para armazenar os pontos do círculo
    points = []
    # Desenha o primeiro ponto
    points.append((x, y))
    # Itera sobre os pontos do círculo
    while x < y:
        x += 1
        # Testa o parâmetro de decisão
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1
        # Adiciona os pontos simétricos às listas
        points.append((x, y))
        points.append((x, -y))
        points.append((-x, y))
        points.append((-x, -y))
        points.append((y, x))
        points.append((y, -x))
        points.append((-y, x))
        points.append((-y, -x))
    return points

# Defina o raio do círculo
radius = 5
# Desenha o círculo
circle_points = draw_circle(radius)
# Extrai as coordenadas x e y dos pontos
x_coords, y_coords = zip(*circle_points)
# Cria o gráfico do círculo
plt.figure()
plt.plot(x_coords, y_coords, 'bo')  # 'bo' para pontos azuis
plt.gca().set_aspect('equal', adjustable='box')  # Define o aspecto igual para evitar a distorção
plt.title("Círculo Gerado pelo Algoritmo do Ponto Médio")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.grid(True)  # Adiciona uma grade ao gráfico
plt.show()