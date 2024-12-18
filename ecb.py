import aes
import imagem

caminho_imagem_antes_txt = 'selfie_antes.txt'
caminho_imagem_depois_txt = 'selfie_depois.txt'
caminho_blocos_encrypted_txt = 'selfie_encrypt.txt'
caminho_blocos_decrypted_txt = 'selfie_decrypt.txt'
caminhoImagemRec = 'selfie_recuperada.jpeg'

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

def ecb_cipher(blocks, key):
    # Array para armazenar os resultados criptografados
    blocos_criptografados = []
    
    # Para cada bloco na lista de blocos, criptografa com aes_encrypt
    for bloco in blocks:
        # Converte o bloco para decimais e criptografa com AES
        criptografado = aes.aes_encrypt(aes.converter_para_decimais(bloco), key, 10)
        
        # Formata o bloco criptografado como hexadecimal
        blocos_criptografados.append(aes.format_state_hex(criptografado))
    
    # Salva os blocos criptografados em um arquivo de texto
    with open(caminho_blocos_encrypted_txt, 'w') as output_file:
        for bloco_criptografado in blocos_criptografados:
            output_file.write(bloco_criptografado + '\n')
    
    return blocos_criptografados

def ecb_decipher(caminhoOr, caminhoDest, key):
    # Array para armazenar os resultados descriptografados
    blocos_descriptografados = []

    # Lê os blocos criptografados do arquivo
    with open(caminhoOr, 'r') as input_file:
        blocos_criptografados = input_file.read().splitlines()
    
    # Para cada bloco no arquivo, realiza a descriptografia
    for bloco_hex in blocos_criptografados:
        # Converte o bloco hexadecimal para decimais e descriptografa com AES
        bloco_decimais = aes.converter_para_decimais(bloco_hex)
        descriptografado = aes.aes_decrypt(bloco_decimais, key, 10)
        
        # Converte o bloco descriptografado para hexadecimal
        blocos_descriptografados.append(aes.format_state_hex(descriptografado))
    
    # Salva os blocos descriptografados em um novo arquivo de texto
    with open(caminhoDest, 'w') as output_file:
        for bloco in blocos_descriptografados:
            output_file.write(bloco + '\n')
    
    return blocos_descriptografados

def blocks_unprep(caminho_decrypted, caminho_saida):
    # Lê os blocos formatados do arquivo
    with open(caminho_decrypted, 'r') as file:
        blocos = file.read().splitlines()  # Lê cada linha como um bloco
    
    # Remove os espaços entre os bytes e junta os blocos
    hex_string = ''.join(bloco.replace(' ', '') for bloco in blocos)
    
    # Salva a string hexadecimal no arquivo de saída
    with open(caminho_saida, 'w') as output_file:
        output_file.write(hex_string)
    
    return hex_string


def main():
    
    choice = input("Digite 1 para cifrar e 2 para decifrar: ")

    if choice == '1':

        chave = input("\nInsira a chave nesse formato: \n"
                    "00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f\n"
                    "Insira aqui: ")
        
        if aes.verificar_formato(chave) == False:
            print("\nFormato inválido! Digite 16 bytes separados por um espaço.")
            return 
    
        resultadoChave = aes.converter_para_bytes(chave)
        print("\nChave: ", resultadoChave)

        caminho_selfie = input("\nInsira o caminho da imagem: ")

        hex_string = imagem.imagem_para_hex(caminho_selfie)
        imagem.salvar_hex_em_txt(hex_string, caminho_imagem_antes_txt)

        blocos = blocks_prep(caminho_imagem_antes_txt)
        
        blocos_encrypted = ecb_cipher(blocos, resultadoChave)
        
        verImagem = input("\nDeseja ver a imagem? y para sim e n para não: ")

        if verImagem == 'y':
            print("Imagem original está em selfie_original.jpeg")
            print("Imagem criptografada está em selfie_cripto.jpeg")

            with open(caminho_imagem_antes_txt, 'r') as file:
                hex_string_lido = file.read()
            imagem.hex_para_imagem(hex_string_lido, 'selfie_original.jpeg')
            
            blocosUnp = blocks_unprep(caminho_blocos_encrypted_txt, 'selfie_encrypt_processada.txt')
            
            with open('selfie_encrypt_processada.txt', 'r') as file:
                hex_string_lido2 = file.read()
            imagem.hex_para_imagem(hex_string_lido2, 'selfie_cripto.jpeg')
        else:
            return


    elif choice == '2':
        chave = input("\nInsira a chave nesse formato: \n"
                    "00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f\n"
                    "Insira aqui: ")
        
        if aes.verificar_formato(chave) == False:
            print("\nFormato inválido! Digite 16 bytes separados por um espaço.")
            return 
    
        resultadoChave = aes.converter_para_bytes(chave)
        print("\nChave: ", resultadoChave)

        blocos_decrypted = ecb_decipher(caminho_blocos_encrypted_txt, caminho_blocos_decrypted_txt, resultadoChave)

        blocos_unpreped = blocks_unprep(caminho_blocos_decrypted_txt, caminho_imagem_depois_txt)

        verImagem = input("\nDeseja ver o resultado da imagem? y para sim e n para não: ")

        if verImagem == 'y':
            with open(caminho_imagem_depois_txt, 'r') as file:
                hex_string_lido = file.read()
            imagem.hex_para_imagem(hex_string_lido, caminhoImagemRec)
            print(f"Imagem está em {caminhoImagemRec}")
        else:
            return


if __name__ == "__main__":
    main()
