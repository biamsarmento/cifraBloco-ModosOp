import aes
import imagem
import hashlib
import ecb

caminho_imagem_antes_txt = 'selfieD_antes.txt'
caminho_imagem_depois_txt = 'selfieD_depois.txt'
caminho_blocos_encrypted_txt = 'selfieD_encrypt.txt'
caminho_blocos_decrypted_txt = 'selfieD_decrypt.txt'
caminhoImagemRec = 'selfieD_recuperada.jpeg'

# Função para calcular o hash de uma imagem em hexadecimal
def calcular_hash(hex_string):
    return hashlib.sha256(hex_string.encode('utf-8')).hexdigest()

def test_aes_ecb_with_rounds(caminho_selfie, chave):
    # Converte a chave para bytes
    if not aes.verificar_formato(chave):
        raise ValueError("Formato inválido de chave. Digite 16 bytes separados por um espaço.")
    
    resultadoChave = aes.converter_para_bytes(chave)

    # Converte a selfie para hexadecimal
    hex_string = imagem.imagem_para_hex(caminho_selfie)
    imagem.salvar_hex_em_txt(hex_string, caminho_imagem_antes_txt)

    # Prepara os blocos
    blocos = ecb.blocks_prep(caminho_imagem_antes_txt)

    # Lista de número de rodadas a ser testada
    rodadas = [1, 5, 9, 13]

    for rounds in rodadas:
        # Cifra os blocos no modo ECB
        blocos_encrypted = ecb.ecb_cipher(blocos, resultadoChave, rounds)

        # Salva o resultado da cifragem em um arquivo
        caminho_saida_hex = f"selfie_encrypt_{rounds}_rounds.txt"
        with open(caminho_saida_hex, 'w') as file:
            file.write('\n'.join(blocos_encrypted))

        # Unprep dos blocos e converte para imagem
        caminho_saida_processada = f"selfie_encrypt_processada_{rounds}.txt"
        ecb.blocks_unprep(caminho_saida_hex, caminho_saida_processada)

        with open(caminho_saida_processada, 'r') as file:
            hex_string_lido = file.read()

        caminho_imagem_cifrada = f"selfie_cifrada_{rounds}_rounds.jpeg"
        imagem.hex_para_imagem(hex_string_lido, caminho_imagem_cifrada)

        # Calcula o hash da imagem cifrada
        hash_imagem = calcular_hash(hex_string_lido)

        print(f"Rodadas: {rounds}")
        print(f"Imagem cifrada salva em: {caminho_imagem_cifrada}")
        print(f"Hash da imagem cifrada: {hash_imagem}\n")

# Exemplo de execução da função test_aes_ecb_with_rounds
if __name__ == "__main__":
    chave = input("\nInsira a chave nesse formato: \n"
                  "00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f\n"
                  "Insira aqui: ")

    caminho_selfie = input("\nInsira o caminho da imagem (selfie): ")

    test_aes_ecb_with_rounds(caminho_selfie, chave)
