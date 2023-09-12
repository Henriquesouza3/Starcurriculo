from pessoa import Pessoa
pessoa1 = Pessoa("Danielo", "29/08/2005", "Masculino", "024.231.232-29", "danilo@gmail.com.br")
print(f"Nome: {pessoa1.nome}\nData de nascimento: {pessoa1.data_nascimento}\nGênero: {pessoa1.genero}\nCPF: {pessoa1.cpf}\nE-mail: {pessoa1.email}")

pessoa1.setNome("Muliro")
print(f"Nome atualizado: ")
