import string, os

lista_usuario = []
optionsMenu = ['1', '2', '3', '4', '5']
optionsAceite = ['1', '2']

def menu():
    print("### Menu Sistema ###")
    print("# 1. Cadastrar #")
    print("# 2. Remover   #")
    print("# 3. Listar    #")
    print("# 4. Atualizar #")
    print("# 5. Fechar    #")
    print("### ------&------ ###")
    options = input("Digite a operação: ")
    if options in optionsMenu:
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
    else:
        print("Invalid Option")
        menu()

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
    usuario = [id, nome, idade, rg]
    lista_usuario.append(usuario)
    print("Aluno cadastrado com sucesso")
    reload("Gostaria de cadastrar uma nova pessoa?", cadastrar)

def getUsuario(id, list):
    cont = 0
    for usuario in list:
        cont += 1
        if usuario[0] is id:
            cont -= 1
            return cont

def remover():
    id = input("Digite o ID: ")
    index = getUsuario(id, lista_usuario)
    lista_usuario.pop(index)
    print("Aluno Removido com sucesso")
    reload("Gostaria de remover outro aluno?", remover)
def listar():
    for list in lista_usuario:
        print(list[0] + ',', list[1] + ',', list[2] + ',', list[3])
    reload("Gostaria listar novamente?", listar)
def atualizar():
    id = input("Digite o ID: ")
    index = getUsuario(id, lista_usuario)
    usuario = lista_usuario[index]
    statusNome = input("Atualizar Nome: [1-Sim/2-Não]: ")
    if statusNome == "1":
        nome = input("NOME: ")
        usuario[1] = nome

    statusIdade = input("Atualizar Idade: [1-Sim/2-Não]: ")
    if statusIdade == "1":
        idade = input("Idade: ")
        usuario[2] = idade

    statusRg = input("Atualizar RG: [1-Sim/2-Não]: ")
    if statusRg == "1":
        rg = input("RG: ")
        usuario[3] = rg

    lista_usuario.pop(index)
    lista_usuario.append(usuario)
    reload("Gostaria de atualizar mais pessoas?", atualizar)
def fechar():
    os.system('pause')
def main():
    menu()

main()