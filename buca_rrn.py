# constantes globais
SIZEOF_REG = 64
SIZEOF_CAB = 4

''' Função principal '''
def main() -> None:
    try:
        nomeArq = input('Digite o nome do arquivo a ser aberto: ')
        arq = open(nomeArq, 'rb')

        cab = arq.read(SIZEOF_CAB)
        total_reg = int.from_bytes(cab)

        rrn = int(input('digite o rrn: '))
        #continue a implementaçao
        if rrn >= total_reg:
            print('erro, valor invalido')
            return
        offset = rrn * SIZEOF_REG + SIZEOF_CAB
        arq.seek(offset)
        buffer = arq.read(SIZEOF_REG).decode()

        buffer = buffer.rstrip('\0')
        buffer = ''
        contaCampo = 1
        for campo in buffer.split(sep='|'):
            if campo:
                print(f"Campo #{contaCampo}: {campo} - {len(campo)}")
                contaCampo += 1
        print()
        arq.close()
    except OSError as e:
        print(f'Erro main: {e}')
    

if __name__ == '__main__':
    main()