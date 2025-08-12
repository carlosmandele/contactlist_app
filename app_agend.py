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
        @classmethod
        def listar_contatos(cls):
            return [f"Nome: {c.nome}, Telefone: {c.telefone}, Email: {c.email}" for c in cls.lista_contatos]

    @classmethod
    def salvar_contatos(Contato):
        return f"Nome: Telefone: {c.telefone}, Email: {c.email}" for c in cls.lista_contat
