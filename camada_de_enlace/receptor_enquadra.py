# ------------------------------
from metodos.contagem_caracteres import contagem_caracteres, desenquadramento_contagem
from metodos.byte_stuffing import byte_stuffing, des_byte_stuffing

from transf_bits_bytes import bits_para_bytes

if __name__ == '__main__':
    
    ''' Teste abaixo'''    
    # tem que criar um metodo para transformar msg em bits
    # msg_client = input()
    
    dado_bruto = f'{5:08b}{9:08b}{11:08b}'
    print(f' Mensagem original transformada em bits : {dado_bruto} \n')
    print('metodos: contagem \n ')
    
    selection_mtd = input("Qual metodo de enquadramento deseja utilizar? Selecione a opção \n 1 - contagem \n 2 - Bytestuffing \n OP: ")
    # Escolher um metodo de enquadramento
    match selection_mtd:
        case '1':
            contagem = contagem_caracteres(dado_bruto)
            print()
            print(f'Mensagem transmitida para o receptor: {bits_para_bytes(contagem)}, {contagem}')
            print('.....Recebendo..........')
            desquadro = desenquadramento_contagem(contagem)
            print(f'mensagem recebida e desenquadrada: {bits_para_bytes(desquadro)}, {desquadro}, {desquadro==dado_bruto}')

        case '2':
            byte_stuffing = byte_stuffing(dado_bruto)
            print()
            print(f'Mensagem transmitida para o receptor: {bits_para_bytes(byte_stuffing)}, {byte_stuffing}')
            print('.....Recebendo..........')
            desquadro = des_byte_stuffing(byte_stuffing)
            print(f'mensagem recebida e desenquadrada: {bits_para_bytes(desquadro)}, {desquadro}, {desquadro==dado_bruto}')
        case _:
            print('Ainda em Construção ')
    
