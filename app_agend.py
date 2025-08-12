'''Construindo uma aplicação de Agenda de Contatos'''
class Contato:
    '''Class que representa um contato na agenda'''
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        # lista_conta para guardar os objetos em memoria
    lista_contatos =[]
    
    def adicionar_contato(self):
        Contato.lista_contato.append(self)
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"