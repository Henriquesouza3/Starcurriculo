from pessoa import Pessoa
from funcionario import Funcionario
from cliente import Cliente

lista_clientes = []
lista_funcionario =[]

def getNome(self):
    return self .__nome =
    "sobrenome"


def cadastrarCliente():
    print("Digite os dados solicitados;")
    nome = input("Digite o nome:")
    data_nascimento = input("Digite a data de nascimento:")
    genero = input("Digite a o genero:")
    cpf = input("Digite o cpf:")
    email = input("Digite o email:")
    endereco = input("Digite o endereço:")
    valor_compra = input("Digite o valor da compra:")
    forma_pagamento = input("Digite a forma de pagamento:")
    numero_telefone = input("Digite o numero do Cliente:")
    cliente = Cliente(nome, data_nascimento, genero, cpf, email, endereco, numero_telefone, valor_compra, forma_pagamento)
    return cliente

def cadastraFuncionario():
    print("Digite os dados solicitados:")
    Nome = input("Digite o nome:")
    Data_nascimento = input("Digite a data de nascimento:")
    Genero = input("Digite a o genero:")
    Cpf = input("Digite o cpf:")
    Email = input("Digite o email:")
    Matricula = input("Digite a Matricula:")
    Cargo = input("Digite a ocupação:")
    Salario = input("Digite o salario:")
    funcionario = Funcionario(Nome, Data_nascimento, Genero, Cpf, Email, Matricula, Cargo, Salario )
    return funcionario

def remove_cliente():
    removecliente= input("Digite o nome do cliente para ser removido: ")

    for rem in lista_clientes:
        if rem.getNome() == removecliente:
            lista_clientes.remove(rem)

def remove_funcioario():
    removefuncionario= input("Digite o nome do cliente para ser removido: ")

    for rem in lista_funcionario:
        if rem.getNome() == removefuncionario:
            lista_funcionario.remove(rem)


run = True

x = 0
while x==0:
    menu = int(input("Bem Vindo ao SysElegancy. sua botiquye digital!\nO QUE VAMOS FAZER HOJE?\n-------------------------------------------\n1 - Cadastrar clientes novos clientes.\n2 - Cadastrar novo funcionario\n3 - lista todos os clientes:\n4 - Listar todos os Funcionarios\n5 - Procurar cliente pelo nome:\n6 - Procurar fucncionario por nome:\n7 - Remover cliente: \n8 - Remover funcionario: \n0 - Sair:" ))
    
    if menu == 1:
        cliente = cadastrarCliente()
        lista_clientes.append(cliente)

        #cadastro de clientes
    elif menu == 2:
        funcionario = cadastraFuncionario()
        lista_funcionario.append(funcionario)
        #cadastro de funcionarios

    elif menu == 3:
        for cliente in lista_clientes:
            print("-------------------------------------------------------------")
            print(cliente.getNome())

    elif menu == 4:
        for funcionario in lista_funcionario:
            print("-------------------------------------------------------")
            print(funcionario.getNome())

    elif menu == 5:
        nome = input("-------------------------------------------------------------\nDigite o nome do cliente: ")
        if cliente.getNome() == nome:
            print("-------------------------------------------------------------\nCliente Encontrado!!!")
        encontrados = 0     
        for cliente in lista_clientes:
            if cliente.getNome() == nome:
                encontrados += 1
            print(f"-----------------------------------------------------------\nClinte encontrado:\nNome: {cliente.getNome()}\nData de Nascimento: {cliente.getDataNascimento()}\nGenero: {cliente.getGenero()}\nCPF: {cliente.getCpf()}\nEmail: {cliente.getEmail()}\nNumero de telefone: {cliente.getNumero_telefone()}\n Total de Compras: R${cliente.getValor_compra()}\nForma de pagamento: {cliente.getForma_pagamento}")
        if encontrados == 0:
            print("Cliente não encontrado!!!")
 
    elif menu == 6:
        encontrados = 0   
        nome = input("-----------------------------------'-'-------------------------\nDigite o nome do cliente: ")
        for funcionario in lista_funcionario:
            if funcionario.getNome() == nome:
                encontrados += 1
            print(f"-----------------------------------------------------------\nFuncionarios encontrado:\nNome: {funcionario.getNome()}\nData de Nascimento: {funcionario.getDataNascimento()}\nGenero: {funcionario.getGenero()}\nCPF: {funcionario.getCpf()}\nMatricula: {funcionario.getMatricula()}\nCargo: {funcionario.getCargo()}\nSalario: {funcionario.getSalario()}")
        if encontrados == 0:
            print("Funcionario não encontrado!!!")

    elif menu == 7:
        remove_cliente()

    elif menu == 8:
        remove_funcioario()

    elif menu != 0:
        print("Digite a opção valida!")
        
    
    else:
        print("Obrigado por utilizar o sysElegancy ")
        x += 1

for x in lista_clientes:
    print(f"\nDados atualizados: \nNome: {x.getNome()}\nData de Nascimento: {x.getDataNascimento()}\nGenero: {x.getGenero()}\nCpf: {x.getCpf()}\nEmail: {x.getEmail()}\nEndereço: {x.getEndereco()}\nTelefone: {x.getNumero_telefone()}\nValor da compra: {x.getValor_compra()}")
 
for x in lista_funcionario:
    print(f"\nDados atualizados: \nNome: {x.getNome()}\nData de Nascimento: {x.getDataNascimento()}\nGenero: {x.getGenero()}\nCpf: {x.getCpf()}\nEmail: {x.getEmail()}\nMatricula: {x.getMatricula()}\nCargo: {x.getCargo()}\nSalario: {x.getSalario()}")
 