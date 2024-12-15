# Função para transpor a matriz (linhas <-> colunas)
def transpose(matrix):
    """
    Transpõe uma matriz 4x4.
    Exemplo: de linhas para colunas ou vice-versa.
    """
    return [[matrix[row][col] for row in range(4)] for col in range(4)]

# Função para multiplicação no campo GF(2^8)
def galois_multiply(a, b):
    p = 0
    for i in range(8):
        if b & 1:
            p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set:
            a ^= 0x1B
        b >>= 1
    return p & 0xFF

# Matriz inversa do MixColumns no AES
INV_MIX_COLUMNS_MATRIX = [
    [0x0E, 0x0B, 0x0D, 0x09],
    [0x09, 0x0E, 0x0B, 0x0D],
    [0x0D, 0x09, 0x0E, 0x0B],
    [0x0B, 0x0D, 0x09, 0x0E],
]

# Função InvMixColumns corrigida
def inv_mix_columns(state):
    """
    Aplica a operação InvMixColumns em uma matriz state (4x4) organizada por colunas.
    """
    new_state = [[0] * 4 for _ in range(4)]
    for col in range(4):
        for row in range(4):
            value = 0
            for k in range(4):
                value ^= galois_multiply(INV_MIX_COLUMNS_MATRIX[row][k], state[k][col])
            new_state[row][col] = value
    return new_state

# Função principal que organiza a entrada, aplica InvMixColumns e reorganiza a saída
def process_inv_mix_columns(input_state):
    """
    - Transpõe a entrada (linhas -> colunas).
    - Aplica InvMixColumns.
    - Transpõe a saída (colunas -> linhas).
    """
    print("Entrada original:")
    print_matrix(input_state)

    # Transpõe a matriz de linhas para colunas
    transposed_input = transpose(input_state)
    print("Matriz transposta (para colunas):")
    print_matrix(transposed_input)

    # Aplica InvMixColumns
    result = inv_mix_columns(transposed_input)
    print("Matriz após InvMixColumns:")
    print_matrix(result)

    # Transpõe a matriz de volta para o formato original (colunas -> linhas)
    final_result = transpose(result)
    print("Matriz final transposta (de volta para linhas):")
    print_matrix(final_result)

    return final_result

# Função auxiliar para exibir a matriz
def print_matrix(matrix, label="Matriz"):
    print(f"{label}:")
    for row in matrix:
        print(" ".join([hex(byte)[2:].zfill(2) for byte in row]))
    print()

# Entrada original organizada por linhas
input_state = [
    [0xE9, 0xF7, 0x4E, 0xEC],  # Linha 0
    [0x02, 0x30, 0x20, 0xF6],  # Linha 1
    [0x1B, 0xF2, 0xCC, 0xF2],  # Linha 2
    [0x35, 0x3C, 0x21, 0xC7]   # Linha 3
]

# Processa o InvMixColumns com ajuste na entrada e saída
output_state = process_inv_mix_columns(input_state)
