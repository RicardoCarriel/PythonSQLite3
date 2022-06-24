from conexao import Conexao
from cores import Cores
from sqlite3 import Error



class Projeto:


    def view():
        try: 
            conecta = Conexao()
            conecta.connect()
            conecta.execute("select * from projeto;")
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Projeto".center(118))
            print("|{:<5}|{:<7}|{:<45}|{:<45}|{:<10}|".format("id", "sigla", "descricaoP", "nomeUsuarioGerente", "idUsuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<7}|{:<45}|{:<45}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3], rows[it][4]))
            print(f"{Cores.ENDC}")
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Pesquisa realizada com sucesso em PROJETO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def insert(idProjeto, siglaProjeto, descricaoP, nomeUsuarioGerente, idDoUsuario):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("insert into projeto (idProjeto, siglaProjeto, descricaoP, nomeUsuarioGerente, idDoUsuario) values(?, ?, ?, ?, ?);", (idProjeto, siglaProjeto, descricaoP, nomeUsuarioGerente, idDoUsuario))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Inserção realizada com sucesso em PROJETO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def search(idProjeto="", siglaProjeto="", descricaoP="", nomeUsuarioGerente="", idDoUsuario=""):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("select * from projeto where idProjeto=? or siglaProjeto=? or descricaoP=? or nomeUsuarioGerente=? or idDoUsuario=?;", (idProjeto, siglaProjeto, descricaoP, nomeUsuarioGerente, idDoUsuario))
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Projeto".center(118))
            print("|{:<5}|{:<7}|{:<45}|{:<45}|{:<10}|".format("id", "sigla", "descricaoP", "nomeUsuarioGerente", "idUsuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<7}|{:<45}|{:<45}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3], rows[it][4]))
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Pesquisa realizada com sucesso em PROJETO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def update(idProjeto, siglaProjeto, descricaoP, nomeUsuarioGerente, idDoUsuario):
        try:   
            conecta = Conexao()
            conecta.connect()
            conecta.execute("update projeto set siglaProjeto=?, descricaoP=?, nomeUsuarioGerente=?, idDoUsuario=? WHERE idProjeto = ?;", (siglaProjeto, descricaoP, nomeUsuarioGerente, idDoUsuario, idProjeto))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Atualizacao realizada com sucesso em PROJETO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def delete(idProjeto):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("delete from projeto where idProjeto=?;", (idProjeto))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Remocao realizada com sucesso em PROJETO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()
