#EXERCÍCIOS
#Utilizando Python

#Exercício 1: Criar e ler um Arquivo

#Exercício 2:Criar um Diretório

#Exercício 3: Renomear um Diretório

#Exercício 4:  Listar Arquivos em um Diretório

#Exercício 5:  Copiar Arquivos em um Diretório

#Exercício 6:  Remover

"""#Exercício 1: Criar e ler um Arquivo

import os

with open('rodigrinho', 'w') as arquivo: #criou arquivo
    arquivo.write("teste")

with open('rodigrinho', 'r') as arquivo: #puxou na memoria e leu
    conteudo = arquivo.read()
    print(conteudo)"""

#Exercício 2:Criar um Diretório

import os
with os.scandir('C:/Users/Aluno/Downloads/aula14senai/') as entrada:
    for arquivo in entrada:
       print(f'diretorio encontrado: {arquivo.name}')
#Exercício 3: Renomear um Diretório
"""os.rename("rodigrinho", "corithians")"""
#Exercício 4:  Listar Arquivos em um Diretório
for arquivo in entrada:
        if arquivo.is_file():
            print(f'Arquivo encontrado: {arquivo.name}')
#Exercício 5:  Copiar Arquivos em um Diretório
import shutil
shutil.copytree('novo_arquivo', '1910')
#Exercício 6:  Remover
shutil.rmtree('C:/Users/Aluno/Downloads/aula14senai/')


