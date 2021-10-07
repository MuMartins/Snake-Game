# Importando as bibliotecas necessárias
import pygame
import sys
from random import randrange

# Funções


# Iniciando o pygame e sua tela
pygame.init()
screen_borderW = 500
screen_borderH = 500
screen = pygame.display.set_mode((screen_borderW, screen_borderH))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
movement = ''

# Config
player_x = 60
player_y = 220
player_speed = 20
snake_list = []
snake_length = 1

bg_surface = pygame.image.load('ASSETS/background.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

food_surface = pygame.image.load('ASSETS/food.png')
food_x = 220
food_y = 220

box_surface = pygame.image.load('ASSETS/box.png')
box_x = randrange(0, 500, 20)
box_y = randrange(0, 500, 20)

game_over = pygame.image.load('ASSETS/game-over.png')

# Main loop


def snake(snake_list):
    for all_snake in snake_list[:-1]:
        pygame.draw.rect(screen, (0, 0, 255), [
                         all_snake[0], all_snake[1], 20, 20])

    for head_snake in snake_list[0]:
        pygame.draw.rect(screen, (255, 0, 0), [player_x, player_y, 20, 20])


def main():
    global movement, game_over, snake_length, snake_list, player_x, player_y, player_speed, food_x, food_y, box_x, box_y
    game_on = True

    '''Main loop for the game'''
    while game_on:
        # Frames per second
        clock.tick(15)

        '''Ending the game by clicking to close the window'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            # Detect the key
            if keys[pygame.K_UP]:
                movement = 'up'

            if keys[pygame.K_DOWN]:
                movement = 'down'

            if keys[pygame.K_LEFT]:
                movement = 'left'

            if keys[pygame.K_RIGHT]:
                movement = 'right'

        '''Player Movement'''
        # Continuous movement
        if movement == 'up':
            player_y -= player_speed
            if player_y < 0:
                player_y = (screen_borderH - 20)

        if movement == 'down':
            player_y += player_speed
            if player_y > (screen_borderH - 20):
                player_y = 0

        if movement == 'left':
            player_x -= player_speed
            if player_x < 0:
                player_x = (screen_borderW - 20)

        if movement == 'right':
            player_x += player_speed
            if player_x > (screen_borderW - 20):
                player_x = 0

        # Generating a new food object
        if player_x == food_x and player_y == food_y:
            snake_length += 1
            food_x = randrange(0, 500, 20)
            food_y = randrange(0, 500, 20)

        # Hitting the box and ending the game
        if player_x == box_x and player_y == box_y:
            game_on = False

        '''Objetos sendo colocados na tela a cada frame'''
        # Objects in the screen
        screen.blit(bg_surface, (0, 0))
        screen.blit(food_surface, (food_x, food_y))
        screen.blit(box_surface, (box_x, box_y))

        '''Snake'''
        # Expanding snake list
        snake_head = []
        snake_head.append(player_x)
        snake_head.append(player_y)
        snake_list.append(snake_head)

        # Running snake by head
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Snake colission check
        for x in snake_list[:-1]:
            if x == snake_head:
                game_on = False

        # Getting the snake
        snake(snake_list)

        # Flip giving update for every content in the screen
        pygame.display.flip()

    '''Message of GAME OVER after hitting the box'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        screen.blit(game_over, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
