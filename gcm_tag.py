import aes

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

def galois_multiply(a, b):
    """Multiplica dois valores no campo de Galois (GF(2^128))"""
    result = 0
    for i in range(128):
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & (1 << 127):
            a ^= 0x87  # Polinômio de redução padrão no AES-GCM
    return result

def calculate_tag_from_file(filename, key):
    """Calcula a tag de autenticação para dados cifrados a partir de um arquivo sem usar IV"""
    
    blocks_preped = blocks_prep(filename)

    # Calcula o valor H (cifra de 128 bits do vetor de 0s com a chave)
    # O valor H é a cifra de 128 bits de um vetor de zeros, formatado como uma matriz 4x4
    h_block = [[0, 0, 0, 0],  # 4x4 matriz com zeros
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

    # Cifra o h_block com a chave AES e as 10 rodadas
    h = aes.aes_encrypt(h_block, key, 10)  # Usando a função aes.aes_encrypt

    # Converte 'h' (matriz de 4x4) em uma sequência contínua de bytes
    h_bytes = b''.join([bytes([elem for row in h for elem in row])])

    # Converte a sequência de bytes para um inteiro
    h_int = int.from_bytes(h_bytes, byteorder='big')

    # Inicializa o acumulador (devemos garantir que ele tenha 128 bits)
    accumulator = 0

    # Multiplica no campo de Galois os blocos de ciphertext com o valor H
    for block_hex in blocks_preped:
        # Converte o bloco de string hexadecimal para bytes
        block_bytes = bytes.fromhex(block_hex)
        
        # Converte o bloco de bytes para um inteiro
        block_int = int.from_bytes(block_bytes, byteorder='big')

        # Multiplica o bloco de texto cifrado com o valor H (usando multiplicação de Galois)
        accumulator = galois_multiply(accumulator, h_int)
        accumulator ^= block_int  # XOR com o bloco de texto cifrado

    # Inclui o tamanho do texto cifrado (em bits)
    ciphertext_length = len(blocks_preped) * 8  # Tamanho em bits
    accumulator ^= ciphertext_length  # XOR com o comprimento do texto cifrado

    # Garante que o acumulador tenha apenas 128 bits (16 bytes)
    accumulator &= (1 << 128) - 1  # Máscara para manter os 128 bits mais baixos

    # Retorna a tag de 128 bits (garantindo que tenha 16 bytes)
    return accumulator

def verify_tag(ciphertext_filename, key, expected_tag):
    """Verifica a tag e decifra o texto se a tag for válida"""
    # Calcula a tag de autenticação a partir do ciphertext e do IV
    tag = calculate_tag_from_file(ciphertext_filename, key)

    # Verifica se a tag gerada corresponde à tag fornecida
    if str(tag) == expected_tag:
        return True
    else:
        return False
