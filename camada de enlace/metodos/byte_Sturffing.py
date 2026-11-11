# Desenquadramento por Byte stuffing (inserção por byte)

def des_byte_sturffing(quadro):
    dados_msg = ''.join(quadro)
    
    flag = '_'
    esc = ' '
    caract_especial = esc+flag
    
    if caract_especial in dados_msg:
        dados_msg = dados_msg.replace(caract_especial, flag)
    
    lista_caract = list(dados_msg) # listar os dados
    
    fix_tam_quadro = 256  # cada quadro tem um limite de 254 caracteres + as 2 flags
    tam_dados = len(lista_caract)
    
    msg_quadro = []
    
    if tam_dados <= fix_tam_quadro:
        msg_quadro = lista_caract
        del msg_quadro[0]
        del msg_quadro[-1]
        
        
    else:
        posicao = 0
        limite = 256
        fatia = []
        
        while posicao < len(dados):
            fatia = lista_caract[posicao:limite]
            
            del fatia[0]
            del fatia[-1]
            
            posicao = limite+1
            limite += 256
            msg_quadro += fatia
            
    
    mensagem_desqu = ''.join(msg_quadro)
    
    return mensagem_desqu 





# Enquadramento por Byte stuffing (inserção por byte)

'''
O metodo de enquadramento por flags com inserção por byte sturffing funciona assim:
quadro = [FLAG, dados de carga util, FLAG]

FLAG é 1 byte, um caracter especial
caso haja o mesmo nbyte de flag na carga util, adicionar um byte de ESC

quadro  = [FLAG, ESC, carga util, FLAG]

'''

def byte_sturffing(dados):
   
    flag = '_' # a flag para utilizar
    esc = ' '
    
    # caso tenha uma flag dentro, adicionar um ESC
    if flag in dados:
        dados = dados.replace(flag, esc+flag)
     
    lista_caract = list(dados) # listar os dados
    
    fix_tam_quadro = 254  # cada quadro tem um limite de 254 caracteres + as 2 flags
    tam_dados = len(lista_caract)
    
    quadro = []
    if tam_dados < fix_tam_quadro:
        quadro = lista_caract
        quadro.insert(0, flag)
        quadro.insert(tam_dados+1, flag)
        
    else:
        posicao = 0
        limite = 254
        fatia = []
        
        while posicao < len(dados):
            fatia = lista_caract[posicao:limite]
            
            fatia.insert(0, flag)
            quadro.insert(tam_dados+1, flag)
            
            posicao = limite
            limite += 254
            quadro += fatia 
    
    
    
    return quadro



# Chamada e impressão de resultado
msg = 'a' * 30 + ' '+ '_' + 'b' + "_"
print('.....ENQUADRAMENTO.....\n')
enq_bytesturffing = byte_sturffing(msg)
print(f'A mensagem original foi: \n {msg} \n\nEnquadramento por byte sturffing: \n {''.join(enq_bytesturffing)} \n ')

des_msg = des_byte_sturffing(enq_bytesturffing)

print(f'.....DESENQUADRAMENTO.....: \n {des_msg} \n Será que é igual? \n É {msg==des_msg}')
