#importar transformações
from transf_bits_bytes import bits_para_bytes, bytes_para_bits

# ----------------------------------------------
# Desenquadramento por metodo de contagem_caracteres
# -----------------------------------------------
def desenquadramento_contagem(quadro):
    # Recebe o quadro e verifica o tamanho para retornar a mensagem original 
    quadro_dados = bits_para_bytes(quadro)

    # tamanhos de bytes e quadro
    tam_byte = quadro_dados[0]
    tam_quadro = len(quadro_dados)

    # caso o tamanho do quadro seja menor que o tamanho do byte, retorna o erro
    if tam_byte > tam_quadro:
        return "QUADRO COM ERRO DE TAMANHO"
    
    dados_recebidos = bytearray() 

    # puxar os dados do quadro pelo tamanho do byte
    while len(quadro_dados) > 0:
        for i in range(1, tam_byte):
            dados_recebidos.append(quadro_dados[i])

        dif_tam = tam_quadro - tam_byte

        if dif_tam > 0:
            quadro_dados = quadro_dados[tam_byte+1:]
            dados_recebidos += desenquadramento_contagem(quadro_dados) 

        else:
            break

    # transformar os dados em bits
    mensagem_recebida = bytes_para_bits(dados_recebidos)
    
    return mensagem_recebida 

# ----------------------------------------------
# Enquadramento por metodo de contagem_caracteres
# -----------------------------------------------
def contagem_caracteres(dados):
    bytes_msg = bits_para_bytes(dados)
    
    tam_carat = len(bytes_msg)+1
    trem_bytes = bytes([tam_carat]) + bytes_msg
    
    quadro = bytes_para_bits(trem_bytes)
    
    return quadro
