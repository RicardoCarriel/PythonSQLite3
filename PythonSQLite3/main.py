from sqlite3 import Error
import schema
from projeto import Projeto as pr
from tarefa import Tarefa as ta
from tipoUsuario import Tipousuario as tu
from usuario import Usuario as us
from time import sleep
from scripts import Scripts
from cores import Cores


#funcao para fazer a limpeza da tela
def clear():
    import os


    def screenClear():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')

    sleep(1)
    screenClear()

    
#criando o menu principal
def menu():
    clear()
    print(f"{Cores.BOLD}{Cores.MAG}▬▬▬MENU QUERATINA▬▬▬\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{Cores.ENDC}")
    print(f"{Cores.BOLD}{Cores.MAG}▬▬▬▬▬▬▬OPCOES▬▬▬▬▬▬▬\n1. tipoUsuario\n2. Usuario\n3. Projeto\n4. Tarefa\n5. Colaboradores sem tarefas atribuidas\n6. Ver todas tabelas\n7. Projeto com tarefa em aberto\n8. Tarefa por periodo \n9. Sair{Cores.ENDC}")
    escolha = int(input(f"{Cores.BOLD}{Cores.CIA}Indique sua escolha: "))
    print(f"{Cores.ENDC}")
    return escolha



#criando o menu secundario para cada tabela
def submenu(tabela):
    clear()
    print(f"{Cores.BOLD}{Cores.MAG}▬▬▬.◙.▬▬▬\n▂▄▄▓▄▄▂\n◢◤ █▀▀████▄▄▄▄▄▄◢◤\n█▄ █ :) ██▀▀▀▀▀▀▀╬\n◥█████◤\n══╩══╩══")
    print(f"   ╬═╬\n   ╬═╬\n   ╬═╬\n   ╬═╬\n   ╬═╬Desci pra pedir que\n   ╬═╬escolha mais uma opcao\n   ╬═╬\n   ╬═╬☻/\n   ╬═╬/▌\n   ╬═╬/ \ ")
    print(f"▬▬▬▬▬▬▬OPCOES▬▬▬▬▬▬▬{Cores.ENDC}")
    print(f"{Cores.BOLD}{Cores.FAIL}0. Retorna ao menu principal{Cores.ENDC}")
    print(f"{Cores.BOLD}{Cores.MAG}1. Inserir {tabela}")
    print(f"2. Atualizar {tabela}")
    print(f"3. Pesquisar {tabela}")
    print(f"4. Pesquisar especifico {tabela}")
    print(f"5. Excluir {tabela}{Cores.ENDC}")
    escolha1 = int(input(f"{Cores.BOLD}{Cores.CIA}Indique sua escolha: "))
    print(f"{Cores.ENDC}")
    return escolha1


#conectando com o banco e criando as tabelas se não existirem
def conectarBD():
    try:
        schema.initDB()
        print(f"{Cores.BOLD}{Cores.OKGREEN}")
        print(" Tabelas criadas com exito ".center(40, '▬'), f"{Cores.ENDC}")
    except Error as e:
        print(e)


if __name__ == '__main__':
    clear()
    print(f"{Cores.BOLD}{Cores.MAG}▬"*40)
    print("  BEM-VINDO A QUERATINA  ".center(40, '▬'))
    print(f"▬"*40)
    print("  Conectando o banco de dados  ".center(40, '▬'))
    print("  Criando o banco de dados  ".center(40, '▬'))
    print("  Criando conexão  ".center(40, '▬'))
    print("  Criando tabelas  ".center(40, '▬'))
    sleep(2)
    conectarBD()
    print(f"{Cores.BOLD}{Cores.MAG}")
    input(f"  Pressione |ENTER| para continuar  ".center(40, '▬'))
    print(f"{Cores.ENDC}")
    try:
        escolha = menu()
        while escolha != 9:
            if escolha == 1:
                tabela = 'tipoUsuario'
            elif escolha == 2:
                tabela = 'usuario'
            elif escolha == 3:
                tabela = 'projeto'
            elif escolha == 4:
                tabela = 'tarefa'
            elif escolha == 5:
                Scripts.colaboradores()
                tabela = ''
                print(f"{Cores.BOLD}{Cores.MAG}")
                input(f"  Pressione |ENTER| para continuar  ".center(40, '▬'))
                print(f"{Cores.ENDC}")
            elif escolha == 6:
                Scripts.verTodas()
                tabela = ''
                print(f"{Cores.BOLD}{Cores.MAG}")
                input(f"  Pressione |ENTER| para continuar  ".center(40, '▬'))
                print(f"{Cores.ENDC}")
            elif escolha == 7:
                Scripts.tarefasProjeto()
                tabela = ''
                print(f"{Cores.BOLD}{Cores.MAG}")
                input(f"  Pressione |ENTER| para continuar  ".center(40, '▬'))
                print(f"{Cores.ENDC}")
            elif escolha == 8:
                tabela = ''
                dataInicial = input('Data inicial: ')
                dataFinal = input('Data final: ')
                Scripts.pesqTarefa(dataInicial, dataFinal)
                print(f"{Cores.BOLD}{Cores.MAG}")
                input(f"  Pressione |ENTER| para continuar  ".center(40, '▬'))
                print(f"{Cores.ENDC}")
            else:
                print('Opcao invalida')
            escolha2 = 0
            if tabela != '':
                escolha2 = submenu(tabela)
            
            while escolha2 != 0:
                if escolha2 == 1:
                    print(f"{Cores.BOLD}{Cores.MAG}Inserir dados na tabela: {tabela}")
                    if tabela == 'tipoUsuario':
                        id = int(input("Id Tipo Usuario: "))
                        descricao = input("Descricao: ")
                        sigla = input("Sigla Tipo: ")
                        tu.insert(id, descricao, sigla)
                    elif tabela == 'usuario':
                        id = int(input("Id Usuario: "))
                        nome = input("Nome: ")
                        idade = int(input("Idade: "))
                        idUser = int(input("Id Tipo Usuario: "))
                        us.insert(id, nome, idade, idUser)
                    elif tabela == 'projeto':
                        id = int(input("Id Projeto: "))
                        sigla = input("Sigla: ")
                        descricao = input("Descricao: ")
                        nome = input('Nome Usuario Gerente: ')
                        idUser = int(input("Id Usuario: "))
                        pr.insert(id, sigla, descricao, nome, idUser)
                    elif tabela == 'tarefa':
                        id = input('Id Tarefa: ')
                        sigla = input('Sigla: ')
                        descricao = input('Descricao: ')
                        dataInicio = input("Data Inicial: ")
                        dataPrev = input("Data de previsao do fim: ")
                        dataConc = input("Data de conclusao: ")
                        acoes= input("Acoes realizadas: ")
                        nome = input("Nome usuario colaborador: ")
                        idPro = input("Id Projeto: ")
                        idUs = input('Id Usuario: ')
                        ta.insert(id, sigla, descricao, dataInicio, dataPrev, dataConc, acoes, nome, idPro, idUs)
                    print(f"{Cores.ENDC}")
                    clear()
                elif escolha2 == 2:
                    print(f"{Cores.BOLD}{Cores.MAG}Atualizar valores na tabela: {tabela}")
                    if tabela == 'tipoUsuario':
                        id = int(input("Id Tipo Usuario: "))
                        descricao = input("Descricao: ")
                        sigla = input("Sigla Tipo: ")
                        tu.update(id, descricao, sigla)
                    elif tabela == 'usuario':
                        id = int(input("Id Usuario: "))
                        nome = input("Nome: ")
                        idade = int(input("Idade: "))
                        idUser = int(input("Id Tipo Usuario: "))
                        us.update(id, nome, idade, idUser)
                    elif tabela == 'projeto':
                        id = input("Id Projeto: ")
                        sigla = input("Sigla: ")
                        descricao = input("Descricao: ")
                        nome = input('Nome Usuario Gerente: ')
                        idUser = int(input("Id Usuario"))
                        pr.update(id, sigla, descricao, nome, idUser)
                    elif tabela == 'tarefa':
                        id = input('Id Tarefa: ')
                        sigla = input('Sigla: ')
                        descricao = input("Descricao: ")
                        dataInicio = input("Data inicio: ")
                        dataPrev = input("Data de previsao do fim: ")
                        dataConc = input("Data de conclusao: ")
                        acoes= input("Acoes realizadas: ")
                        nome = input("Nome usuario colaborador: ")
                        idPro = input("Id Projeto: ")
                        idUs = input('Id Usuario: ')
                        ta.update(id, sigla, descricao, dataInicio, dataPrev, dataConc, acoes, nome, idPro, idUs)
                    print(f"{Cores.ENDC}")
                    clear()
                elif escolha2 == 3:
                    print(f"{Cores.BOLD}{Cores.MAG}tabela {tabela}:")
                    if tabela == 'tipoUsuario':
                        tu.view()
                        sleep(1)
                    elif tabela == 'usuario':
                        us.view()
                        sleep(1)
                    elif tabela == 'projeto':
                        pr.view()
                        sleep(1)
                    elif tabela == 'tarefa':
                        ta.view()
                        sleep(1)
                    print(f"{Cores.ENDC}")
                    clear()

                elif escolha2 == 4:
                    print(f"{Cores.BOLD}{Cores.MAG}Pesquisa especifica em: {tabela}")
                    if tabela == 'tipoUsuario':
                        id = int(input("Id Tipo Usuario: "))
                        descricao = input("Descricao: ")
                        sigla = input("Sigla Tipo: ")
                        tu.search(id, descricao, sigla)
                        sleep(1)
                    elif tabela == 'usuario':
                        id = input("Id Usuario: ")
                        nome = input("Nome: ")
                        idade = input("Idade: ")
                        idUser = input("Id Tipo Usuario: ")
                        us.search(id, nome, idade, idUser)
                        sleep(1)
                    elif tabela == 'projeto':
                        id = input("Id Projeto: ")
                        sigla = input("Sigla: ")
                        descricao = input("Descricao: ")
                        nome = input('Nome Usuario Gerente: ')
                        idUser = input("Id Usuario: ")
                        pr.search(id, sigla, descricao, nome, idUser)
                        sleep(1)
                    elif tabela == 'tarefa':
                        id = int(input('Id Tarefa: '))
                        sigla = input('Sigla: ')
                        descricao = input("Descricao: ")
                        dataInicio = input("Data de inicio: ")
                        dataPrev = input("Data de previsao do fim: ")
                        dataConc = input("Data de conclusao: ")
                        acoes= input("Acoes realizadas: ")
                        nome = input("Nome usuario colaborador: ")
                        idPro = input("Id Projeto: ")
                        idUs = input('Id Usuario: ')
                        ta.search(id, sigla, descricao, dataInicio, dataPrev,dataConc, acoes, nome, idPro, idUs)
                        sleep(1)
                    print(f"{Cores.ENDC}")
                    clear()
                elif escolha2 == 5:
                    print(f"{Cores.BOLD}{Cores.MAG}Pesquisa especifica em: {tabela}")
                    if tabela == 'tipoUsuario':
                        tu.view()
                        id = input("Id: ")
                        tu.delete(id)
                    elif tabela == 'usuario':
                        us.view()
                        id = input('Id: ')
                        us.delete(id)
                    elif tabela == 'projeto':
                        pr.view()
                        id = input("Id: ")
                        pr.delete(id)
                    elif tabela == 'tarefa':
                        ta.view()
                        id = input('Id: ')
                        ta.delete(id)
                    else:
                        print("Opcao invalida")
                        clear
                    print(f"{Cores.ENDC}")
                escolha2 = submenu(tabela)
                clear()


               
            else:
                
                print(f"{Cores.BOLD}{Cores.OKGREEN}Voltando ao menu principal...{Cores.ENDC}")
                sleep(2)
            escolha = menu() 
            clear()
                        
                        

    except ValueError:
        print("Opção de Menu selecionada inválida. Deve ser um número.")
    finally:
        print("Pressione Run novamente")