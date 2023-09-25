class Objeto:
    def __init__(self, x, y):
        self.x = x  # coordenada x do objeto
        self.y = y  

    def reflexao_eixo_x(self):
        # realiza a reflexão em relação ao eixo x
        self.y = -self.y

    def reflexao_eixo_y(self):
        # realiza a reflexão em relação ao eixo y
        self.x = -self.x

    def __str__(self):
        return f'Objeto nas posições: ({self.x}, {self.y})'


# função para exibir as posições do objeto
def exibir_posicao(obj):
    print(obj)


# criando um objeto inicial nas posições
objeto = Objeto(3, 2)

# exibindo a Posição Inicial
print("Posição Inicial:")
exibir_posicao(objeto)

# realizando a reflexão em relação ao eixo x
objeto.reflexao_eixo_x()

# exibindo as posições após a reflexão em relação ao eixo x
print("\nPosição após a reflexão em relação ao eixo x:")
exibir_posicao(objeto)

# realizando a reflexão
objeto.reflexao_eixo_y()

# exibindo as posições após a reflexão em relação ao eixo y
print("\nPosição após a reflexão em relação ao eixo y:")
exibir_posicao(objeto)
