''' A lista mensagens contém as strings que serão usadas pela função
    input na leitura dos campos '''
mensagens: str = [
    '                                   Nome: ',
    '                               Endereco: ',
    '                                 Cidade: ',
    '                                 Estado: ',
    '                                    CEP: '
]

''' Função auxiliar que concatena o campo no buffer junto com o | '''
def concatena_campo(buffer: str, campo: str) -> str:
    return buffer + campo + '|'
    
''' Função principal '''
def main() -> None:
    try:
        nomeArq = input('Digite o nome do arquivo a ser criado: ')
        arq = open(nomeArq, 'wb')
        campo = input('Digite o sobrenome ou <ENTER> para sair: ')
        while campo:
            buffer = ''
            buffer = concatena_campo(buffer, campo.capitalize())
            for m in mensagens:
                campo = input(m)
                buffer = concatena_campo(buffer, campo)
            # caracteres especiais vão ocupar mais de um byte depois de decodificados, 
            # por isso precisa decodificar a string antes de calcular o tamanho 
            buffer = buffer.encode()
            lenBuffer = len(buffer)
            arq.write(lenBuffer.to_bytes(2))
            arq.write(buffer)
            campo = input('Digite o sobrenome ou <ENTER> para sair: ')
        arq.close()
    # OSError é a classe geral de erros que podem ocorrer na manipulação do arquivo
    except OSError as e:
        print(f'Erro main: {e}')
    

if __name__ == '__main__':
    main()