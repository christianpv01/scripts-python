#Manipulando texto

frase = 'Aprendendo Python utilizando vscode'

#Analise

#len -> Mostra a quantidade de caracteres da string 
print(len(frase))
#count -> Mostra a quantidade da letra
print(frase.count('o')) #Conta os 'o' tem dentro de frase
print(frase.count('o',0,16)) #Conta os 'o' dentro da range 0 e 16
#find -> Procura o string dentro da variavel
print(frase.find('den'))
print(frase.find('Teste')) #Como não existe dentro da string, retorna -1
print('Python' in frase) #Verifica se existe dentro da string, retornando True e False