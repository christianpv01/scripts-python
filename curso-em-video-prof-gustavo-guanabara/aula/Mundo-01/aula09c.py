#Manipulando texto

frase = 'Aprendendo Python utilizando vscode'

#Transformação

#replase -> Substitui a primeira informação pela segunda
print(frase.replace('Python','Substituir'))
#upper -> Transforma a variavel toda em maiúscula
print(frase.upper())
#lower -> Transforma a variavel toda em minúscula
print(frase.lower())
#capitalize -> Transforma somete a primera letra em maiúscula
print(frase.capitalize())
#title -> Transforma as letras depois do espaço em maiúsculas
print(frase.title())
#stripe -> Remove os espaços inúteis do inicio e do fim, com a eliminação, o primeiro caractere passa a ser o 0 da string
teste = '   Aprendendo Python  '
print(len(teste))
print(teste.strip())
testestrip = teste.strip()
print(len(testestrip))
#rstripe -> Remove os espaços inúteis da direita
print(teste.rstrip())
testerstrip = teste.rstrip()
print(len(testerstrip))
#lstripe -> Remove os espaços inúteis da esquerda
print(teste.lstrip())
testelstrip = teste.lstrip()
print(len(testelstrip))