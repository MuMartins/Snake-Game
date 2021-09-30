# Importando as bibliotecas necessárias
import pygame
import sys

# Funções


# Iniciando o pygame e sua tela
pygame.init()
screen_borderW = 500
screen_borderH = 500
screen = pygame.display.set_mode((screen_borderW, screen_borderH))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# Config
player_x = 20
player_y = 20
player_speed = 20

bg_surface = pygame.image.load(
    'C:/Users/muril/Documents/ÁREA DE TRABALHO/01 - SCRIPTS/PYTHON/03 - PYGAME/Snake-Game/ASSETS/background.png')
bg_surface = pygame.transform.scale2x(bg_surface)

# Main loop


def main():
    '''Definindo escopo global para as variaveis de movimentação'''
    global player_x, player_y, player_speed

    '''Loop principal onde o jogo está sendo rodado'''
    while True:
        # Definindo os frames por segundo
        clock.tick(15)

        '''Verifição a cada frame do jogo'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        '''Movimentação do player'''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_y -= player_speed
            if player_y < 0:
                player_y = (screen_borderH - 20)

        if keys[pygame.K_DOWN]:
            player_y += player_speed
            if player_y > (screen_borderH - 20):
                player_y = 0

        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            if player_x < 0:
                player_x = (screen_borderW - 20)

        if keys[pygame.K_RIGHT]:
            player_x += player_speed
            if player_x > (screen_borderW - 20):
                player_x = 0

        '''Objetos sendo colocados na tela a cada frame'''
        # background
        screen.blit(bg_surface, (0, 0))

        # Snake
        pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, 20, 20))

        # Flip para dar update de todos os conteudos da tela
        pygame.display.flip()


if __name__ == '__main__':
    main()
