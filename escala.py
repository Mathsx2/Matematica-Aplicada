class Objeto:
    def __init__(self, x, y):
        self.x = x  # posição x do objeto
        self.y = y  

    def escala(self, ponto_escalamento, fator_x, fator_y):
        # deslocamento em relação ao ponto de escalamento
        delta_x = self.x - ponto_escalamento[0]
        delta_y = self.y - ponto_escalamento[1]

        # fórmula de escala
        self.x = ponto_escalamento[0] + delta_x * fator_x
        self.y = ponto_escalamento[1] + delta_y * fator_y

    def __str__(self):
        return f'Objeto nas posições: ({self.x}, {self.y})'

# função para exibir as posições do objeto
def exibir_posicoes(obj):
    print(obj)

# criando um objeto inicial nas posições
objeto = Objeto(5, 3)

# ponto de escalamento (2, 1)
ponto_escalamento = (2, 1)

# fatores de escala (aumento em 2 vezes na direção x e 3 vezes na direção y)
fator_x = 2
fator_y = 3

# exibindo as Posição Inicial
print("Posição Inicial:")
exibir_posicoes(objeto)

# realizando a escala em relação ao ponto de escalamento
objeto.escala(ponto_escalamento, fator_x, fator_y)

# exibindo as posições após a escala
print("\nPosição após a escala:")
exibir_posicoes(objeto)
