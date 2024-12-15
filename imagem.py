def imagem_para_hex(imagem_path):
    # Abre a imagem em modo binário
    with open(imagem_path, 'rb') as file:
        # Lê os bytes da imagem
        imagem_bytes = file.read()
    
    # Converte os bytes para uma string hexadecimal
    hex_string = imagem_bytes.hex()
    
    return hex_string

def salvar_hex_em_txt(hex_string, caminho_txt):
    # Salva a string hexadecimal no arquivo .txt
    with open(caminho_txt, 'w') as file:
        file.write(hex_string)

def hex_para_imagem(hex_string, caminho_imagem):
    # Converte a string hexadecimal de volta para bytes
    imagem_bytes = bytes.fromhex(hex_string)
    
    # Salva os bytes em um arquivo de imagem
    with open(caminho_imagem, 'wb') as file:
        file.write(imagem_bytes)

# Exemplo de uso
# caminho_imagem = 'selfie.jpeg'     # Caminho da imagem original
# caminho_arquivo_txt = 'selfie.txt'  # Caminho onde o arquivo .txt será salvo
# caminho_imagem_recuperada = 'selfie_recuperada.jpeg'  # Caminho para a imagem recuperada

# # Converte a imagem para hexadecimal
# hex_string = imagem_para_hex(caminho_imagem)

# # Salva a string hexadecimal no arquivo .txt
# salvar_hex_em_txt(hex_string, caminho_arquivo_txt)

# Lê a string hexadecimal do arquivo .txt
# with open(caminho_arquivo_txt, 'r') as file:
#     hex_string_lido = file.read()

# # Converte a string hexadecimal de volta para a imagem
# hex_para_imagem(hex_string_lido, caminho_imagem_recuperada)

# print(f'Imagem salva como {caminho_imagem_recuperada}')
