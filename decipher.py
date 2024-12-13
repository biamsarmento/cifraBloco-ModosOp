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

INV_S_BOX = [
    [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
    [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
    [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
    [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
    [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
    [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
    [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
    [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
    [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
    [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
    [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
    [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
    [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
    [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
    [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]
]

# Funções auxiliares

def format_state_hex(text):
    """Formata o estado como uma matriz 4x4 de valores hexadecimais."""
    return ' '.join(' '.join(f"{byte:02x}" for byte in row) for row in text)

def inv_add_round_key(state, round_key):
    """Realiza a operação AddRoundKey inversa (também XOR com a chave)."""

    temp = state

    for i in range(4):
        for j in range(4):
            temp[i][j] ^= round_key[i][j]
    
    return temp

def inv_sub_bytes(state):
    """
    Aplica a substituição de bytes inversa usando a tabela INV_S_BOX.
    `state` deve ser uma matriz 4x4 de bytes (inteiros de 0 a 255).
    """
    # Cria uma cópia profunda para evitar modificar o estado original.
    temp = [row[:] for row in state]

    print("Como o state chega em inv_sub_bytes: ", temp)
    for i in range(4):
        for j in range(4):
            byte = temp[i][j]
            row = (byte >> 4) & 0x0F  # Obtém os 4 bits mais significativos
            col = byte & 0x0F         # Obtém os 4 bits menos significativos
            temp[i][j] = INV_S_BOX[row][col]  # Substitui usando INV_S_BOX

    return temp


def inv_shift_rows(state):
    """Realiza a operação ShiftRows respeitando a representação coluna por coluna."""
    # Linha 1: Desloca 1 posição à esquerda
    temp  = state

    temp[0][1], temp[1][1], temp[2][1], temp[3][1] = (
        temp[3][1], temp[0][1], temp[1][1], temp[2][1]
    )

    # Linha 2: Desloca 2 posições à direita
    temp[0][2], temp[1][2], temp[2][2], temp[3][2] = (
        temp[2][2], temp[3][2], temp[0][2], temp[1][2]
    )

    # Linha 3: Desloca 3 posições à direita
    temp[0][3], temp[1][3], temp[2][3], temp[3][3] = (
        temp[1][3], temp[2][3], temp[3][3], temp[0][3]
    )

    return temp


# O erro está em mix_columns!

# # Função de InvMixColumns
# def inv_mix_columns(state): 
#     temp = state
#     print("STATE:", state)
#     # Matriz de transformação inversa para InvMixColumns
#     inv_mix_matrix = [
#         [0x0e, 0x0b, 0x0d, 0x09],
#         [0x09, 0x0e, 0x0b, 0x0d],
#         [0x0d, 0x09, 0x0e, 0x0b],
#         [0x0b, 0x0d, 0x09, 0x0e]
#     ]
    
#     # Matriz temporária para armazenar o resultado
#     temp_state = [[0] * 4 for _ in range(4)]
    
#     # Multiplica e aplica o XOR para cada coluna usando a matriz inversa
#     for i in range(4):
#         for j in range(4):
#             temp_state[i][j] = 0
#             for k in range(4):
#                 if inv_mix_matrix[j][k] == 0x09:
#                     temp_state[i][j] ^= mul09(temp[i][k])
#                 elif inv_mix_matrix[j][k] == 0x0b:
#                     temp_state[i][j] ^= mul0b(temp[i][k])
#                 elif inv_mix_matrix[j][k] == 0x0d:
#                     temp_state[i][j] ^= mul0d(temp[i][k])
#                 elif inv_mix_matrix[j][k] == 0x0e:
#                     temp_state[i][j] ^= mul0e(temp[i][k])
    
#     # Atualiza o estado com o resultado da operação de InvMixColumns
#     for i in range(4):
#         for j in range(4):
#             temp[i][j] = temp_state[i][j]
    
#     return temp

# Função para multiplicação por 2 em GF(2^8)
def xtime(x):
    return ((x << 1) & 0xFF) ^ (0x1B if (x & 0x80) else 0)

# Funções para multiplicações específicas em GF(2^8)
def mul0e(x):
    return xtime(xtime(xtime(x))) ^ xtime(xtime(x)) ^ xtime(x)

def mul0b(x):
    return xtime(xtime(xtime(x))) ^ xtime(x) ^ x

def mul0d(x):
    return xtime(xtime(xtime(x))) ^ xtime(xtime(x)) ^ x

def mul09(x):
    return xtime(xtime(xtime(x))) ^ x

# Função InvMixColumns
# Função de InvMixColumns
def inv_mix_columns(state):
    temp = state
    # Matriz inversa de transformação para InvMixColumns
    inv_mix_matrix = [
        [0x0e, 0x0b, 0x0d, 0x09],
        [0x09, 0x0e, 0x0b, 0x0d],
        [0x0d, 0x09, 0x0e, 0x0b],
        [0x0b, 0x0d, 0x09, 0x0e]
    ]
    
    # Matriz temporária para armazenar o resultado
    temp_state = [[0] * 4 for _ in range(4)]
    
    # Multiplica e aplica o XOR para cada coluna usando a matriz inversa
    for col in range(4):
        for row in range(4):
            temp_state[row][col] = 0
            for k in range(4):
                if inv_mix_matrix[row][k] == 0x09:
                    temp_state[row][col] ^= mul09(temp[k][col])
                elif inv_mix_matrix[row][k] == 0x0b:
                    temp_state[row][col] ^= mul0b(temp[k][col])
                elif inv_mix_matrix[row][k] == 0x0d:
                    temp_state[row][col] ^= mul0d(temp[k][col])
                elif inv_mix_matrix[row][k] == 0x0e:
                    temp_state[row][col] ^= mul0e(temp[k][col])
    
    # Atualiza o estado com o resultado da operação de InvMixColumns
    for i in range(4):
        for j in range(4):
            temp[i][j] = temp_state[i][j]
    
    return temp

# Reformatar entrada e saída
def format_input_output(input_bytes, to_columns=True):
    if to_columns:  # Converter bytes em formato col-major para matriz 4x4
        return [[input_bytes[i + 4 * j] for i in range(4)] for j in range(4)]
    else:  # Converter matriz 4x4 de volta para formato col-major
        return [input_bytes[row][col] for col in range(4) for row in range(4)]


def inv_key_expansion(key):
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

    # Agrupa as chaves expandidas em blocos de 4 palavras (4x4 bytes)
    expanded_keys = [w[i:i + Nb] for i in range(0, len(w), Nb)]

    # Retorna as chaves na ordem inversa
    return expanded_keys[::-1]

def text_to_state(text):
    """Converte um texto para uma matriz 4x4 (estado) do AES."""
    state = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(len(text)):
        row = i % 4
        col = i // 4
        state[row][col] = ord(text[i])
    return state

# def aes_decrypt(ciphertext, key):
#     """Descriptografa o texto cifrado usando a chave fornecida."""
#     # state = text_to_state(ciphertext)
#     round_keys = inv_key_expansion(key)

#     for i, rk in enumerate(round_keys):
#         print(f"Round Key {i}:", rk)

#     state = ciphertext
    
#     # 10 rounds de descriptografia
#     print("State 0: ", state)
#     state = inv_add_round_key(state, round_keys[0])
    
#     for i in range(1, 10):
#         print(f"round[{i}].start: {state}")
#         state = inv_sub_bytes(state)
#         print(f"round[{i}].inv.sub_bytes: {state}")
#         state = inv_shift_rows(state)
#         print(f"round[{i}].inv.shift_rows: {state}")
#         if i < 10:
#             state = inv_mix_columns(state)
#             print(f"round[{i}].inv.mix.columns: {state}")
#         state = inv_add_round_key(state, round_keys[i])
#         print(f"round[{i}].inv.add_round_keys: {state}")
    
#     return state

def aes_decrypt(ciphertext, key):
    """Descriptografa o texto cifrado usando a chave fornecida."""
    round_keys = inv_key_expansion(key)

    for i, rk in enumerate(round_keys):
        print(f"Round Key {i}:", format_state_hex(rk))

    state = ciphertext

    # Etapa inicial: Adiciona a chave da última rodada
    print("State 0: ", format_state_hex(state))
    state = inv_add_round_key(state, round_keys[0])

    # Rodadas principais (Nr-1 rodadas)
    for round in range(1, 10):
        print(f"round[{round}].start: {format_state_hex(state)}")
        state = inv_shift_rows(state)
        print(f"round[{round}].inv.shift_rows: {format_state_hex(state)}")
        state = inv_sub_bytes(state)
        print(f"round[{round}].inv.sub_bytes: {format_state_hex(state)}")
        state = inv_add_round_key(state, round_keys[round])
        print(f"round[{round}].inv.add_round_keys: {format_state_hex(state)}")
        state = inv_mix_columns(state)
        print(f"round[{round}].inv.mix.columns: {format_state_hex(state)}")

    # Rodada final (sem InvMixColumns)
    state = inv_shift_rows(state)
    print("Final round.inv.shift_rows: ", format_state_hex(state))
    state = inv_sub_bytes(state)
    print("Final round.inv.sub_bytes: ", format_state_hex(state))
    state = inv_add_round_key(state, round_keys[0])
    print("Final round.inv.add_round_keys: ", format_state_hex(state))

    return state


# Exemplo de uso
ciphertext = [
        [0x69, 0xC4, 0xE0, 0xD8], 
        [0x6A, 0x7B, 0x04, 0x30], 
        [0xD8, 0xCD, 0xB7, 0x80], 
        [0x70, 0xB4, 0xC5, 0x5A]
    ]

key = bytes([
    0x00, 0x01, 0x02, 0x03,
    0x04, 0x05, 0x06, 0x07,
    0x08, 0x09, 0x0a, 0x0b,
    0x0c, 0x0d, 0x0e, 0x0f
])

plaintext = aes_decrypt(ciphertext, key)
print("Texto Decifrado: ", plaintext)

# print("Texto Decifrado:", ''.join(chr(x) for row in plaintext for x in row))
