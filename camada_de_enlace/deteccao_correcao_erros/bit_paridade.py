# CONTROLE DE ERROS: DETECÇÃO E CORREÇÃO

'''
Para simular a confiabilidade em um canal ruidoso, adicione redundâncias aos quadros gerados na
subetapa anterior. O transmissor deve calcular e anexar o código de verificação, e o receptor deve
validar a integridade e descartar ou sinalizar quadros corrompidos utilizando:
'''
def ver_paridade_par(quadro):
    msg_paridade = quadro
    
    bit_paridade = msg_paridade[-1]
    
    msg_sem_paridade = msg_paridade[:len(msg_paridade)-1]
    
    # recalcular paridade
    qtd_bits = 0
    
    for i in msg_sem_paridade:
        if i == '1':
            qtd_bits += 1
    # bit de paridade verificado        
    ver_bit = '0' if qtd_bits % 2 == 0 else '1'
    
    if ver_bit == bit_paridade:
        return msg_paridade
    else:
        return 'QUADRO COM ERRO DE PARIDADE'


# -----------------------------
# Adicionar o bit de paridade par
def add_paridade_par(quadro):
    
    msg_paridade = quadro
    
    qtd_bits = 0
    
    for i in msg_paridade:
        if i == '1':
            qtd_bits += 1
    
    if qtd_bits % 2 == 1:
        msg_paridade += '1'
    else:
        msg_paridade += '0'
    
    
    return msg_paridade

# ------------- EXEMPLO 
bit3 = f'{3:08b}'

par = add_paridade_par(bit3)
print(par)

ver = ver_paridade_par(par)

print(ver)
