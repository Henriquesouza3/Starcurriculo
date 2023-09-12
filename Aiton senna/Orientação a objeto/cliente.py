from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self,nome ="default", data_nascimento="default", genero ="default", cpf ="default", email ="default", endereco ="default", numero_telefone="default", valor_compra ="default", forma_pagamento ="default"):
        super().__init__(nome, data_nascimento, genero, cpf, email)
        self.__endereco = endereco
        self.__numero_telefone = numero_telefone
        self.__valor_compra = valor_compra
        self.__forma_pagamento = forma_pagamento

    def getEndereco(self):
        return self.__endereco
    
    def setEndereco(self, novoendereco):
        self.__endereco = novoendereco

    def getNumero_telefone(self):
        return self.__numero_telefone
    
    def setNumero_telefone(self, novonumero_telefone):
        self.__numero_telefone = novonumero_telefone

    def getValor_compra(self):
        return self.__valor_compra
    
    def setValor_compra(self, novavalor_compra):
        self.__valor_compra = novavalor_compra

    def getForma_pagamento(self):
        return self.__forma_pagamento
    
    def setForma_pagamento(self, novoforma_pagamento):
        self.__forma_pagamento = novoforma_pagamento