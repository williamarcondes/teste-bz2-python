import bz2

def comprimir_arquivo(nome_arquivo, nome_arquivo_comprimido):
    with open(nome_arquivo, 'rb') as arquivo:
        with bz2.open(nome_arquivo_comprimido, 'wb') as arquivo_comprimido:
            arquivo_comprimido.writelines(arquivo)

    print(f'O arquivo {nome_arquivo} foi comprimido com sucesso para {nome_arquivo_comprimido}.')

def descomprimir_arquivo(nome_arquivo_comprimido, nome_arquivo_descomprimido):
    with bz2.open(nome_arquivo_comprimido, 'rb') as arquivo_comprimido:
        with open(nome_arquivo_descomprimido, 'wb') as arquivo_descomprimido:
            for linha in arquivo_comprimido:
                arquivo_descomprimido.write(linha)

    print(f'O arquivo {nome_arquivo_comprimido} foi descomprimido com sucesso para {nome_arquivo_descomprimido}.')

# Exemplo de uso
arquivo_origem = 'exemplo.txt'
arquivo_comprimido = 'exemplo.txt.bz2'
arquivo_descomprimido = 'exemplo_descomprimido.txt'

comprimir_arquivo(arquivo_origem, arquivo_comprimido)
descomprimir_arquivo(arquivo_comprimido, arquivo_descomprimido)
