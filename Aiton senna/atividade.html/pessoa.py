
class Pessoa:
    def __init__(self, nome="default", data_nascimento = "default", genero = "default", cpf="default", email="default"): #valor aos atributos
       self.nome = nome
       self.data_nascimento = data_nascimento
       self.genero = genero
       self.cpf = cpf
       self.email = email
    def setNome(self, novoNome):
        self.nome = novoNome
    
    def getNome(self):
        return self.nome
