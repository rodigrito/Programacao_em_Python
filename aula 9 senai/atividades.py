"""#***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***

def checar_par_impar_simples(a, b):
    if a % 2 == 0:
        print ("{a} é PAR.")
    else:
        print("{a} é IMPAR.")
        
    if b % 2 == 0:
        print("{b} é PAR.")
    else:
        print("{b} é IMPAR.")

checar_par_impar_simples(33, 40)

#***CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***

def multiplicar(x, y, z):
    return x * y * z

resultado = multiplicar(10, 5, 2)
print("produto é: {resultado}")

#***UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***

def calcular_potencia(base, expoente):
    return base ** expoente

valor = calcular_potencia(5, 3)
print("o valo elevado é: {valor}")

#***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***

def mensagem_idade(idade):
    if idade == 18:
        print("vc eh de maior")
    else:
        print(f"ce tem {idade} anos.")

mensagem_idade(18)
mensagem_idade(29)

#***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

def descobrir_idade(nascimento, atual):
    return atual - nascimento

idade_final = descobrir_idade(1990, 2025)
print("a pessoa tem {idade_final} anos.")

#****DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***

def copa(ano):
    if ano == 1999:
        print("O Brasil NÃO ganhou a Copa do Mundo em 1999.")
    else:
        print("A pergunta era sobre 1999.")

copa(1999)

#***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***

def cumprimentar(nome):
    print(f"ola, {nome} ! tudo joia? bem-vindo ao restaurante.")

def sistema_restaurante():
    menu = ["salada", "macarronada", "sanduíche", "sorvete"]
    precos = [15.00, 35.00, 20.00, 12.00]
    pedido = []
    total = 0.0

    print("menu")
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]} - R$ {precos[i]:.2f}")
    print("5. encerra pedido")
    
    while True:
        try:
            escolha = int(input("escolha item (1-5): "))
            
            if escolha == 5:
                break
            
            elif 1 <= escolha <= 4:
                item_indice = escolha - 1
                pedido.append(menu[item_indice])
                total += precos[item_indice]
                print(f"adicionado: {menu[item_indice]}")
            else:
                print("opção inválida.")
                
        except ValueError:
            print("entrada inválida. digite só numeros.")

    print("\nresumo pedido:")
    for item in pedido:
        print(f"- {item}")
        
    print(f"total deu: R$ {total:.2f} volte sempre!!!!")

nome_cliente = input("Digite seu nome: ")
cumprimentar(nome_cliente)
sistema_restaurante()"""