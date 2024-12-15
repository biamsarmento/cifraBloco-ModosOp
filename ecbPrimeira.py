import comboComRodada as aes

caminho_arquivo_txt = 'selfie.txt'


# def blocks_prep(caminho_txt):
#     # Lê a string hexadecimal do arquivo .txt
#     with open(caminho_txt, 'r') as file:
#         hex_string = file.read().strip()  # Lê e remove espaços em branco
    
#     # Converte a string hexadecimal para bytes
#     imagem_bytes = bytes.fromhex(hex_string)
    
#     # Tamanho do bloco em bytes (128 bits = 16 bytes)
#     bloco_tamanho = 16
    
#     # Divide os bytes em blocos de 16 bytes (128 bits)
#     blocos = [imagem_bytes[i:i + bloco_tamanho] for i in range(0, len(imagem_bytes), bloco_tamanho)]
    
#     # Verifica o último bloco e adiciona padding (zeros) se necessário
#     if len(blocos[-1]) < bloco_tamanho:
#         blocos[-1] = blocos[-1] + b'\x00' * (bloco_tamanho - len(blocos[-1]))
    
#     return blocos

def blocks_prep(caminho_txt):
    # Lê a string hexadecimal do arquivo .txt
    with open(caminho_txt, 'r') as file:
        hex_string = file.read().strip()  # Lê e remove espaços em branco
    
    # Converte a string hexadecimal para bytes
    imagem_bytes = bytes.fromhex(hex_string)
    
    # Tamanho do bloco em bytes (128 bits = 16 bytes)
    bloco_tamanho = 16
    
    # Divide os bytes em blocos de 16 bytes (128 bits)
    blocos = [imagem_bytes[i:i + bloco_tamanho] for i in range(0, len(imagem_bytes), bloco_tamanho)]
    
    # Verifica o último bloco e adiciona padding (zeros) se necessário
    if len(blocos[-1]) < bloco_tamanho:
        blocos[-1] = blocos[-1] + b'\x00' * (bloco_tamanho - len(blocos[-1]))
    
    # Função para formatar os bytes no formato com e sem espaços
    def format_bytes(block):
        # Formato com espaços entre os bytes
        formatted_with_spaces = ' '.join(format(byte, '02x') for byte in block)
        
        # Formato contínuo, sem espaços
        formatted_continuous = ''.join(format(byte, '02x') for byte in block)
        
        return formatted_with_spaces

    # Formata todos os blocos
    blocos_formatados = [format_bytes(bloco) for bloco in blocos]
    
    return blocos_formatados

def ecb(blocks, key):
    # Array para armazenar os resultados criptografados
    blocos_criptografados = []
    
    # Para cada bloco na lista de blocos, criptografa com aes_encrypt
    for bloco in blocks:
        criptografado = aes.aes_encrypt(aes.converter_para_decimais(bloco), key, 10)
        blocos_criptografados.append(aes.format_state_hex(criptografado))
    
    return blocos_criptografados
    

def main():
    chave = input("\nInsira a chave nesse formato: \n"
                 "00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f\n"
                 "Insira aqui: ")
    
    resultadoChave = aes.converter_para_bytes(chave)
    print("\nChave: ", resultadoChave)

      # Caminho para o arquivo .txt com a imagem em hexadecimal
    blocos = blocks_prep(caminho_arquivo_txt)
    print("\nBlocos: ", blocos)

    blocos_encrypted = ecb(blocos, resultadoChave)

    print("Blocos criptografados: \n", blocos_encrypted)

if __name__ == "__main__":
    main()
