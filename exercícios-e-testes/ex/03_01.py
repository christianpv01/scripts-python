# Faça um programa que conta quantas vezes a letra 'a' aparece em uma palavra

frase = input('Escreva uma frase: ').lower()

print(f'A frase "{frase.capitalize()}" contém {frase.count('a')} letras "A".')

# Utilizando laço
count = 0
for i in range(len(frase)):
    if frase[i] == 'a':
        count += 1
print(f'A frase "{frase.capitalize()}" contém {count} letras "A".')

count1 = 0
for letra in frase:
    if letra == 'a':
        count1 += 1
print(f'A frase "{frase.capitalize()}" contém {count1} letras "A".')

count2 = 0
for letra in frase:
    count2 += letra == 'a'
        
print(f'A frase "{frase.capitalize()}" contém {count2} letras "A".')
