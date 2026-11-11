from caract import contagem_caracteres
from transf_bits_bytes import bits_para_bytes

''' Teste abaixo'''    

dado_bruto = f'{5:08b}{9:08b}'
print(dado_bruto)

contagem = contagem_caracteres(dado_bruto)

#print(contagem)

print(bits_para_bytes(contagem))

