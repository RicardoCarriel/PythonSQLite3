from conexao import Conexao
from cores import Cores
from sqlite3 import Error



class Tarefa:



    def drop():
        try:  
            conecta = Conexao()
            conecta.connect()
            conecta.execute("drop table tarefa")
            print("deu certo")
        except Error as e:
            print(e)
        finally:
            conecta.disconnect()
    
    def view():
        try:    
            conecta = Conexao()
            conecta.connect()
            conecta.execute("select * from tarefa;")
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Tarefa".center(173))
            print("|{:<5}|{:<7}|{:<30}|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|{:<10}|{:<10}|".format("id", "sigla", "descricaoT", "dataInicio", "dataPrevFim", "dataConc", "acoesRealizadas", "Colaborador", "idProj", "idUsuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<7}|{:<30}|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|{:<10}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3], rows[it][4], rows[it][5], rows[it][6], rows[it][7], rows[it][8], rows[it][9]))
            print(f"{Cores.ENDC}")
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Pesquisa realizada com sucesso em tipoUsuario.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def insert(idTarefa, siglaTarefa, descricaoT, dataInicio, dataPrevisaoFim, dataConclusao, acoesRealizadas, nomeUsuarioColaborador, idDoProjeto, idUser):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("insert into tarefa (idTarefa, siglaTarefa, descricaoT, dataInicio, dataPrevisaoFim, dataConclusao, acoesRealizadas, nomeUsuarioColaborador, idDoProjeto, idUser) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (idTarefa, siglaTarefa, descricaoT, dataInicio, dataPrevisaoFim, dataConclusao, acoesRealizadas, nomeUsuarioColaborador, idDoProjeto, idUser))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Inserção realizada com sucesso em TAREFA.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def search(idTarefa="", siglaTarefa="", descricaoT="", dataInicio="", dataPrevisaoFim="", dataConclusao="", acoesRealizadas="", nomeUsuarioColaborador="", idDoProjeto="", idUser=""):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("select * from tarefa WHERE idTarefa=? or siglaTarefa=? or descricaoT=? or dataInicio=? or dataPrevisaoFim=? or dataConclusao=? or acoesRealizadas=? or nomeUsuarioColaborador=? or idDoProjeto=? or idUser=?;", (idTarefa, siglaTarefa, descricaoT, dataInicio, dataPrevisaoFim, dataConclusao, acoesRealizadas, nomeUsuarioColaborador, idDoProjeto, idUser))
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Tarefa".center(173))
            print("|{:<5}|{:<7}|{:<30}|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|{:<10}|{:<10}|".format("id", "sigla", "descricaoT", "dataInicio", "dataPrevFim", "dataConc", "acoesRealizadas", "Colaborador", "idProj", "idUsuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<7}|{:<30}|{:<20}|{:<20}|{:<20}|{:<20}|{:<20}|{:<10}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3], rows[it][4], rows[it][5], rows[it][6], rows[it][7], rows[it][8], rows[it][9]))
            print(f"{Cores.ENDC}")
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Pesquisa realizada com sucesso em TAREFA.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()    
    
    
    def update(idTarefa, siglaTarefa, descricaoT, dataInicio, dataPrevisaoFim, dataConclusao, acoesRealizadas, nomeUsuarioColaborador, idDoProjeto, idUser):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("update tarefa set siglaTarefa=?, descricaoT=?, dataInicio=?, dataPrevisaoFim=?, dataConclusao=?, acoesRealizadas=?, nomeUsuarioColaborador=?, idDoProjeto=?, idUser=? where idTarefa=?;", (siglaTarefa, descricaoT, dataInicio, dataPrevisaoFim, dataConclusao, acoesRealizadas, nomeUsuarioColaborador, idDoProjeto, idUser, idTarefa))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Atualizacao realizada com sucesso em TAREFA.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()



    def delete(idTarefa):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("delete from tarefa where idTarefa=?;", (idTarefa,))
            conecta.persist()
        except Error as e:
            print(e)
        else:
            print(f"{Cores.BOLD}{Cores.HEADER}Remocao realizada com sucesso em TAREFA.{Cores.ENDC}")
            input(f"{Cores.BOLD}{Cores.OKGREEN}Pressione |ENTER| para continuar{Cores.ENDC}")
        finally:
            conecta.disconnect()
        
        