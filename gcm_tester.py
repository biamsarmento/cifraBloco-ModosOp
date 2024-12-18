import gcm
import gcm_tag
import aes

def main():

    choice = input("Digite 1 para cifrar e 2 para decifrar: ")
    
    caminho_origem = input("\nInsira o caminho do arquivo de origem: ")
    chave = input("\nInsira a chave nesse formato: \n"
                    "00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f\n"
                    "Insira aqui: ")
    iv = input("\nInsira o iv nesse formato: \n"
                    "00 11 22 33 44 55 66 77 88 99 aa bb 00 00 00 00\n"
                    "Insira aqui: ")
    caminho_destino = input("\nInsira o caminho do arquivo de destino: ")
        
    if aes.verificar_formato(chave) == False:
        print("\nFormato inválido! Digite 16 bytes separados por um espaço.")
        return 
    resultado_chave = aes.converter_para_bytes(chave)
    print("\nChave: ", resultado_chave)

    if aes.verificar_formato(iv) == False:
            print("\nFormato inválido! Digite 16 bytes separados por um espaço.")
            return 
    resultado_iv = aes.converter_para_decimais(iv)
    print("\nTexto: ", resultado_iv)

    blocos_preped = gcm.blocks_prep(caminho_origem)
    gcm.gcm(blocos_preped, resultado_chave, resultado_iv, caminho_destino)

    if choice == '1':
        tag = gcm_tag.calculate_tag_from_file(caminho_destino, resultado_chave)
        print("\nA sua tag é: ", tag)
        print("\nSeu resultado está em: ", caminho_destino)

    elif choice == '2':
        tag = input("\nInsira a Tag: ")
        if gcm_tag.verify_tag(caminho_origem, resultado_chave, tag):
             print("Tag é válida!")
        else:
            return
        print("Seu resultado está em: ", caminho_destino)


if __name__ == "__main__":
    main()
