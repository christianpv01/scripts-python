#Manipulando texto

frase = 'Aprendendo Python utilizando vscode'

#Fatiamento

print(frase[0])
print(frase[11:17]) #Onde o inicial começa no caracter correto e o final precisamos adicionar +1 pois não considera o caracter final
print(frase[11:17:2])
# primeiro é o inicial, segundo é o 'até' e terceiro é o passo
print(frase[:10]) #Sem valor do inicial, escreve todos os caracteres anteriores
print(frase[11:]) #Sem valor do final, escreva todos os caracteres após o inicial
print(frase[11::3]) #Declara o inicial, considera até o final, mas com passo de 3 em 3
print(frase[::2]) #Declarando somente o passo, pula de acordo com o valor
