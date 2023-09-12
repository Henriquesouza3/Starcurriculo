from pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__ (self, nome, data_nascimento, genero, cpf, email, matricula, cargo, salario):
        
        super().__init__(nome, data_nascimento, genero, cpf, email)
        self.__matricula = matricula
        self.__cargo = cargo
        self.__salario = salario


    def getMatricula(self):
        return self.__matricula

    def setMatricula(self, novomatricula):
        self.__matricula = novomatricula
    
    def getCargo(self):
        return self.__cargo

    def setCargo(self, novocargo):
        self.__cargo = novocargo

    def getSalario(self):
        return self.__salario

    def setSalario(self, novosalario):
        self.__salario = novosalario



    
    

    


    
    