# transformar BITS -> BYTES 
def bits_para_bytes(dados):
    # transformar bits - bytes
    bits_dados = dados
    tam_quadro = len(bits_dados)
    
    lista_bytes = bytearray()
    
    if tam_quadro % 2 == 0:
        for bit8 in range(0, tam_quadro, 8):
            byte_dado = bits_dados[bit8:bit8+8]
            
            lista_bytes.append(int(byte_dado, 2))
            
    else:
        return 'QUADRO COM ERRO'
        
    return lista_bytes
    
# -------------------------------------    
# transformar BYTES -> BITS    
def bytes_para_bits(dados):
    
    bytes_dados = dados
    # tam_quadro = len(bits_dados)
    
    trem_bits = ''
    
    for byt8 in bytes_dados:
        formato_bit = f"{byt8:08b}"
        trem_bits += formato_bit

    return trem_bits
