#8) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do 
# distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor 
# seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, 
# calcular e escrever o custo final ao consumidor.
#
# Fatores
#  1.soma do custo de fábrica, com a porcentagem do distribuidor(aplicado ao custo de fábrica) e impostos.
#  2.distribuidor = 28% 
#  3.impostos = 45%
#
# o que ele quer ?
# um algoritimo para ler o custo de fábrica de um carro, calcular oe escrever o valor final pro consumidor
# ou seja, se um carro a custo de fábrica custa 10.000, 10.000 + 28% do vendedor + 45% de impostos.

# resolução
 
# 1.temos os valores fixos de impostos e distribuidor. 
distribuidor = 28.00
imposto = 45.00

# custo de fabrica
value_car_fabric = 10000

#converter porcentagens para decimais
distribuidor_decimal = distribuidor /100
imposto_decimal = imposto / 100

#calculo
custo_final_consumer = value_car_fabric + (value_car_fabric * distribuidor_decimal) + (value_car_fabric * imposto_decimal)
print(f"o valor total do carro é:{custo_final_consumer}")


"""