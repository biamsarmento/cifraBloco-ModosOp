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

def xor_blocks(block1, block2):
    """Realiza a operação XOR entre dois blocos de bytes de mesmo tamanho e retorna no formato 4x4."""
    
    # Converte os blocos de string com espaços em bytes
    block1_bytes = bytes.fromhex(block1)
    block2_bytes = bytes.fromhex(block2)
    
    # Realiza o XOR byte a byte entre os blocos
    xor_result = [b1 ^ b2 for b1, b2 in zip(block1_bytes, block2_bytes)]
    
    # Divida o resultado em uma matriz 4x4 (16 bytes no total)
    return [xor_result[i:i+4] for i in range(0, len(xor_result), 4)]

def format_state_hex(text):
    """Formata o estado como uma matriz 4x4 de valores hexadecimais."""
    return ' '.join(' '.join(f"{byte:02x}" for byte in row) for row in text)
# Função para garantir que a matriz 4x4 seja passada corretamente para aes.aes_encrypt
def matrix_to_bytes(matrix):
    """Converte uma matriz 4x4 de inteiros para uma lista de bytes (16 bytes no total)."""
    return [byte for row in matrix for byte in row]  # Flatten a matriz e converte para bytes

# Função para converter bytes de volta para a matriz 4x4 de inteiros
def bytes_to_matrix(bytes_data):
    """Converte uma lista de 16 bytes de volta para uma matriz 4x4 de inteiros."""
    return [bytes_data[i:i+4] for i in range(0, len(bytes_data), 4)]

def increment_iv(iv_inc):
    # Converte a matriz 4x4 em uma lista de bytes (16 bytes)
    iv_bytes = matrix_to_bytes(iv_inc)
    
    # Começa pelo último byte e propaga o carry, se necessário
    for i in range(len(iv_bytes) - 1, -1, -1):
        iv_bytes[i] += 1
        if iv_bytes[i] < 256:  # Se o byte não ultrapassar 255, não há carry
            break
        iv_bytes[i] = 0  # Se ultrapassar 255, zera o byte e continua para o próximo
       
    # Converte de volta para uma matriz 4x4
    return bytes_to_matrix(iv_bytes)

# Função que cifra o IV (em formato de matriz 4x4) com a chave fornecida
def encrypt_iv_with_key(iv_en, key, rounds):
    # Converte o IV para uma lista de 16 bytes
    # iv_bytes = matrix_to_bytes(iv_matrix)

    # Cifra o IV com a chave AES
    iv_plus_key = aes.aes_encrypt(iv_en, key, rounds)

    # Converte os bytes cifrados de volta para a matriz 4x4
    return format_state_hex(iv_plus_key)

import copy  # Importa a biblioteca para cópias profundas

def gcm(blocos_preped, key, iv, dest_file, rounds=10):
    iv_temp = copy.deepcopy(iv)  # Faz uma cópia profunda de iv

    # Abre o arquivo para salvar os resultados
    with open(dest_file, 'w') as result_file:

        # Itera sobre os blocos
        for i, bloco in enumerate(blocos_preped):

            iv_plus_key = encrypt_iv_with_key(iv_temp, key, rounds)
            
            xor_result = xor_blocks(bloco, iv_plus_key)

            # Converte o resultado para o formato adequado e salva no arquivo
            result_file.write(format_state_hex(xor_result) + '\n')

            # Incrementa o IV para o próximo bloco
            iv = increment_iv(iv)  # Incrementa o IV antes de usá-lo novamente

            iv_temp = copy.deepcopy(iv)  # Faz uma cópia profunda do IV atualizado
