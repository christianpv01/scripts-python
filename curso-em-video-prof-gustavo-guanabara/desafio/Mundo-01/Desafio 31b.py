distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
#preço = distância * 0.50 if distância <= 200 else distância * 0.45 - Condição Simplificada
print('E o preço da sua passagem serpa de R${:.2f}'.format(preço))