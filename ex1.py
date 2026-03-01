class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.bateria = 100

celular1 = Celular('Apple', '14 pro')
celular2 = Celular('Samsung', 'A23')

print(celular1.marca)
print(celular2.bateria)