# 5)Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade 
# dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

# 1. passo, realizar o calculo com idade, pegar a idade da pessoa e apresentar em dias.
# 1 ano é igual 365 dias 
idade = 23;
#considerando que todos os messes terão apenas 30 dias o valor de ano será 360
ano = 360;

calculo_de_dias = idade * ano;

print(f"sua idade e {idade} e voce viveu: {calculo_de_dias} dias")
