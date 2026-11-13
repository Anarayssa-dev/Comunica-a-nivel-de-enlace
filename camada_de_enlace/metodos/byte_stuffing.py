#importar transformações de bits e bytes
from transf_bits_bytes import bits_para_bytes, bytes_para_bits

# ----------------------------------------------
# Desenquadramento por metodo de Byte Stuffing
# -----------------------------------------------
def des_byte_stuffing(quadro):
    
    bytes_msg = bits_para_bytes(quadro)
    

    # Flag é o caracter especial _ 
    flag = ord('_')
    
    # ESC para uso anterior do flag se há igual
    esc = ord(' ')
    
    tam_quadro = len(bytes_msg)
    
    # Retirar as flags de inicio e fim
    if flag == bytes_msg[0] == bytes_msg[-1]:
        # armazenar a carga util
        carga_util = bytes_msg[1:tam_quadro-1]
        
    # verificar a existencias dos caracteres especiais na mensagem transmitida
    tam_carga = len(carga_util)
    dados_carga = bytearray()
        
    for i, byte in enumerate(carga_util):
        if i+1 < tam_carga:
            prox_byte = carga_util[i+1]
            if (byte == esc and (prox_byte == flag or prox_byte == esc)) == False:
                dados_carga.append(byte)
        else:
            dados_carga.append(byte)
    
    # transformar em trem de bits
    dados = bytes_para_bits(dados_carga)

    return dados

# ----------------------------------------------
# Enquadramento por metodo de contagem_caracteres
# -----------------------------------------------

def byte_stuffing(dados):
    bytes_msg = bits_para_bytes(dados)

    # Flag é o caracter especial _ 
    flag = ord('_')
    
    # ESC para uso anterior do flag se há igual
    esc = ord(' ')
    
    # armazenar a carga util
    carga_util = bytearray()
    
    # verificar a existencias dos caracteres especiais na mensagem transmitida
    for byte in bytes_msg:
        
        if byte == flag or byte == esc:
            carga_util.append(esc)
        carga_util.append(byte)
        
    flag = bytearray([flag]) # int para formato de bytes
 
    quadro = flag + carga_util + flag
    
    # transformar em trem de bits
    quadro = bytes_para_bits(quadro)
    return quadro 


'''TESTE
# Chamada e impressão de resultado
msg_bits = f'{3:08b}{95:08b}'
# print('.....ENQUADRAMENTO.....\n')
enq_bytesturffing = byte_stuffing(msg_bits)

print(f'A mensagem original foi: \n {msg_bits} \n\nEnquadramento por byte sturffing: \n {enq_bytesturffing} \n ')

desquadro = des_byte_stuffing(enq_bytesturffing)
print(desquadro)


print(f'.....DESENQUADRAMENTO.....: \n {desquadro} \n Será que é igual? \n É {msg_bits==desquadro}')

'''
