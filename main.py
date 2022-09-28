import string, os

lista_usuario = []

class Usuario:
    id: int
    nome: string
    idade: int
    rg: string

    def __init__(self, id, nome, idade, rg):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.rg = rg


def menu():
    print("### Menu Sistema ###")
    print("# 1. Cadastrar #")
    print("# 2. Remover #")
    print("# 3. Listar #")
    print("# 4. Atualizar #")
    print("# 5. Fechar #")
    print("### ------&------ ###")
    options = input("Digite a operação: ")

    if options == "1":
        cadastrar()
    elif options == "2":
        remover()
    elif options == "3":
        listar()
    elif options == "4":
        atualizar()
    elif options == "5":
        fechar()

def reload(mensagem: string, function):
    options = input(mensagem + " [1-Sim/2-Não]: ")
    if options == "1":
        function()
    elif options == "2":
        menu()
def cadastrar():
    id = input("ID: ")
    nome = input("NOME: ")
    idade = input("IDADE: ")
    rg = input("RG: ")
    usuario = Usuario(id, nome, idade, rg)
    lista_usuario.append(usuario)
    print("Aluno cadastrado com sucesso")
    reload("Gostaria de cadastrar uma nova pessoa?", cadastrar)

def remover():
    id = input("Digite o ID: ")
    for index, list in lista_usuario:
        if list.id == id:
            lista_usuario.remove(0)

    print("Aluno Removido com sucesso")
    reload("Gostaria de remover outro aluno?", remover)
def listar():
    for list in lista_usuario:
        print(list)
    reload("Gostaria listar novamente?", listar)
def atualizar():
    reload("Gostaria de atualizar mais pessoas?", atualizar)
def fechar():
    os.system('pause')
def main():
    menu()

main()