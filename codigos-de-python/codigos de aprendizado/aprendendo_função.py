def calcular_imposto(salario):
    salario = float(salario)
    if salario <= 1518:
        impostado =  salario * 0.075
        valor_descontato = salario + impostado 
        print(f"seu salario de {salario} virou {valor_descontato:.2f} se não tivesse o desconto de 7,5%")

    elif salario > 1518 and salario < 2793.88:
        impostado =  salario * 0.09
        valor_descontato = salario + impostado 
        print(f"seu salario de {salario} virou {valor_descontato:.2f} se não tivesse o desconto de 9%")

    elif salario > 2793.89 and salario < 4190.83:
        impostado =  salario * 0.12
        valor_descontato = salario + impostado 
        print(f"seu salario de {salario} virou {valor_descontato:.2f} se não tivesse o desconto de 12%")
    
    elif salario > 4190.84 and salario < 8157.41:
        impostado =  salario * 0.14
        valor_descontato = salario + impostado 
        print(f"seu salario de {salario} virou {valor_descontato:.2f} se não tivesse o desconto de 13%")
    
    return valor_descontato
user = input("qual o valor do seu salario: ")

try:
    salario_num = float(user.replace(",", "."))
    calcular_imposto(user)

except ValueError:
    print("Somente valores numéricos, bro.")


    