#Comandos basicos de loops:
"""for
while
try
except
pass
finally"""

"""Atividades para trabalhar com try and except
Exercício 1: Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.


Exercício 2: Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação - ZeroDivisionError.


Exercício 3: Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).
Suba as atividade para o github"""
try:
    x = int(input("Digite um número inteiro: ")) 
    erro = "Erro, digite algo válido"
except ValueError as erro:
    print(erro)
except ZeroDivisionError as erro:
    print(erro)
finally:
    print("Fim de carregamento")


try:
    numero1 = float(input("Digite o numero que quer dividir: "))
    numero2 =  float(input("Digite o divisor: "))
    resultado = numero1 / numero2
    
    print("O resultado da divisão é: ")
    print(resultado)
    erro = "Erro, digite algo válido"
except ValueError as erro:
    print(erro)
except ZeroDivisionError as erro:
    print(erro)
finally:
    print("fim de carregamento")




lista = ["A(0)", "B(1)", "C(2)"]
print(lista)
indice_lista = int(input("digite o indice de qual letra vc quer"))
try:
    elemento = lista[indice_lista]

    print("o elemento no indice {indice_lista} é: {elemento}.")
except IndexError:
    print("erro, o indice {indice_lista} é invalido")
finally:
    print("fim de carregamento")