from caract import contagem_caracteres
from transf_bits_bytes import bits_para_bytes

''' Teste abaixo'''    

dado_bruto = f'{5:08b}{9:08b}'
print(dado_bruto)

contagem = contagem_caracteres(dado_bruto)

#print(contagem)

print(bits_para_bytes(contagem))
------------------------------
from caract import contagem_caracteres
from bits_and_bytes import bits_para_bytes


if __name__ == '__main__':
    
    ''' Teste abaixo'''    
    # tem que criar um metodo para transformar msg em bits
    # msg_client = input()
    
    dado_bruto = f'{5:08b}{9:08b}'
    print(f' Mensagem original transformada em bits : {dado_bruto}')
    
    selection_mtd = input()
    # Escolher um metodo de enquadramento
    match selection_mtd:
        case 'contagem':
            contagem = contagem_caracteres(dado_bruto)
            print(bits_para_bytes(contagem))
        case _:
            print('nada foi selecionado')
    
    #print(contagem)
    
    


