# Desenvolver uma função para enquadrar uma sequência de bytes usando o metodo contagem de caracteres
'''
A entrada recebida é um fluxo de dados brutos que devem ser tratados antes de tonarem em bits na proxima camada
você deve inserir no primeiro byte do quadro o tamanho do quadro em formato de byte 
escolha o tamanho que deve seguir

'''
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

dado_bruto = 'a' * 300 +'b'

contagem = contagem_caracteres(dado_bruto)

print(contagem, len(contagem))
