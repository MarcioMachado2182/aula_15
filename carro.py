class Carro:
    marca = ''
    modelo = ''
    ano = 0
    cor = ''
    cambio = ''
    valor = 0

    def __init__(self, marca, modelo, ano, cor, cambio, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.cambio = cambio
        self.valor = valor

carro1 = Carro('Renault', 'Duster', 2023, 'Prata', 'Automatico', 85)
print(f'O carro da \n Marca: {carro1.marca}\n Modelo: {carro1.modelo}\n Ano: {carro1.ano}\n Cor: {carro1.cor}\n Cambio: {carro1.cambio}\n Valor: R$ {carro1.valor} mil reais')
