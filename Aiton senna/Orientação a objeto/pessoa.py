class Pessoa:
    def __init__ (self, nome="default", data_nascimento="default", genero="default", cpf="default", email="default"):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__genero = genero
        self.__cpf = cpf
        self.__email = email


    def getNome(self):
        return self.__nome
    
    def setNome(self, novoNome):
        self.__nome = novoNome

    def getDataNascimento(self):
        return self.__data_nascimento
    
    def setDataNascimento(self, nova_data_nascimento):
        self.__data_nascimento = nova_data_nascimento

    def getGenero(self):
        return self.__genero

    def setGenero(self, novogenero):
        self.__genero = novogenero

    def getCpf(self):
        return self.__cpf

    def setCpf(self, novocpf):
        self.__cpf = novocpf

    def getEmail(self):
        return self.__email

    def setEmail(self, novoemail):
        self.__email = novoemail

    

