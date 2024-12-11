# Tabela oficial da S-Box AES 16x16 (para cifragem)
S_BOX = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
]

def pad_pkcs7(text):
    """Aplica padding PKCS#7 para completar 16 bytes."""
    padding_len = 16 - len(text)
    return text + chr(padding_len) * padding_len


def text_to_state(text):
    """Converte um texto para a matriz 4x4 (estado) do AES."""
    state = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(len(text)):
        state[i // 4][i % 4] = ord(text[i])  # Inverter os índices
        
    print("Palavra transformada:", state)
    return state

def print_state(state, label):
    """Imprime o estado formatado."""
    print(f"\n{label}:")
    for row in state:
        print(" ".join(f"{byte:02X}" for byte in row))

def add_round_key(state, round_key):
    """Realiza a operação AddRoundKey com matrizes 4x4."""
    temp = state

    for i in range(4):
        for j in range(4):
            temp[i][j] ^= round_key[i][j]
    
    return temp


def sub_bytes(state):
    """Aplica substituição de bytes usando a S-Box."""

    temp = state

    print("Como o state chega em sub_bytes: ", temp)
    for i in range(4):
        for j in range(4):
            byte = temp[i][j]
            row = (byte >> 4) & 0x0F
            col = byte & 0x0F
            temp[i][j] = S_BOX[row][col]
    
    return temp
    




# def shift_rows(state):
#     """Realiza a operação ShiftRows."""
#     state[1] = state[1][1:] + state[1][:1]
#     state[2] = state[2][2:] + state[2][:2]
#     state[3] = state[3][3:] + state[3][:3]

def shift_rows(state):
    """Realiza a operação ShiftRows respeitando a representação coluna por coluna."""
    # Linha 1: Desloca 1 posição à esquerda
    temp  = state

    temp[0][1], temp[1][1], temp[2][1], temp[3][1] = (
        temp[1][1], temp[2][1], temp[3][1], temp[0][1]
    )

    # Linha 2: Desloca 2 posições à esquerda
    temp[0][2], temp[1][2], temp[2][2], temp[3][2] = (
        temp[2][2], temp[3][2], temp[0][2], temp[1][2]
    )

    # Linha 3: Desloca 3 posições à esquerda
    temp[0][3], temp[1][3], temp[2][3], temp[3][3] = (
        temp[3][3], temp[0][3], temp[1][3], temp[2][3]
    )

    return temp


# Até aqui está certo!

# Nao usamos na ultima
# def mix_columns(state):
#     """Realiza a operação MixColumns (simplificada, sem multiplicações reais)."""
#     for i in range(4):
#         t = state[i][0] ^ state[i][1] ^ state[i][2] ^ state[i][3]
#         u = state[i][0]
#         state[i][0] ^= t ^ state[i][0] ^ state[i][1]
#         state[i][1] ^= t ^ state[i][1] ^ state[i][2]
#         state[i][2] ^= t ^ state[i][2] ^ state[i][3]
#         state[i][3] ^= t ^ state[i][3] ^ u

# def gmul(a, b):
#     """Multiplica dois números no campo finito GF(2^8)."""
#     p = 0
#     for _ in range(8):
#         if b & 1:
#             p ^= a
#         carry = a & 0x80
#         a <<= 1
#         if carry:
#             a ^= 0x1B
#         b >>= 1
#     return p & 0xFF

# def mix_columns(state):
#     """Realiza a operação MixColumns."""
#     for col in range(4):
#         a = state[0][col]
#         b = state[1][col]
#         c = state[2][col]
#         d = state[3][col]

#         state[0][col] = gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1)
#         state[1][col] = gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1)
#         state[2][col] = gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3)
#         state[3][col] = gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2)

# Função para multiplicação por 2 em GF(2^8)
# def xtime(x):
#     return ((x << 1) & 0xFF) ^ (0x1B if (x & 0x80) else 0)

# # Função para multiplicação por 3 em GF(2^8)
# def mul3(x):
#     return xtime(x) ^ x

# # Função para mix_columns
# def mix_columns(state):
#     # A matriz de transformação fixa
#     mix_matrix = [
#         [0x02, 0x03, 0x01, 0x01],
#         [0x01, 0x02, 0x03, 0x01],
#         [0x01, 0x01, 0x02, 0x03],
#         [0x03, 0x01, 0x01, 0x02]
#     ]
    
#     # Criar uma matriz para armazenar os resultados
#     result = [[0] * 4 for _ in range(4)]
    
#     # Realizar a multiplicação das colunas com a matriz de transformação
#     for i in range(4):
#         for j in range(4):
#             result[i][j] = (
#                 mul3(state[i][0]) if mix_matrix[j][0] == 0x02 else state[i][0] ^
#                 mul3(state[i][1]) if mix_matrix[j][1] == 0x03 else state[i][1] ^
#                 mul3(state[i][2]) if mix_matrix[j][2] == 0x02 else state[i][2] ^
#                 mul3(state[i][3]) if mix_matrix[j][3] == 0x02 else state[i][3]
#             ) 
                
#     return result

# Função para multiplicação por 2 em GF(2^8)
def xtime(x):
    return ((x << 1) & 0xFF) ^ (0x1B if (x & 0x80) else 0)

# Função para multiplicação por 3 em GF(2^8)
def mul3(x):
    return xtime(x) ^ x

# Função de MixColumns (corrigida)
def mix_columns(state):

    temp = state
    # Matriz de transformação fixa para MixColumns
    mix_matrix = [
        [0x02, 0x03, 0x01, 0x01],
        [0x01, 0x02, 0x03, 0x01],
        [0x01, 0x01, 0x02, 0x03],
        [0x03, 0x01, 0x01, 0x02]
    ]
    
    # Matriz temporária para armazenar o resultado
    temp_state = [[0] * 4 for _ in range(4)]
    
    # Multiplica e aplica o XOR para cada coluna
    for i in range(4):
        for j in range(4):
            temp_state[i][j] = 0
            for k in range(4):
                if mix_matrix[j][k] == 0x01:
                    temp_state[i][j] ^= temp[i][k]
                elif mix_matrix[j][k] == 0x02:
                    temp_state[i][j] ^= xtime(temp[i][k])
                elif mix_matrix[j][k] == 0x03:
                    temp_state[i][j] ^= mul3(temp[i][k])
    
    # Atualiza o estado com o resultado da operação de MixColumns
    for i in range(4):
        for j in range(4):
            temp[i][j] = temp_state[i][j]
            
    return temp


# Acredito que as chaves estejam sendo geradas corretamente.

def key_expansion(key):
    """Expande a chave para 11 rodadas (AES-128)."""
    # Constantes para AES-128
    Nb = 4  # Número de colunas (32 bits) no estado
    Nk = 4  # Número de palavras (32 bits) na chave original
    Nr = 10  # Número de rodadas
    RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

    # Conversão da chave inicial em palavras (w[0] até w[Nk-1])
    w = []
    for i in range(Nk):
        w.append([key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]])

    # Expansão da chave para (Nr + 1) * Nb palavras
    for i in range(Nk, Nb * (Nr + 1)):
        temp = w[i - 1]  # Última palavra gerada

        # RotWord e SubWord a cada Nk palavras
        if i % Nk == 0:
            # RotWord (circular shift)
            temp = temp[1:] + temp[:1]
            # SubWord (substituição via S-Box)
            temp = [S_BOX[b >> 4][b & 0x0F] for b in temp]
            # XOR com RCON
            temp[0] ^= RCON[(i // Nk) - 1]

        # SubWord para o caso especial de AES-192 ou AES-256 (Nk > 6)
        elif Nk > 6 and i % Nk == 4:
            temp = [S_BOX[b >> 4][b & 0x0F] for b in temp]

        # XOR com a palavra Nk posições antes
        w.append([w[i - Nk][j] ^ temp[j] for j in range(4)])

    # Retorna as chaves expandidas em blocos de 4 palavras (4x4 bytes)
    return [w[i:i + Nb] for i in range(0, len(w), Nb)]

def aes_encrypt(text, key):
    """Executa a cifra AES com o texto e a chave fornecidos."""
    # Aplicar padding
    # text_padding = pad_pkcs7(text)
    # state = text_to_state(text_padding)
    # state = [
    #     [0, 17, 34, 51], 
    #     [68, 85, 102, 119], 
    #     [136, 153, 170, 187], 
    #     [204, 221, 238, 255]
    # ]
    state = text

    # state = [
    #     [0x00, 0x11, 0x22, 0x33], 
    #     [0x44, 0x55, 0x66, 0x77], 
    #     [0x88, 0x99, 0xAA, 0xBB], 
    #     [0xCC, 0xDD, 0xEE, 0xFF]
    # ]

    # state = [
    #     [0x00, 0x44, 0x88, 0xCC],
    #     [0x11, 0x55, 0x99, 0xDD],
    #     [0x22, 0x66, 0xAA, 0xEE],
    #     [0x33, 0x77, 0xBB, 0xFF]
    # ]

    firstAddRoundKey = 0
    afterSubBytes = 0
    afterShiftRows = 0
    afterMixColumns = 0
    afterAddRoundKey = 0

    round_keys = key_expansion(key)  # Corrige o formato das subchaves
    # Testando se a saída corresponde ao esperado
    for i, rk in enumerate(round_keys):
        print(f"Round Key {i}:", rk)

    # print("RoundKeys: ", round_keys)

    # Rodada inicial
    print("State inicial:", state)
    firstAddRoundKey = add_round_key(state, round_keys[0])
    # print("State 0 ", state)

    # 9 rodadas intermediárias
    for i in range(1, 10):
        print(f"round[{i}].start: {firstAddRoundKey}")
        afterSubBytes = sub_bytes(firstAddRoundKey)
        print(f"round[{i}].sub_bytes: {afterSubBytes}")
        afterShiftRows = shift_rows(afterSubBytes)
        print(f"round[{i}].shift_rows: {afterShiftRows}")
        afterMixColumns = mix_columns(afterShiftRows)
        print(f"round[{i}].mix_columns: {afterMixColumns}")
        afterAddRoundKey = add_round_key(afterMixColumns, round_keys[i])
        print(f"round[{i}].add_round_keys: {afterAddRoundKey}")
        # print(f"State {i}", state)

    # Última rodada
    print(f"round[{10}].start: {afterAddRoundKey}")
    afterSubBytes = sub_bytes(afterAddRoundKey)
    print(f"round[{10}].sub_bytes: {afterSubBytes}")
    afterShiftRows = shift_rows(afterSubBytes)
    print(f"round[{10}].shift_rows: {afterShiftRows}")
    afterAddRoundKey = add_round_key(afterShiftRows, round_keys[10])
    print(f"round[{10}].add_round_keys: {afterAddRoundKey}")
    print("State 10 ", afterAddRoundKey)

    return state


def main():
    text = input("Digite uma palavra/frase (máx 16 caracteres): ")
    if len(text) > 16:
        print("Erro: Máximo de 16 caracteres.")
        return

    # Quer dizer Segredo123456789
    # key = bytes([ 
    #     0x53, 0x65, 0x67, 0x72, 
    #     0x65, 0x64, 0x6F, 0x31, 
    #     0x32, 0x33, 0x34, 0x35, 
    #     0x36, 0x37, 0x38, 0x39
    # ])

    # Chave do livro.
    # key = bytes([
    #     0x2b, 0x7e, 0x15, 0x16,
    #     0x28, 0xae, 0xd2, 0xa6,
    #     0xab, 0xf7, 0x15, 0x88,
    #     0x09, 0xcf, 0x4f, 0x3c
    # ])

    key = bytes([
        0x00, 0x01, 0x02, 0x03,
        0x04, 0x05, 0x06, 0x07,
        0x08, 0x09, 0x0a, 0x0b,
        0x0c, 0x0d, 0x0e, 0x0f
    ])


    encrypted_state = aes_encrypt([
        [0x00, 0x11, 0x22, 0x33], 
        [0x44, 0x55, 0x66, 0x77], 
        [0x88, 0x99, 0xAA, 0xBB], 
        [0xCC, 0xDD, 0xEE, 0xFF]
    ], key)
    print_state(encrypted_state, "Texto Cifrado")

if __name__ == "__main__":
    main()





