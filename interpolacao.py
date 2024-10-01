email_tmpl = """
   ...: Olá, %(nome)s
   ...:
   ...: Tens interesse em comprar %(produto)s?
   ...:
   ...: Este produto é ótimo para resolver seus problemas de %(texto)s
   ...:
   ...: Clique agora em %(link)s
   ...:
   ...: Apenas %(quantidade)d disponíveis!
   ...:
   ...: Preço promocional %(preco).2f
   ...: """


import sys
import os

arguments = sys.argv[1:]
if not argument:
    print ("informa o nome do arquivo emails")
    sys.exit(1)
filename = arguments.[0]

path = os.curdir
filepath = os.path.join(path, filename)

clientes = ["Maria", "Joao", "Raphael"]

for cliente in clientes:
    print(
        email_tmpl 
        % {
         "nome": cliente, 
         "produto":"caneta",
          "texto": "Escrever muito bem",
          "link":"https://canetaslegais.com",
          "quantidade": 1, 
          "preco": 50.5
          }
)
