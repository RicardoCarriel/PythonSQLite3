from conexao import Conexao
from cores import Cores
from sqlite3 import Error

class Usuario:


    def view():
        try:    
            conecta = Conexao()
            conecta.connect()
            conecta.execute("select * from usuario;")
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Usuario".center(72))
            print("|{:<5}|{:<45}|{:<7}|{:<10}|".format("id", "nome", "idade", "id usuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<45}|{:<7}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3]))
            print(f"{Cores.ENDC}")

        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Pesquisa realizada com sucesso em tipoUsuario.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def insert(idUsuario, nome, idade, idDoTipoUsuario):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("insert into usuario (idUsuario, nome, idade, idDoTipoUsuario) values (?, ?, ?, ?);", (idUsuario, nome, idade, idDoTipoUsuario))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Insercao realizada com sucesso em USUARIO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def search(idUsuario="", nome="", idade="", idDoTipoUsuario=""):
        try:    
            conecta = Conexao()
            conecta.connect()
            conecta.execute("select * from usuario where idUsuario=? or nome=? or idade=? or idDoTipoUsuario=?;", (idUsuario, nome, idade, idDoTipoUsuario))
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Usuario".center(72))
            print("|{:<5}|{:<45}|{:<7}|{:<10}|".format("id", "nome", "idade", "id usuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<45}|{:<7}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3]))
            print(f"{Cores.ENDC}")
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Pesquisa realizada com sucesso em USUARIO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def update(idUsuario, nome, idade, idDoTipoUsuario):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("update usuario set nome=?, idade=?, idDoTipoUsuario=? where idUsuario=?;", (nome, idade, idDoTipoUsuario, idUsuario))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Atualizacao realizada com sucesso em USUARIO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def delete(idUsuario):
        try:    
            conecta = Conexao()
            conecta.connect()
            conecta.execute("delete from usuario where idUsuario=?;", (idUsuario))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Remocao realizada com sucesso em USUARIO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()

        
        
        