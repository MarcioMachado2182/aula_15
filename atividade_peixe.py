class Peixe:
    def __init__(self, especie, tipo_de_agua, profundidade):
        self.especie = especie
        self.tipo_de_agua = tipo_de_agua
        self.profundidade = profundidade

    def __repr__(self):
        return f"O peixe (especie = '{self.especie}', tipo_de_agua = {self.tipo_de_agua}, profundidade = {self.idade})"
    
peixe1 = ['sardinha', 'Mar', 50]
peixe2 = ['tainha', 'Rio', 20]
peixe3 = ['Salmao', 'Mar', 100]
peixe4 = ['Bagre', 'Rio', 15]
peixe5 = ['Atum', 'Mar', 200]

lista_peixes = [peixe1, peixe2, peixe3, peixe4, peixe5]

print(lista_peixes)

