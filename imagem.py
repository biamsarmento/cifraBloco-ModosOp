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
