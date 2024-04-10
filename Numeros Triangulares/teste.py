import matplotlib.pyplot as plt
import numpy as np

# def is_triangular(num):
#     if (num < 0):
#             return False

#     sum, n = 0, 1
#     while(sum <= num):
#         sum = sum + n
#         if (sum == num):
#                 return True
#         n += 1
#     return False

def is_triangular(num):
    n = int(np.sqrt(2 * num))
    return n * (n + 1) // 2 == num


def draw_triangular_balls(n):
    num_rows = int(np.ceil((-1 + np.sqrt(1 + 8 * n)) / 2))

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for row in range(num_rows):
        for col in range(row + 1):
            ax.add_patch(plt.Circle((col - row / 2, -row * np.sqrt(3) / 2), 0.3, color='blue'))

    ax.set_xlim(-num_rows / 2 - 1, num_rows / 2 + 1)
    ax.set_ylim(-num_rows * np.sqrt(3) / 2 - 1, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.title('Representação gráfica número triangular')
    plt.show()

# Exemplo de uso:
n = int(input("Digite o valor de n: "))
if (is_triangular(n)):
    draw_triangular_balls(n)

else: 
    print("n não é um número triangular!")