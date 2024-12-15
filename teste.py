# Função para multiplicação no campo GF(2^8)
def galois_multiply(a, b):
    p = 0
    for i in range(8):
        if b & 1:  # Verifica se o bit menos significativo de b está setado
            p ^= a  # XOR com a
        hi_bit_set = a & 0x80  # Verifica o bit mais significativo
        a <<= 1  # Desloca para a esquerda
        if hi_bit_set:
            a ^= 0x1B  # Aplica a redução com o polinômio irreducível AES
        b >>= 1  # Desloca b para a direita
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
    Aplica a operação InvMixColumns em uma matriz state (4x4).
    A matriz state é organizada por colunas.
    """
    new_state = [[0] * 4 for _ in range(4)]  # Inicializa a nova matriz
    
    # Processa cada coluna individualmente
    for col in range(4):
        print(f"Processando coluna {col}:")
        for row in range(4):
            value = 0
            # Multiplica cada elemento da matriz inversa pelos elementos da coluna
            for k in range(4):
                product = galois_multiply(INV_MIX_COLUMNS_MATRIX[row][k], state[k][col])
                print(f"  Multiplica inv_matrix[{row}][{k}]={hex(INV_MIX_COLUMNS_MATRIX[row][k])} "
                      f"por state[{k}][{col}]={hex(state[k][col])} => {hex(product)}")
                value ^= product  # Aplica o XOR
            new_state[row][col] = value
            print(f"  Resultado new_state[{row}][{col}] = {hex(value)}")
    return new_state

# Função auxiliar para exibir a matriz
def print_matrix(matrix, label):
    print(f"{label}:")
    for row in matrix:
        print(" ".join([hex(byte)[2:].zfill(2) for byte in row]))
    print()

# Entrada correta (por colunas)
state = [
    [0xe9, 0x02, 0x1b, 0x35],  # Coluna 0
    [0xf7, 0x30, 0xf2, 0x3c],  # Coluna 1
    [0x4e, 0x20, 0xcc, 0x21],  # Coluna 2
    [0xec, 0xf6, 0xf2, 0xc7],  # Coluna 3
]

# Executa o InvMixColumns
print_matrix(state, "Matriz de entrada (state)")
result = inv_mix_columns(state)
print_matrix(result, "Matriz resultante após InvMixColumns")
