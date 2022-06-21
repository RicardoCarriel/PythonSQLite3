poltronas = [0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0,
            0, 0]
def mostrarAssentos(poltronas):
    print('MAPA             NUMEROS')
    for i in range(0,48, 4):
        print(poltronas[i], poltronas[i+1],'    ', poltronas[i+2], poltronas[i+3], '    ', i+1, i+2, i+3, i+4)

while True:
    desejo = int(input('O que você deseja fazer?\n [1] Para ver os assentos disponiveis (quando tiver o numero 0 esta disponivel e 1 ja esta ocupado.\n [2]Comprar passagem.'))
    if desejo == 1:
        mostrarAssentos(poltronas)
    #elif desejo == 2:
        
            

