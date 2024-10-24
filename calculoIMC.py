#variavéis
altura = float 
peso = float
imc = float

#entradas de dados
altura = float (input("Qual é o sua altura em metros: "))
peso = float (input("Qual é o seu peso: "))

#processo
imc = round((peso/(altura*altura)),2)

if imc < 16 :
    classificacao = "magreza grave"

elif 16<= imc < 16.9:
    classificacao = "magreza moderada"

elif 17<= imc < 18.5:
    classificacao = "magreza leve"

elif 18.6<= imc < 24.9:
    classificacao = "magreza moderada"

elif 25 <= imc < 29.9:
    classificacao = "sobrepeso"

elif 30<= imc < 34.9:
    classificacao = "obesidade grau 1"

elif 35<= imc < 39.9:
    classificacao = "obesidade grau 2"

else:
    classificacao = "obesidade grau 3"

# Impressão de dados
print(f"Seu IMC é de {imc} e sua classificação: {classificacao}")