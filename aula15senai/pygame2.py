# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()

# ATIVIDADE 1: 

# o que a estrutura(sintaticamente)? para que serve(contexto)? 
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/

# 1 - cita a estrutura de código
# 2 - contextualiza 




#exemplo:
# 2 varáveis , uma define a altura a outra a largura 
largura, altura = 400, 400

tela = pygame.display.set_mode((largura, altura)) #setup
pygame.display.set_caption("Labirinto")


preto = (0, 0, 0) #define cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)


tamanho_celula = 40
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


x, y = 1 * tamanho_celula, 1 * tamanho_celula #velocidade do bloco vermelho
velocidade = 40
#moldando o labirinto
def desenhar_labirinto(): #le as arrays tudo
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))


executando = True #setando os loops, dando um resultado diferente a cada cenario
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False


    teclas = pygame.key.get_pressed() #definindo os movimentos e os botoes
    if teclas[pygame.K_LEFT]: #se a tecla for para esquerda, atualiza pra uma nova posição pro lado e assim em diante com todos os botoes
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]: #mesma coisa so que no eixo y
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y


    tela.fill(branco) #preenche a tela com uma cor pra "limpar" tudo do ultimo frame

    
    desenhar_labirinto() #chama o metodo
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))


    pygame.display.flip() #gira o display pra funcionar na sua tela


    pygame.time.Clock().tick(10)#relogio


pygame.quit() #fim!
