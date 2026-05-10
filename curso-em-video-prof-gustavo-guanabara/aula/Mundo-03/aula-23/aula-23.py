'''
Curso Python #23 - Tratamento de Erros e Exceções
Nessa aula, vamos ver como o Python permite tratar erros e criar respostas a essas exceções. Aprenda como usar a estrutura try except no Python de uma forma simples.

Python Exceptions - https://docs.python.org/3/library/exceptions.html

Comandos
try: <- tentar
    Operação
except: <- caso de erro / Pode conter mais de 1 except dentro do try
    Falhou
else: <- se o try foi válido, vai executar
    deu certo  
finally:
    certo/falha
'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
   print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado!')