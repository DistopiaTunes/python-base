#!/usr/bin/env python3
"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe
a mensagem correspondente (teste)

Usage:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py

    ultima visita - 02/05/2024
"""
__version__ = "0.1.2"
__author__ = "Raphael"
__licence__ = "copyleft"

import os #biblioteca externa

current_language = os.getenv("LANG", "en_US")[:7]

msg = {

    "C.UTF-8": "Hello, World!",
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
    
}

# 0
print(msg[current_language])

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


