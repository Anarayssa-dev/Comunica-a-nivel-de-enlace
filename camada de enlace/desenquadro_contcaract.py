# Desenquadramento por metodo de contagem_caracteres
def desenquadro_contcaract(quadro):
    # mensagem com os dados para retornar
    msg = ''
    
    # recuperar os dados do Enquadramento
    tam_byte = quadro[0]
    tam_quadro = len(quadro)
    
    
    for i in range(1, tam_byte):
        msg += quadro[i]
        
    if tam_byte < tam_quadro:
        if isinstance(quadro[tam_byte+1], int):
            desenquadro_contcaract(quadro[tam_byte+1:])
        else:
            return "DEU MERDA"
    
    else:
        return msg


# Enquadramento por metodo de contagem_caracteres
def contagem_caracteres(dados):
    listagem_caract = list(dados)
    fix_tam_quadro = 255
    tam_quadro = len(listagem_caract)+1
    quadro = []
    
    if tam_quadro < fix_tam_quadro:
        quadro = listagem_caract
        quadro.insert(0, tam_quadro)
        
    else:
        posicao = 0
        limite = 254
        fatia = []
        
        while posicao < len(dados):
            fatia = listagem_caract[posicao:limite]
            fatia.insert(0, len(fatia)+1)
            posicao = limite
            limite += 254
            quadro += fatia 
    
    
    return quadro
    
    
    
''' Teste abaixo'''    

dado_bruto = 'a' * 30 +'b'

contagem = contagem_caracteres(dado_bruto)

print(contagem, len(contagem))

# Desenquadramento

print("Desenquadramento....")

desquad = desenquadro_contcaract(contagem)

print(f'Mensagem : \n \n {desquad} \n \n Tamanho original do Quadro:  {len(desquad)}')
