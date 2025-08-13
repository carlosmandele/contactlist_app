# contactsDirectory-app

### Projeto de avliação ifsp - devDjango


```
import os
import json


'''Construindo uma aplicação de Agenda de Contatos'''
class Contato:
    '''Class que representa um contato na agenda'''
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

# Lista para guardar os objetos contato em memoria
lista_contatos =[]


ARQUIVO_CONTATOS = "contatos.json"

def salvar_contatos(contatos):
    try:
        contatos_para_salvar = [
            {"nome": c.nome, "telefone": c.telefone, "email": c.email}
            for c in contatos
        ]

        with open(ARQUIVO_CONTATOS, 'W') as arquivo:
            json.dump(contatos_para_salvar, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar contatos: {e}")

def carregar_contatos():
    # Carregar contatos do arquivo JSON para lista em memoria
    contatos = []
    try:
        if os.path.exists(ARQUIVO_CONTATOS):
            with open(ARQUIVO_CONTATOS, 'r') as arquivo:
                dados = json.load(arquivo)
                for item in dados:
                    contatos.append(Contato(item['nome'], item['telefone'], item['email']))
    except (FileNotFoundError, json.JSONDecoderError) as e:
        print(f"Erro ao carregar contatos: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    return contatos

'''Adicionando um novo conatota a lista'''
def adicionar_contatos():
    print("\n--- Adicionar Contato ---")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()

    if nome:
        novo_contato = Contato(nome, telefone, email)
        lista_contatos.append(novo_contato)
        salvar_contatos(lista_contatos)
        print("Contato adicionado com sucesso! ")
    else:
        print("Erro: Nome é obrigatório! ")

# Lista todos os contatos da agenda
def listar_contatos():
    print("\n--- Lista de Contatos ---")
    if not lista_contatos:
        print("Nenhum contato cadastrado.")
        return
    
    for i, contato in enumerate(lista_contatos, 1):
        print(f"{i}. {contato.nome} - {contato.telefone} - {contato.email}")

# Buscando contatos por nome
def buscar_contato():
    print("\n--- Buscar Contato ---")
    termo = input("Digite o nome ou parte do nome: ").strip().lower()

    encontrados = []
    for contato in lista_contatos:
        if termo in contato.nome.lower():
            encontrados.append(contato)

    if not encontrados:
        print("Nenhum contato encontrado")
        return
    
    print("\nRESULTADOS DA BUSCA:")
    for i, contato in enumerate(encontrados, 1):
        print(f"{i}. {contato.nome} - {contato.telefone} - {contato.email}")

# Excluindo um contato da lista
def remover_contato():
    print("\n--- Remover Contato ---")
    listar_contatos()

    if not lista_contatos:
        return
    
    try:
        indice = int(input("\nDigite o número do contato a excluir: ")) -1


        if 0 <= indice< len(lista_contatos):
            excluido = lista_contatos.pop(indice)
            salvar_contatos(lista_contatos)
            print(f"Contato '{excluido.nome}' excluido com sucesso! ")
        else:
            print("Número inválido.")
    except ValueError:
        print("Erro: Digite um número válido.")


def menu_principal():
    global lista_contatos
    lista_contatos = carregar_contatos()


    while True:
        print("\n--- AGENDA DE CONTATOS ---")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Buscar Contato")
        print("4. Remover Contato")
        print("5. Sair")

        opcao = input("\nEscolha uma opçao: ").strip()

        if opcao == '1':
            adicionar_contatos()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '5':
            print("\nSaindo da agenda. Até logo! ")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()

```