# Desenquadro por flags com inserção de bits

def des_bit_stuffing(quadro):
    quadro_recebido = quadro
    flag_bit = '01111110'
    bit_especial = '111110'
    
    cinco_bits = '11111'
    
    tam_flag = len(flag_bit)
    tam_quadro = len(quadro_recebido)
    
    # retirando as flags de bits inicio e fim
   
    if quadro_recebido[0:tam_flag] == flag_bit and quadro_recebido[tam_quadro-tam_flag:] == flag_bit:
        carga_util = quadro_recebido.replace(quadro_recebido[0:tam_flag], '')
        carga_util = quadro_recebido.replace(quadro_recebido[tam_quadro-tam_flag:], '')
        
    # verificando se há 5 bits '1' com '0'
    mensagem = carga_util.replace(bit_especial, cinco_bits)
    
    
        
    return mensagem
    



# Enquadramento por flags com Bit sturffing (inserção de bits)
'''
O Enquadramento por inserção de bits funciona assim:
Cada quadro começa e termina com um padrão de bits especial, 01111110, ou 0x7E 
em hexadecimal
 quadro = [01111110, carga util, 01111110]

A cada 5 bits '1' inserir um '0' em seguida
'''

def bit_stuffing(dados):
    carga_util = dados
    flag_bit = '01111110'
    
    cinco_bits = '11111'
    
    # verificando se há 5 bits '1'
    if cinco_bits in dados:
        carga_util = carga_util.replace(cinco_bits, cinco_bits+'0')
    
    quadro = flag_bit + carga_util + flag_bit 
        
    return quadro
    
    

# Chamada e resultado
mensagem = '01111110'

quadro_bits = bit_stuffing(mensagem)

print(f'...ENQUADRAMENTO... \n Escrevi assim : {mensagem}, tamanho : {len(mensagem)} \n quadro gerado: {quadro_bits}, tamanho gerado: {len(quadro_bits)} \n')

desquadro_bits = des_bit_stuffing(quadro_bits)

print(f'...DESENQUADRO...\n quadro recebido: {quadro_bits}, tamanho: {len(quadro_bits)} \n mensagem descriptografada : {desquadro_bits} tamanho: {len(desquadro_bits)} \n \n A mensagem é {mensagem==desquadro_bits}')
