# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def tipo_banco(nome):
  if nome == "MySQL":
    return "Relacional"
  elif nome == "MongoDB":
    return "NoSQL"
  elif nome == "Cosmos DB":
    return "NoSQL (Distribuído)"
  elif nome == "SQL Server":
    return "Relacional"

# Imprime o resultado de acordo com a entrada
print(tipo_banco(entrada))