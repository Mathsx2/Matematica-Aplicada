import math


class Objeto:

  def __init__(self, x, y):
    self.x = x  # posição x do objeto
    self.y = y

  def rotacao(self, ponto_rotacao, angulo_graus):
    # converte o angulo de graus para radianos
    angulo_radianos = math.radians(angulo_graus)

    # deslocamento em relação ao ponto de rotação
    delta_x = self.x - ponto_rotacao[0]
    delta_y = self.y - ponto_rotacao[1]

    # aplica a formula de rotação
    self.x = ponto_rotacao[0] + delta_x * math.cos(
        angulo_radianos) - delta_y * math.sin(angulo_radianos)
    self.y = ponto_rotacao[1] + delta_x * math.sin(
        angulo_radianos) + delta_y * math.cos(angulo_radianos)

  def __str__(self):
    return f'Objeto nas posições: ({self.x}, {self.y})'


# função para exibir as posições
def exibir_posicoes(obj):
  print(obj)


# criando um objeto inicial
objeto = Objeto(5, 3)

# ponto de rotação
ponto_rotacao = (1, 1)

# exibindo as posições iniciais
print("Posição Inicial:")
exibir_posicoes(objeto)

# realizando uma rotação de 45 graus em torno do ponto de rotação
objeto.rotacao(ponto_rotacao, 45)

# exibindo as posições após a rotação
print("\nPosição após a rotação:")
exibir_posicoes(objeto)
