# Arquivo main.py

from pessoa import Pessoa

# Criação de instâncias
pessoa1 = Pessoa(nome="Alice", idade=30, cidade="Bauru")
nova_pessoa = Pessoa(nome="", idade=0, cidade="")

# Utilização de getters e setters
nova_pessoa.set_nome(input('Digite o nome: '))
nova_pessoa.set_idade(input('Digite a idade: '))
nova_pessoa.set_cidade(input('Digite a cidade: '))

# Utilização de getters para imprimir os valores
print(nova_pessoa.get_nome(), nova_pessoa.get_idade(), nova_pessoa.get_cidade())

# Chamada do método cumprimentar
nova_pessoa.cumprimentar()
pessoa1.cumprimentar()
