nome = str(input('Qual é o seu nome? '))
idade = int(input('Quantos anos você tem? '))
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
print('Bem-vindo ',nome)
print('----------------------------')
print('    Verificador de IMC')
print('----------------------------')
imc = float(peso/(altura*altura))
print('IMC:',imc)
if imc<18.5 :
    print('Você está abaixo do peso ideal')
elif imc>=18.5 and imc<25 :
    print('Você está no peso ideal')
elif imc>=25 and imc<30 :
    print('Você está com sobrepeso')
else :
    print('Você está obeso')
