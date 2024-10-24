arred=0
soma=0
subt=0
div=0
mult=0
divo=0

n1 = 20 #int
n2 = 14.8 #float
n3 = "30" #str
n4 = 15.87953 #float
n5 = 12 #int
n6 = 5
#arredondar o numero
arred=0
arred=round (n4,2)
print(arred)
#adição
soma = round(n1 + n2 + n4) #Soma sem arredondamento
print(f" resultado é: {soma}")
soma = round(n1+n2+n4,2) #Soma com arredondamento
print(f" resultado arredondado é: {soma}")
#subtração
subt = round(n4-n2) #Subtração sem arredondamento
print(f" resultado é: {subt}")
subt = round (n4-n2,2) #Soma com arredondamento
print(f" resultado arredondado é: {subt}")
#divisao
div= round(n4/n2) #divisao sem arredondamento
print (f" resultado é: {div}")
div= round(n4/n2,2) #divisao com arredondamento
print (f" resultado arredondado é: {div}")
#multiplicacao
mult= round(n4*n2) #multiplicacao sem arredondamento
print (f" resultado é: {mult}")
mult= round(n4*n2,2) #multiplicacao com arredondamento
print (f" resultado arredondado é: {mult}")
#potenciacao
exp= n1**n5
print(f" resultado é: {exp}")
#divisão sem decimal
divo= n5//n6
print(f" resultado é: {divo}")