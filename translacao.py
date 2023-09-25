class Objeto:
    def __init__(self, x, y):
        self.x = x  # inicializa a posição x
        self.y = y  

    # metodo para realizar a translação do objeto
    def translacao(self, delta_x, delta_y):
        self.x += delta_x  # att a posição x com o deslocamento em delta_x
        self.y += delta_y  

    # método para representar o objeto como uma str
    def __str__(self):
        return f'Objeto nas posições: ({self.x}, {self.y})'


# função para exibir as posições
def exibir_posicoes(obj):
    print(obj)

# criando um objeto inicial nas posições
objeto = Objeto(0, 0)

# exibindo as posição inicial
print("Posição Inicial:")
exibir_posicoes(objeto)

# realizando a translação
objeto.translacao(5, 3)

# exibindo as posições
print("\nPosição após a translação:")
exibir_posicoes(objeto)
