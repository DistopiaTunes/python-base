#!/user/bin/env python
"""
"Imprime a mensagem de um email"
"""

__version__:"0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print ("informa o nome do arquivo emails")
    sys.exit(1)
    
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) #emails.txt
templatepath = os.path.join(path, templatename) #email_tmpl.txt


for line in open(filepath):
    name, email = line.split(",")
    
    print(f"Enviando email para:{email}")
    print()
    print(
        open(templatepath).read() 
        % {
         "nome": name, 
         "produto":"caneta",
          "texto": "Escrever muito bem",
          "link":"https://canetaslegais.com",
          "quantidade": 1, 
          "preco": 50.5
          
          }
    )
    print ("-" * 50)
