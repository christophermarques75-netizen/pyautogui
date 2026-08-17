class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False  # atributo booleano para estado do carro

    def ligar(self):
        self.ligado = True
        print(f"Seu carro é um {self.modelo} da marca {self.marca} e está ligado.")

# Criando uma instância (objeto)
meu_carro = Carro("Toyota", "Corolla")

# Usando um método
meu_carro.ligar()
