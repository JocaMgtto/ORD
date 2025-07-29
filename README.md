Módulo de Geração de Arquivo de Dados
Este script em Python é a primeira parte de um sistema de manipulação de dados. Sua função é criar um arquivo binário contendo registros de tamanho variável, com base nas informações fornecidas interativamente pelo usuário.

Ele serve como a ferramenta de entrada e escrita de dados, preparando o arquivo para ser lido e processado por um módulo complementar.

Descrição do Projeto
O programa solicita ao usuário um nome para o arquivo a ser criado. Em seguida, entra em um loop para coletar dados de múltiplos registros, que incluem sobrenome, nome, endereço, cidade, estado e CEP. Cada registro completo é então formatado e gravado no arquivo binário.

A principal característica técnica deste módulo é a implementação do método de armazenamento de Registros de Comprimento Variável com Indicador de Tamanho.

Formato do Arquivo
O arquivo gerado por este script tem uma estrutura bem definida, crucial para a sua leitura posterior.

Cada registro dentro do arquivo é composto por duas partes:

Indicador de Tamanho (Cabeçalho): Um inteiro de 2 bytes que armazena o tamanho exato (em bytes) do bloco de dados que o sucede.

Bloco de Dados: Os dados do registro propriamente ditos, formatados como uma única string e codificados em bytes.

A estrutura de cada registro é:
[TAMANHO (2 bytes)] [DADOS (N bytes)]

Estrutura do Bloco de Dados
O bloco de dados ([DADOS]) é uma string onde os campos são concatenados e separados pelo caractere pipe (|). A ordem dos campos é:

Sobrenome|Nome|Endereco|Cidade|Estado|CEP|

O script abre um arquivo em modo de escrita binária ('wb').

Um loop while controla a entrada de novos registros.

Para cada registro, os campos são lidos via input() e concatenados em um buffer com | como separador.

A string do buffer é codificada para bytes (ex: UTF-8) para calcular seu tamanho real.

O tamanho do buffer em bytes é escrito no arquivo como um inteiro de 2 bytes.

Imediatamente após o tamanho, o buffer de dados (já em bytes) é escrito no arquivo.

O processo se repete até que o usuário decida sair.

Módulo de Leitura e Busca em Arquivo de Dados
Este script em Python é a segunda parte de um sistema de manipulação de dados. Sua função é ler um arquivo binário, gerado pelo gerador.py, e realizar uma busca sequencial por um registro específico, utilizando o sobrenome como chave de busca.

Ele serve como a ferramenta de leitura e consulta dos dados, demonstrando como interpretar a estrutura de arquivo personalizada que foi criada.

Descrição do Projeto
O programa solicita ao usuário o nome do arquivo de dados que deseja abrir. Em seguida, pede um sobrenome para ser utilizado como chave de busca. O script então percorre o arquivo, lendo um registro de cada vez, até encontrar um que corresponda à chave ou até chegar ao final do arquivo.

Se o registro for encontrado, seus campos são exibidos de forma formatada. Caso contrário, uma mensagem informa que a busca não teve sucesso.

Como Funciona
A lógica de leitura e busca se baseia estritamente no formato de arquivo definido pelo script de geração:

Abertura do Arquivo: O programa abre o arquivo de dados especificado em modo de leitura binária ('rb').

Busca Sequencial: O método de busca implementado é o sequencial. O script lê cada registro desde o início do arquivo até encontrar o que procura ou atingir o fim do arquivo.

Leitura de Registro (leia_reg):

Primeiro, a função lê os 2 bytes do cabeçalho para determinar o tamanho do registro.

Em seguida, ela lê o número exato de bytes correspondente a esse tamanho, obtendo o bloco de dados do registro.

Os bytes lidos são decodificados de volta para uma string.

Verificação da Chave:

A string do registro é dividida usando o caractere pipe (|) como separador.

O primeiro campo (o sobrenome) é comparado com a chave de busca fornecida pelo usuário.

Exibição do Resultado:

Se houver uma correspondência, o loop de busca é interrompido e todos os campos do registro encontrado são impressos na tela.

Se o fim do arquivo for alcançado sem uma correspondência, o programa informa que o registro não foi encontrado.

terceiro codigo: busca_rrn.py

Leitor de Arquivo com Registros de Tamanho Fixo
Este script Python demonstra o método de acesso direto a registros por RRN (Número Relativo de Registro) em um arquivo binário. Diferente dos métodos anteriores que usavam registros de tamanho variável, este programa opera sobre um arquivo onde todos os registros possuem um tamanho fixo, permitindo o cálculo e o acesso imediato a qualquer registro.

Descrição do Projeto
O objetivo do programa é ler um registro específico de um arquivo de dados sem a necessidade de percorrer o arquivo sequencialmente. O usuário fornece o nome do arquivo e o RRN (índice) do registro desejado. O script então calcula a posição exata (offset) do registro no arquivo, salta diretamente para essa posição e lê os dados, exibindo seus campos.

Esta abordagem é extremamente eficiente para situações onde a posição do registro é conhecida ou pode ser facilmente calculada.

Formato do Arquivo
Para que este script funcione, ele espera que o arquivo de dados tenha a seguinte estrutura de Registros de Tamanho Fixo:

Cabeçalho (4 bytes): Os primeiros 4 bytes do arquivo contêm um único número inteiro que indica o número total de registros presentes no arquivo.

Área de Dados: Após o cabeçalho, seguem-se os registros, um após o outro.

Cada registro ocupa um espaço fixo de 64 bytes.

Dentro de cada registro de 64 bytes, os dados são armazenados como uma string com campos separados pelo caractere pipe (|).

O espaço não utilizado dentro de um registro é preenchido com um caractere de padding (neste caso, o caractere nulo \0).

Como Funciona
O script lê o cabeçalho de 4 bytes para saber quantos registros existem no total e para validar a entrada do usuário.

A posição exata do registro no arquivo é calculada com a fórmula de acesso direto:
posição = (RRN * tamanho_do_registro) + tamanho_do_cabeçalho
posição = (rrn * 64) + 4

A função arq.seek() é usada para mover o ponteiro de leitura do arquivo diretamente para a posição calculada, sem ler os dados anteriores.

O script lê exatamente 64 bytes (o tamanho de um registro).

Os caracteres de padding (\0) são removidos do final da string lida.

A string é dividida pelo caractere | para extrair e exibir os campos individuais.
