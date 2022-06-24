from conexao import Conexao

def initDB():
    conecta = Conexao()
    conecta.connect()
    #criar tabela tipoUsuario
    conecta.execute("CREATE TABLE IF NOT EXISTS tipoUsuario(idTipoUsuario integer primary key, descricao text not null, siglaTipo text not null);")
    #criar tabela usuario
    conecta.execute("CREATE TABLE IF NOT EXISTS usuario(idUsuario integer primary key, nome text not null, idade integer not null, idDoTipoUsuario integer not null, foreign key(idDoTipoUsuario) references tipoUsuario(idTipoUsuario));")
    #criar tabela projeto
    conecta.execute("CREATE TABLE IF NOT EXISTS projeto (idProjeto integer primary key, siglaProjeto text not null, descricaoP text not null, nomeUsuarioGerente text not null, idDoUsuario integer not null, foreign key (idDoUsuario) references usuario(idUsuario));")
    #criar tabela tarefa
    conecta.execute("CREATE TABLE IF NOT EXISTS tarefa (idTarefa integer primary key, siglaTarefa text not null, descricaoT text not null, dataInicio timestamp, dataPrevisaoFim datetime not null, dataConclusao datetime, acoesRealizadas text not null, nomeUsuarioColaborador text not null, idDoProjeto integer, idUser integer not null, foreign key (idUser) references usuario(idUsuario), foreign key(idDoProjeto) references projeto(idProjeto));")
    conecta.persist()
    conecta.disconnect()