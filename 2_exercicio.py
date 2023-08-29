#2) Os pares de instruções abaixo produzem o mesmo resultado?


a = (4/2) + (2/4)
a2 = 4/2 + 2/4

print(a,a2)
#resultado 2.5, são iguais

b = 4/(2+2)/4
b2 = 4/2 + 2/4

print(b,b2)
#resultado 0.25 2.5, nao sao iguais

c = (4+2)*2-4
c2 = 4+2*2-4

print(c,c2)
#resultado 8 e 4, nao sao iguais 
