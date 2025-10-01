def verificar_idade(idade):
    if idade >= 18:
        return "você é maior de idade"
    else:
        return "você é menor de idade"

idade = int(input("digite sua idade"))

resultado = verificar_idade(idade)

print(resultado)