# Recebe a entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um conceito e retornar seu respectivo local de armazenamento.
def armazenar_dado(tipo):
  if tipo == "Imagem":
    return "Blob Storage"
  elif tipo == "Transações Bancárias":
    return "Banco de Dados Relacional"
  elif tipo == "Logs de Servidor":
    return "Data Lake"
  elif tipo == "Documentos Word":
    return "SharePoint"

# Imprime o resultado de acordo com a entrada
print(armazenar_dado(entrada))