import os  # Para manipulação de diretórios

# Função para salvar a string hexadecimal em um arquivo .txt
def salvar_hex_em_txt(hex_string, caminho_txt):
    # Cria o diretório se ele não existir
    os.makedirs(os.path.dirname(caminho_txt), exist_ok=True)
    
    with open(caminho_txt, 'w') as file:
        file.write(hex_string)

# Função principal
if __name__ == "__main__":
    # Caminho da selfie
    input_image_path = "selfie.jpeg"
    output_dir = "output_ecb"

    # Número de rodadas para testar
    rounds_list = [1, 5, 9, 13]

    # Chave AES fixa para todos os testes (16 bytes)
    key = b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"

    # Converter a imagem para hexadecimal
    hex_string = imagem_para_hex(input_image_path)

    # Salvar a string hexadecimal no arquivo .txt
    salvar_hex_em_txt(hex_string, f"{output_dir}/selfie_hex.txt")

    # Lê a string hexadecimal do arquivo .txt
    with open(f"{output_dir}/selfie_hex.txt", 'r') as file:
        hex_string_lido = file.read()

    # Converte a string hexadecimal de volta para a imagem
    hex_para_imagem(hex_string_lido, f"{output_dir}/selfie_recuperada.jpeg")

    # Carregar a imagem original
    image = Image.open(input_image_path)
    blocks, padded_height, padded_width = image_to_blocks(image)

    # Loop sobre diferentes números de rodadas
    for rounds in rounds_list:
        encrypted_blocks = []

        # Cifrar cada bloco
        for block in blocks:
            # Certifique-se de converter o bloco para string hexadecimal (hexadecimal)
            block_as_hex = ''.join(format(byte, '02x') for byte in block)  # Convertendo para string hexadecimal
            encrypted_block = ecb.ecb_cipher([block_as_hex], key, rounds)  # Passando como lista de strings hexadecimais
            encrypted_blocks.append(np.array([int(x, 16) for x in encrypted_block[0]], dtype=np.uint8))  # Convertendo de volta para inteiros

        # Reconstruir a imagem cifrada
        encrypted_image = blocks_to_image(encrypted_blocks, padded_height, padded_width)

        # Salvar a imagem cifrada
        output_image_path = f"{output_dir}/selfie_ecb_{rounds}_rounds.png"
        encrypted_image.save(output_image_path)

        # Calcular e exibir o hash
        encrypted_data = np.array(encrypted_image).tobytes()
        image_hash = calculate_hash(encrypted_data)
        print(f"Rodadas: {rounds}, Hash: {image_hash}")
