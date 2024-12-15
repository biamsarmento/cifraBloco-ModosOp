import comboComRodada as aes
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes, bytes_to_long

# Função GHASH (operações no campo Galois)
def ghash(h, data):
    """
    Função GHASH simplificada: realiza operações no campo de Galois (GF(2^128)).
    h: Chave hash derivada (16 bytes)
    data: Dados de entrada para autenticação (múltiplo de 16 bytes)
    """
    y = b'\x00' * 16  # Inicializa Y com 16 bytes de zero
    for i in range(0, len(data), 16):
        block = data[i:i+16]
        y = galois_mult(bytes_xor(y, block), h)
    return y

# XOR byte a byte
def bytes_xor(a, b):
    """ Realiza a operação XOR byte a byte entre dois blocos. """
    return bytes(x ^ y for x, y in zip(a, b))

# Multiplicação de dois elementos no campo finito GF(2^128)
def galois_mult(x, y):
    """ Multiplicação de dois elementos no campo GF(2^128). """
    r = 0xe1000000000000000000000000000000  # Polinômio irredutível para GF(2^128)
    z = 0
    v = bytes_to_long(y)
    x = bytes_to_long(x)
    for i in range(128):
        if (x >> (127 - i)) & 1:
            z ^= v
        if v & 1:
            v = (v >> 1) ^ r
        else:
            v >>= 1
    return long_to_bytes(z, 16)

# Função para inicializar o GCM e calcular J_0
def initialize_gcm(iv, key):
    """
    Função que inicializa o AES-GCM e calcula o contador inicial J_0.
    iv: Vetor de inicialização (bytes, geralmente 12 bytes)
    key: Chave AES de 16 bytes
    """
    if len(key) != 16:
        raise ValueError("A chave deve ter exatamente 16 bytes (128 bits).")

    # Passo 1: Deriva o bloco H (GHASH key) usando AES
    h = aes.aes_encrypt([[00, 00, 00, 00], [00, 00, 00, 00], [00, 00, 00, 00], [00, 00, 00, 00]], key, 10)  # H é obtido cifrando 16 bytes de zero

    # Passo 2: Inicializa J_0
    if len(iv) == 12:  # Caso IV tenha 12 bytes
        j0 = iv + b'\x00\x00\x00\x01'  # Concatena 4 bytes finais com valor 1
    else:
        # Caso IV tenha tamanho diferente de 12 bytes, use GHASH
        s = (16 - (len(iv) % 16)) % 16  # Padding para múltiplo de 16 bytes
        padded_iv = iv + b'\x00' * s
        length_block = long_to_bytes(len(iv) * 8, 16)  # Comprimento do IV em bits
        j0 = ghash(h, padded_iv + length_block)

    return j0, h

# Função que cifra o contador J_0 usando o modo AES-CTR
def aes_ctr_encrypt(key, ctr):
    """
    Função que cifra o contador J_0 usando o modo AES-CTR.
    key: Chave AES de 16 bytes (128 bits)
    ctr: Contador J_0 a ser cifrado (16 bytes)
    """
    cipher = AES.new(key, AES.MODE_ECB)  # Usando ECB para cifrar o contador
    return cipher.encrypt(ctr)

# Função que incrementa o contador
def increment_counter(counter):
    """
    Função que incrementa o contador em 1, de acordo com o formato do GCM.
    """
    counter_value = bytes_to_long(counter)
    counter_value += 1  # Incrementa o contador
    return long_to_bytes(counter_value, 16)

# Função que cifra os dados usando AES-GCM
def aes_gcm_encrypt(key, iv, plaintext, aad=b''):
    """
    Função para realizar a cifragem de dados usando AES-GCM.
    key: Chave AES de 16 bytes
    iv: Vetor de inicialização de 12 bytes
    plaintext: Dados a serem cifrados
    aad: Dados adicionais para autenticação (opcional)
    """
    # Inicialização do GCM
    j0, h = initialize_gcm(iv, key)

    # Inicializa o contador com o valor de J_0
    counter = j0
    ciphertext = b''

    # Cifra os dados em blocos de 16 bytes
    for i in range(0, len(plaintext), 16):
        block = plaintext[i:i+16]
        encrypted_ctr = aes_ctr_encrypt(key, counter)
        # Cifra o bloco de dados com o XOR do contador cifrado
        block_cipher = bytes_xor(block, encrypted_ctr[:len(block)])
        ciphertext += block_cipher
        counter = increment_counter(counter)  # Incrementa o contador

    # Cálculo do tag de autenticação (GHASH)
    auth_tag = ghash(h, aad + ciphertext)  # Realiza a autenticação com AAD + dados cifrados

    return ciphertext, auth_tag

# Exemplo de uso
if __name__ == "__main__":
    key = bytes([
        0x00, 0x01, 0x02, 0x03,
        0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0a, 0x0b,
        0x0c, 0x0d, 0x0e, 0x0f
    ])
    # key = b"1234567890abcdef"  # Chave AES de 16 bytes (128 bits)
    iv = b"randomIV123456"     # IV de 12 bytes
    plaintext = b"Texto a ser cifrado com AES-GCM!"  # Dados a cifrar

    # Cifra os dados com AES-GCM
    ciphertext, auth_tag = aes_gcm_encrypt(key, iv, plaintext)

    print("Texto cifrado:", ciphertext.hex())
    print("Tag de autenticação:", auth_tag.hex())

