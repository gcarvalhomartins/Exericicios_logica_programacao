# 3) Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor.
# entendimento do problema, quando eu digitar a letra D, ele irá aparecer a letra C. 
#
# 1. passo, preciso de uma lista de todas as teclas
lista_de_teclas = ["A", "B", "C", "D", "E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# 2. adiciono um input para o usuário digitar.

#input("digite a tecla que procura ")

# 3. pegar a tecla que esse usuário digitou

# 3.1 coloquei uma variavel pra testar a lista
letra = "H"

# 4. verificar na lista se ela existe
if letra in lista_de_teclas:
    indice_letra = lista_de_teclas.index(letra) # crirar variavel para informar que o index da lista, será letra
    
# 5. se ela existir, aparece o antessesor dela
    if indice_letra > 0:
        antecessor = lista_de_teclas[indice_letra - 1]
        print(f"o antecessor de {letra} é {antecessor}")
    else:
        print(f"{letra} não tem antecessores na lista")

# 6. se ela não existir, aparecer mensagem, sorry, não temos isso. 
else:
    print(f"desculpe não temos essa {letra} na lista")

