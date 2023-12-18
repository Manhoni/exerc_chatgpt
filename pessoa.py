# Arquivo pessoa.py

class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.__nome = nome
        self.__idade = idade
        self.__cidade = cidade


    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_cidade(self):
        return self.__cidade


    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def set_idade(self, nova_idade):
        self.__idade = nova_idade
    
    def set_cidade(self, nova_cidade):
        self.__cidade = nova_cidade

    def cumprimentar(self):
        print(f'{self.__nome} está cumprimentando.')

    
