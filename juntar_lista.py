class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa(nome = '{self.nome}', idade = {self.idade})"
    
lista_pessoas = []
nomes = ['ze', 'chico', 'maria']
idades = [35, 45, 15]

for nome, idade in zip(nomes, idades):
    lista_pessoas.append(Pessoa(nome, idade))

print(lista_pessoas)
