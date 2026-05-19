'''Exercício Python 115a: Vamos criar um menu em Python, usando modularização.'''

from utilidadescev.interface import *
from utilidadescev.dado import *
from utilidadescev.arquivo import *
from time import sleep

arq = r'C:\Users\chris\Desktop\scripts-python\curso-em-video-prof-gustavo-guanabara\desafio\Resolvidos\desafio-115b\cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
        
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho("NOVO CADASTRO")
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)