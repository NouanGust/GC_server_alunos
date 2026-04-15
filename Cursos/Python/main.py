import random 
import pygame

pygame.init()

# Define a largura e altura d atela em pixels 
largura = 600
altura = 400



# Define a tela
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption("Jogo da cobrinha")


# Cores
PRETO = (0,0,0)
VERDE = (0,255,0)
VERMELHO = (255,0,0)

# Define se o jogo está rodando

def jogar():
    tamanho_pixels = 20
    x, y = largura // 2, altura // 2
    velocidade_x, velocidade_y = 0, 0
    corpo_cobra = [[x,y]]
    comprimento_cobra = 1
    
    comida_x = round(random.randrange(0, largura - tamanho_pixels) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_pixels) / 20.0) * 20.0
    rodando = True  
    
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT: velocidade_x, velocidade_y = -tamanho_pixels, 0
                elif evento.key == pygame.K_RIGHT: velocidade_x, velocidade_y = tamanho_pixels, 0
                if evento.key == pygame.K_UP: velocidade_x, velocidade_y = 0, -tamanho_pixels
                if evento.key == pygame.K_DOWN: velocidade_x, velocidade_y = 0, tamanho_pixels
                
        x += velocidade_x
        y += velocidade_y
        
        cabeca = [x,y]
        corpo_cobra.append(cabeca)
        
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]
    
        
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_pixels) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_pixels) / 20.0) * 20.0
            comprimento_cobra += 1
            
        tela.fill(PRETO)
        for bloco in corpo_cobra:
            pygame.draw.rect(tela, VERDE, [bloco[0], bloco[1], tamanho_pixels, tamanho_pixels])
        
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, tamanho_pixels, tamanho_pixels])
        
        pygame.display.update()
        relogio.tick(15)


jogar()
pygame.quit()