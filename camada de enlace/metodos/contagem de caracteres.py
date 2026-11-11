#importar transformações
from transf_bits_bytes import bits_para_bytes, bytes_para_bits

# Enquadramento por metodo de contagem_caracteres
def contagem_caracteres(dados):
    bytes_msg = bits_para_bytes(dados)
    
    tam_carat = len(bytes_msg)+1
    trem_bytes = bytes([tam_carat]) + bytes_msg
    
    quadro = bytes_para_bits(trem_bytes)
    
    return quadro
