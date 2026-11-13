#-------------------------------------------------------------
# Desenquadramento por flags com Bit sturffing (inserção de bits)
#-------------------------------------------------------------
def des_bit_stuffing(quadro):
    bits_msg = quadro

    # Flag de bits fixa em '01111110' que é 126
    flag = f'{126:08b}'
    
    # Retirar as flags iniciais e finais 
    tam_quadro = len(bits_msg)
    
    if flag == bits_msg[0:8] == bits_msg[tam_quadro-8:tam_quadro]:
        # armazenar a carga util
        carga_util = bits_msg[8:tam_quadro-8]
    
    dados = ''
    
    # verificar a existencias de 5 bits '1's seguidos
    cont_bit = 0
    
    
    for bit in carga_util:
            
        if bit == '0' and cont_bit == 5:
            cont_bit = 0
        else:
            if bit == '1':
                cont_bit += 1
            dados += bit
   
    return dados
    


#-------------------------------------------------------------
# Enquadramento por flags com Bit sturffing (inserção de bits)
#-------------------------------------------------------------
def bit_stuffing(dados):
    bits_msg = dados


    # Flag de bits fixa em '01111110' que é 126
    flag = f'{126:08b}'
    
    # Armazenar bits da mensagem
    carga_util = ''
    
    # verificar a existencias de 5 bits '1's seguidos
    cont_bit = 0
    
    for bit in bits_msg:
        carga_util += bit
        
        if bit == '1':
            cont_bit += 1
            
            if cont_bit == 5:
                carga_util += '0'
                cont_bit = 0
        
    quadro = flag + carga_util + flag
    
    return quadro   


'''TESTE
# Chamada e resultado
mensagem = '01111110'

quadro_bits = bit_stuffing(mensagem)
print(quadro_bits)
# print(f'...ENQUADRAMENTO... \n Escrevi assim : {mensagem}, tamanho : {len(mensagem)} \n quadro gerado: {quadro_bits}, tamanho gerado: {len(quadro_bits)} \n')

desquadro_bits = des_bit_stuffing(quadro_bits)

print(f'...DESENQUADRO...\n quadro recebido: {quadro_bits}, tamanho: {len(quadro_bits)} \n mensagem descriptografada : {desquadro_bits} tamanho: {len(desquadro_bits)} \n \n A mensagem é {mensagem==desquadro_bits}')
'''
