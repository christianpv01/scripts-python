# Faça o programa de uma sorveteria, onde o usuário pode escolher:
# Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
# Sabor do sorvete: morango, creme, chocolate
# Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
# Apresente o valor a ser pago

# %%

tipo_sorvete = {
    'casquinha':1.00,
    'cascão':2.50,
    'cestinha':4.00    
}

sabor_sorvete = ['morango','creme','chocolate']

cobertura_sorvete = {
    'caramelo':1.50,
    'morango':1.50,
    'chocolate':1.50,
    'sem cobertura':0.00
}

escolha_tipo = input(f'{' TIPO ':-^15}\n>> Casquinha\n>> Cascão\n>> Cestinha\nEscolha: ').lower()
escolha_sabor = input(f'{' SABOR ':-^15}\n>> Morango\n>> Creme\n>> Chocolate\nEscolha: ').lower()
escolha_cobertura = input(f'{' COBERTURA ':-^15}\n>> Caramelo\n>> Morango\n>> Chocolate\n>> Sem Cobertura\nEscolha: ').lower()
print(f'O sabor escolhido foi {escolha_sabor} com a opção de cobertura {escolha_cobertura} e o valor do sorvete ficou em R$ {tipo_sorvete[escolha_tipo]+cobertura_sorvete[escolha_cobertura]:.2f}')