# Função para multiplicação por 2 em GF(2^8)
def xtime(x):
    return ((x << 1) & 0xFF) ^ (0x1B if (x & 0x80) else 0)

# Funções para multiplicações específicas em GF(2^8)
def mul9(x):
    return xtime(xtime(xtime(x))) ^ x  # x * 9 = (x * 2 * 2 * 2) + x

def mul11(x):
    return xtime(xtime(x)) ^ x ^ xtime(x)  # x * 11 = ((x * 2 * 2) + x) * 2 + x

def mul13(x):
    return xtime(x) ^ x ^ xtime(xtime(x))  # x * 13 = ((x * 2) + x) * 2 * 2 + x

def mul14(x):
    return xtime(x) ^ xtime(xtime(x)) ^ xtime(x)  # x * 14 = ((x * 2) + x) * 2 + x * 2

# Matriz inversa de transformação para Inverse MixColumns
INV_MIX_MATRIX = [
    [0x0e, 0x0b, 0x0d, 0x09],
    [0x09, 0x0e, 0x0b, 0x0d],
    [0x0d, 0x09, 0x0e, 0x0b],
    [0x0b, 0x0d, 0x09, 0x0e]
]

# Função Inverse MixColumns
def inv_mix_columns(state):
    # Criar uma matriz temporária para armazenar o resultado
    temp_state = [[0] * 4 for _ in range(4)]

    # Itera sobre as linhas e colunas da matriz
    for i in range(4):  # Para cada linha
        for j in range(4):  # Para cada coluna
            for k in range(4):  # Para cada elemento na linha da matriz inversa
                byte = state[k][j]
                if INV_MIX_MATRIX[i][k] == 0x09:
                    temp_state[i][j] ^= mul9(byte)
                elif INV_MIX_MATRIX[i][k] == 0x0b:
                    temp_state[i][j] ^= mul11(byte)
                elif INV_MIX_MATRIX[i][k] == 0x0d:
                    temp_state[i][j] ^= mul13(byte)
                elif INV_MIX_MATRIX[i][k] == 0x0e:
                    temp_state[i][j] ^= mul14(byte)

    # Copia o resultado de volta para o estado original
    for i in range(4):
        for j in range(4):
            state[i][j] = temp_state[i][j]

# Dados de entrada no formato 4x4 (4 linhas e 4 colunas)
input_bytes = [
    [0xe9, 0xf7, 0x4e, 0xec], 
    [0x02, 0x30, 0x20, 0xf6], 
    [0x1b, 0xf2, 0xcc, 0xf2], 
    [0x35, 0x3c, 0x21, 0xc7]
]

# A matriz já está no formato 4x4, então podemos usá-la diretamente
input_state = input_bytes  # Não há necessidade de reformatar a entrada

# Aplica Inverse MixColumns
inv_mix_columns(input_state)

# Converte de volta para col-major e depois para uma sequência linear
result_bytes = [input_state[row][col] for row in range(4) for col in range(4)]

# Exibe o resultado em hexadecimal (como sequência contínua)
result_hex = "".join(f"{byte:02x}" for byte in result_bytes)
print("\nResultado final em hexadecimal:", result_hex)
