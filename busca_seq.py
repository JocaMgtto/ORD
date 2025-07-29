''' Função auxiliar que lê registros no formato gerado pelo escreve_registros.py'''
def leia_reg(arq) -> str:
    try:
        arq.seek(4)
        tam = int.from_bytes(arq.read(2))
        
        if tam > 0:
            s = arq.read(tam)
            return s.decode()
    except OSError as e:
        print(f'Erro leia_reg: {e}')
    return ''


''' Função principal '''
def main() -> None:
    try:
        nomeArq = input('Digite o nome do arquivo a ser aberto: ')
        arq = open(nomeArq, 'rb')
    except FileNotFoundError as e:
        print(f'Erro main: {e}')
    else:
        
        chave = input('Digite o sobrenome a ser buscado: ').capitalize() 
        arq.seek(6)
        achou = False
        buffer = leia_reg(arq)
        while buffer and not achou:
            sobrenome = buffer.split(sep='|')[0]

            if sobrenome == chave:
                achou = True
            else:
                buffer = leia_reg(arq)
        
        if achou:
            contaCampo = 1
            for campo in buffer.split(sep='|'):
                if campo:
                    print(f"campo #{contaCampo}: {campo}")
                    contaCampo +=1
        else: 
            print(f"o registro de sobrenome {chave} nao foi encontrado")

        print()
        arq.close()
    

if __name__ == '__main__':
    main()