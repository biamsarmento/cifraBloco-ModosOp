import comboComRodada as aes
import gcmPrimeiraWithTag as withTag

def verify_tag_and_decrypt(ciphertext_filename, key, expected_tag):
    """Verifica a tag e decifra o texto se a tag for válida"""
    # Calcule a tag de autenticação a partir do ciphertext e do IV
    tag = withTag.calculate_tag_from_file(ciphertext_filename, key)
    print(f'Tag correta para {ciphertext_filename}: {tag:#034x}')
    # Verifique se a tag gerada corresponde à tag fornecida
    if tag != expected_tag:
        print("Tag inválida! Os dados foram corrompidos ou alterados.")
        return False
    else:
        return True

    # Se a tag for válida, execute a decifra**ção**
    # blocks = blocks_prep(ciphertext_filename)
    # plaintext = aes_decrypt(blocks, iv, key)

print(verify_tag_and_decrypt('RESULTADO_GCM_ERROR.txt', b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f', 0x997cbcfc740a23ab478b67d964a1e414))