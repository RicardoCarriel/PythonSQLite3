from conexao import Conexao
from cores import Cores
from sqlite3 import Error

class Tipousuario:


    def view():
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute('SELECT * FROM tipoUsuario;')
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Tipo Usuario".center(60))
            print("|{:<5}|{:<45}|{:<6}|".format("id", "descricao", "sigla"))
            for it in range(len(rows)):
                print("|{:<5}|{:<45}|{:<6}|".format(rows[it][0], rows[it][1], rows[it][2]))
            print(f"{Cores.ENDC}")
        except Error as e:
            print(e)
        
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Pesquisa realizada com sucesso em tipoUsuario.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()

    
    
    def insert(idTipoUsuario, descricao, siglaTipo):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("insert into tipoUsuario (idTipoUsuario, descricao, siglaTipo) values (?, ?, ?);", (idTipoUsuario, descricao, siglaTipo))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.MAG}Inserção realizada com sucesso em TIPO USUARIO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()
            
    
    
    
    def search(idTipoUsuario="", descricao="", siglaTipo=""):
        try:    
            conecta = Conexao()
            conecta.connect()
            conecta.execute("select * from tipoUsuario where idTipoUsuario=? or descricao=? or siglaTipo=?;", (idTipoUsuario, descricao, siglaTipo))
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Tipo Usuario".center(60))
            print("|{:<5}|{:<45}|{:<6}|".format("id", "descricao", "sigla"))
            for it in range(len(rows)):
                print("|{:<5}|{:<45}|{:<6}|".format(rows[it][0], rows[it][1], rows[it][2]))
            print(f"{Cores.ENDC}")
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Pesquisa realizada com sucesso em TIPO USUARIO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def update(idTipoUsuario, descricao, siglaTipo):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("update tipoUsuario set descricao=?, siglaTipo=? WHERE idTipoUsuario = ?;", (descricao, siglaTipo, idTipoUsuario))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Atualizacao realizada com sucesso em TIPO USUARIO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def delete(idTipoUsuario):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("delete from tipoUsuario where idTipoUsuario=?;", (idTipoUsuario,))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Remocao realizada com sucesso em TIPO USUARIUO.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()
    