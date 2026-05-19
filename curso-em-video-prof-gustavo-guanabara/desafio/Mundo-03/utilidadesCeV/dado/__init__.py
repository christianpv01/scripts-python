def leiaDinheiro(msg):
    valor = 0
    while True:
        n = str(input(msg)).strip().replace(',','.')
        try:
            valor = float(n)
            return valor
        except ValueError:
            print('\033[0;31mERRO! "' + n + '" não é um valor monetário válido.\033[m')

def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg)).strip().replace(',','.')
        try:
            valor = int(n)
            return valor
        except ValueError:
            print('\033[0;31mERRO! "' + n + '" não é um número inteiro válido.\033[m')

def leiaFloat(msg):
    valor = 0.0
    while True:
        n = str(input(msg)).strip().replace(',','.')
        try:
            valor = float(n)
            return valor
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não informar algum número.\033[m')
        except ValueError:
            print('\033[0;31mERRO! "' + n + '" não é um número flaot válido.\033[m')

def leiaStr(msg):
    valor = 0
    while True:
        n = str(input(msg)).title()
        validacao = n.strip().replace(' ','')
        if validacao.isalpha():
            valor = n
            return valor
        else:
            print(f'\033[0;31mERRO! "{n}" não é um nome válido.\033[m')

def verificarSite(url):
    import requests
    try:
        resposta = requests.get(url, timeout=3)
        if resposta.status_code == 200:
            print(f'\033[0;32mO site {url} está online!\033[m')
        else:
            print(f'O site {url} retornou o status: {resposta.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'O site {url} está offline ou inacessível. Erro: {e}')

def ListaCadastro():
    caminho = r'C:\Users\chris\Desktop\scripts-python\curso-em-video-prof-gustavo-guanabara\desafio\Mundo-03\utilidadesCeV\lista.txt'
    arquivo = open(caminho,'a')
    nome = leiaStr('Digite um nome: ')
    idade = leiaInt('Digite uma idade: ')
    arquivo.write(f'{nome};{idade}\n')
    print(f'O cadastro de {nome} foi realizado com sucesso.')
    arquivo.close()

def ListaCompleta():
    caminho = r'C:\Users\chris\Desktop\scripts-python\curso-em-video-prof-gustavo-guanabara\desafio\Mundo-03\utilidadesCeV\lista.txt'
    arquivo = open(caminho, 'r')
    titulos('PESSOAS CADASTRADAS')
    for linha in arquivo:
        dados = linha.split(';')

        nome = dados[0] 
        idade = dados[1].strip()

        print(f'{nome:<35} \t{idade:>3} anos')

    arquivo.close()

def titulos(msg):
    print(f'{'-'*50}\n{msg:^50}\n{'-'*50}')

def cadastro():   
    while True:
        titulos('MENU PRINCIPAL')
        print(f'\033[0;33m{'1':<3}\033[m-  \033[1;34;47m{'Cadastrar Nova Pessoa':^23}\033[m\n\033[0;33m{'2':<3}\033[m-  \033[1;34;47m{'Lista Completa':^23}\033[m\n\033[0;33m{'3':<3}\033[m-  \033[1;34;47m{'Sair do Sistema':^23}\033[m')
        print('-'*50)
        opcao = leiaInt('Escolha uma opção: ')
        if opcao == 1:
            ListaCadastro()
        elif opcao == 2:
            ListaCompleta()
        elif opcao == 3:
            print(' >>> Finalizando o programa.\n >>> Volte sempre!')
            break
        else:
            print('\033[0;31mERRO! Você deve selecionar uma opção válida.\033[m')
