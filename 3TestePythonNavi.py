# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 14:23:11 2020

@author: sarah
"""

alunos = {}          
  
def inserir():
    for x in range (0, 5):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Nota dele: "))
        
        if alunos.get(nome):
            print("Ja existe o aluno ",nome)
        else:
            alunos[nome] = nota
            
def exibir():
    print("O aluno com maior nota é:", max(alunos.items(), key=lambda x: x[1]))
        
            
inserir()
exibir()
