# Importando as bibliotecas necessárias 
import pygame, sys

from pygame.constants import KEYDOWN 

# Funções


# Iniciando o pygame e sua tela
pygame.init()
screen = pygame.display.set_mode((500,500))

# Config
location_x = 0
location_y = 0

bg_surface = pygame.image.load('ASSETS/background.png')
bg_surface = pygame.transform.scale2x(bg_surface)

snake_list = [0]

# Main loop
def main():
    global location_x, location_y
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_LEFT:
                    location_x -= 20
                if event.key == pygame.K_RIGHT:
                    location_x += 20
                if event.key == pygame.K_UP:
                    location_y -= 20
                if event.key == pygame.K_DOWN:
                    location_y += 20
    
        screen.blit(bg_surface, (0,0))

        pygame.draw.rect(screen, (0,0,255), (20 + location_x, 20 + location_y, 20, 20))

        pygame.display.flip()

if __name__ == '__main__':
    main()