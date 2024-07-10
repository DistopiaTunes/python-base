#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.

"""
__version__ = "0.1.1"

#Dados



sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles),
    ("Música", aula_musica), 
    ("Dança", aula_danca),
]

atividadeing = {
    "sala1": ["Erik","Maia"],
    "sala2": ["Joana", "Carlos", "Maria"]
    
}

atividademus = {
    "sala1": ["Erik"],
    "sala2": ["Carlos", "Maria"]
}

atividadedan = {
    "sala1": ["Gustavo", "Sofia", "Joana"],
    "sala2": ["Antonio" ]
}

print (f">>> Alunos Matriculados em Inglês na Sala 1")
print (atividadeing['sala1'])
print (f">>> Alunos Matriculados em Inglês na Sala 2")
print (atividadeing['sala2'])
print("#" * 40)
print (f">>> Alunos Matriculados em Música na Sala 1")
print (atividademus['sala1'])
print (f">>> Alunos Matriculados em Música na Sala 2")
print (atividademus['sala2'])
print("#" * 40)
print (f">>> Alunos Matriculados em Dança na Sala 1")
print (atividadedan['sala1'])
print (f">>> Alunos Matriculados em Dança na Sala 2")
print (atividadedan['sala2'])
print("#" * 40)


# a solução de sets com certeza é a mais elegante, mas talvez essa solução seja minimamente aceitavel


# Listar alunos em cada atividade por sala

#for nome_atividade, atividade in atividades:
#
 #   print(f"Alunos da atividade {nome_atividade}\n")
 #   print("-" * 40)

 # sala1 que tem interseção com a atividade: símbolo >  &  <
 #   atividade_sala1 = set(sala1) & set(atividade)
  #  atividade_sala2 = set(sala2) & set(atividade)
   
    
  #  print("Sala 1 ", atividade_sala1)
  #  print("Sala 2 ", atividade_sala2)
  #  print()

   # print("#" * 40)
