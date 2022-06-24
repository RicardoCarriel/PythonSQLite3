from conexao import Conexao
from sqlite3 import Error
from cores import Cores


class Scripts:

    
    
    def colaboradores():
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("select nome from usuario where idDoTipoUsuario=2 and idUsuario not in (select idUser from tarefa);")
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print('| Colaboradores sem tarefa |')
            for it in range(len(rows)):
                print("|{:<26}|".format(rows[it][0]))
                print(f'{Cores.ENDC}')
        except Error as e:
            print(e)

        finally:
            conecta.disconnect()



    def verTodas():
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
            
            conecta.execute("select * from usuario;")
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Usuario".center(72))
            print("|{:<5}|{:<45}|{:<7}|{:<10}|".format("id", "nome", "idade", "id usuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<45}|{:<7}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3]))
            print(f"{Cores.ENDC}")
            
            conecta.execute("select * from projeto;")
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Projeto".center(118))
            print("|{:<5}|{:<7}|{:<45}|{:<45}|{:<10}|".format("id", "sigla", "descricaoP", "nomeUsuarioGerente", "idUsuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<7}|{:<45}|{:<45}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3], rows[it][4]))
            print(f"{Cores.ENDC}")

            conecta.execute("select * from tarefa;")
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Tarefa".center(183))
            print("|{:<5}|{:<7}|{:<30}|{:<20}|{:<20}|{:<20}|{:<30}|{:<20}|{:<10}|{:<10}|".format("id", "sigla", "descricaoT", "dataInicio", "dataPrevFim", "dataConc", "acoesRealizadas", "Colaborador", "idProj", "idUsuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<7}|{:<30}|{:<20}|{:<20}|{:<20}|{:<30}|{:<20}|{:<10}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3], rows[it][4], rows[it][5], rows[it][6], rows[it][7], rows[it][8], rows[it][9]))
            print(f"{Cores.ENDC}")

        except Error as e:
            print(e)

        finally:
            conecta.disconnect()



    def tarefasProjeto():
        try:    
            conecta = Conexao()
            conecta.connect()
            conecta.execute("select * from projeto p inner join tarefa t on p.idProjeto = t.idDoProjeto where dataConclusao like '';")
            rows = conecta.fetchall()
            print()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Projeto com tarefa em aberto".center(118))
            print("|{:<5}|{:<7}|{:<45}|{:<45}|{:<10}|".format("id", "sigla", "descricaoP", "nomeUsuarioGerente", "idUsuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<7}|{:<45}|{:<45}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3], rows[it][4]))
            print(f"{Cores.ENDC}")
            conecta.persist()
        except Error as e:
            print(e)

        finally:
            conecta.disconnect()


    def pesqTarefa(dataInicio, dataFim):
        try:
            conecta = Conexao()
            conecta.connect()
            conecta.execute("select * from tarefa t where t.dataInicio>? and t.dataConclusao<?;", (dataInicio, dataFim))
            rows = conecta.fetchall()
            print(f"{Cores.BOLD}{Cores.PRE}{Cores.BRA}")
            print("Tarefa".center(183))
            print("|{:<5}|{:<7}|{:<30}|{:<20}|{:<20}|{:<20}|{:<30}|{:<20}|{:<10}|{:<10}|".format("id", "sigla", "descricaoT", "dataInicio", "dataPrevFim", "dataConc", "acoesRealizadas", "Colaborador", "idProj", "idUsuario"))
            for it in range(len(rows)):
                print("|{:<5}|{:<7}|{:<30}|{:<20}|{:<20}|{:<20}|{:<30}|{:<20}|{:<10}|{:<10}|".format(rows[it][0], rows[it][1], rows[it][2], rows[it][3], rows[it][4], rows[it][5], rows[it][6], rows[it][7], rows[it][8], rows[it][9]))
            print(f"{Cores.ENDC}")

        except Error as e:
            print(e)

        finally:
            conecta.disconnect()
