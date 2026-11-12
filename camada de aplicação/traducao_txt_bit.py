# Ajustar a importação 
# from teste.bit_byte import bytes_para_bits, bits_para_bytes
# -------------------------------------    
# transformar textos -> BITS

def texto_para_bits(dados):
    texto = dados
    
    # transformar em bytes
    txt_bytes = bytearray(texto, 'utf-8')
    
    # transformar em bits
    txt_bits = bytes_para_bits(txt_bytes)
    
    return txt_bits

# -----------------------
# Transformar os bits para texto
def bits_para_textos(dados):
    bits_dados = dados
    
    # transformar em bytes
    dados_bytes = bits_para_bytes(bits_dados)
    
    # transformar em textos
    bit_txt = dados_bytes.decode('utf-8')
    
    return bit_txt




# -------------- EXEMPLO TESTE

a = input()

tans = texto_para_bits(a)

print(tans)

inv = bits_para_textos(tans)

print(inv)
