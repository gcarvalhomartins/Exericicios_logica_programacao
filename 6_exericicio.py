# 6) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos 
# brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total 
# de eleitores.
#
# 1. Primeiro eu tenho que ter o total dos votos 
total_de_votos = 100
votos_brancos = 20
votos_nulos = 25

# 2. Agora eu preciso calcular a porcentagem que equivale de cada tipo de voto.
calculo_total_de_votos = total_de_votos + votos_brancos + votos_nulos
porcentagem_votos_brancos = votos_brancos * 100 / total_de_votos
porcentagem_votos_nulos = votos_nulos * 100 / total_de_votos

print(f"tivemos o total de: {calculo_total_de_votos} votos")
print(f"onde:{porcentagem_votos_brancos:.2f}% foram de votos em branco")
print(f"onde:{porcentagem_votos_nulos:.2f}% foram de votos Nulos")