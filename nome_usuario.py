# Solicita o nome completo do usuário
nome = input("Digite seu nome completo: ")

# Define quais letras são vogais (minúsculas e maiúsculas)
vogais = "aeiouAEIOU"

# Conta a quantidade de vogais no nome
quantidade_vogais = 0
for letra in nome:
    if letra in vogais:
        quantidade_vogais = quantidade_vogais + 1

# Pega as 3 primeiras letras do nome
tres_primeiras = nome[0:3]

# Substitui todas as vogais pelo caractere *
nome_sem_vogais = ""
for letra in nome:
    if letra in vogais:
        nome_sem_vogais = nome_sem_vogais + "*"
    else:
        nome_sem_vogais = nome_sem_vogais + letra

# Exibe os resultados
print()
print("Quantidade de vogais no nome:", quantidade_vogais)
print("As 3 primeiras letras do nome:", tres_primeiras)
print("Nome com vogais substituídas por *:", nome_sem_vogais)
