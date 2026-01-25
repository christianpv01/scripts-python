#Manipulando texto

frase = 'Aprendendo Python utilizando vscode'

#Divisão

#split -> Divide a string em uma lista, separado pelo padrão espaço
print(frase.split())
frasesplit = frase.split()
print(frasesplit[1]) #Mostrando o segundo item da lista
print(frasesplit[1][2]) #Mostrando o terceiro caractere do segundo item da lista 
#join -> Junção
print('-'.join(frasesplit)) #Depois do split
print('_'.join(frase)) #Sem split
