import numpy as np
import matplotlib.pyplot as plt

# Função para calcular a translação dos pontos
def translacao(pontos, Tx, Ty):
    pontos_transladados = []
    for ponto in pontos:
        x_u = ponto[0] + Tx
        y_u = ponto[1] + Ty
        pontos_transladados.append((x_u, y_u))
    return pontos_transladados

# Pontos originais
p1 = (0, 0)
p2 = (2, 2)

# Vetor de translação
Tx = 3
Ty = 2

# Calcular a translação dos pontos
pontos_transladados = translacao([p1, p2], Tx, Ty)

# Plotar os pontos originais e os pontos transladados
plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'bo-', label='Pontos originais')
plt.plot([ponto[0] for ponto in pontos_transladados], [ponto[1] for ponto in pontos_transladados], 'ro-', label='Pontos transladados')

# Configurações do gráfico
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Translação de pontos no plano cartesiano')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()
