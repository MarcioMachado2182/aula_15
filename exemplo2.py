class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Pessoa(nome = '{self.nome}', idade = {self.idade})"
    
pessoa1 = Pessoa('alice', 15)
pessoa2 = Pessoa('ze', 35)
pessoa3 = Pessoa('Chico', 18)



#print (repr(pessoa))
lista_pessoas = [pessoa1, pessoa2, pessoa3]
#print(lista_pessoas)

for pessoa in lista_pessoas:
    print(f'Nome: {pessoa.nome} Idade:{pessoa.idade}')