#!/usr/bin/env python3
"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe
a mensagem correspondente (teste)

Usage:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe através do CLI argument '--lang'

Ou o usuário terá que digitar

Execução:


    python3 hello.py
    ou
    ./hello.py

    ultima visita - 22/08/2024 - DAY 3 - EP1
"""
__version__ = "0.1.2"
__author__ = "Raphael"
__licence__ = "copyleft"

import os #biblioteca externa
import sys

arguments = { "lang": None,"count": 1 }

for arg in sys.argv[1:]:
    #TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value
    
current_language = arguments["lang"]
if current_language is None:
    #TODO usar repetição

    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")


current_language = current_language[:5]
        
msg = {

    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

print(
    msg[current_language] * int(arguments["count"])
)

#sets (Hash Table) - O(1) - constante
#dicts (Hash Table) 


#primeira versão

#msg = "Hello, World!"
#Ordem de Complexidade O(n)
#if current_language == "pt_BR":
#    msg = "Olá, Mundo!"
#elif current_language == "it_IT":
#    msg = "Ciao, Mondo"
#elif current_language == "es_SP":
#    msg = "Hola, Mundo"
#elif current_language == "fr_FR":
#    msg = "Bonjour, Monde" 
#elif current_language == "fr_FR":
#           msg = "Bonjour, Monde"    

#print(msg)


