# Importing
import pygame
import sys
from random import randrange

# Functions


def snake(snake_list):
    # Creating the blue blocks of the body
    for all_snake in snake_list[:-1]:
        pygame.draw.rect(screen, (0, 0, 255), [
                         all_snake[0], all_snake[1], 20, 20])

    # Creating the red block of the head
    for head_snake in snake_list[0]:
        pygame.draw.rect(screen, (255, 0, 0), [player_x, player_y, 20, 20])


def game_over():
    '''Game over screen function'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Check if the the key R is pressed to run the game again
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and not player_alive:
                    main()

        # Puts the game over screen
        screen.fill((0, 0, 0))
        screen.blit(game_over_surface, (0, 0))
        score_offgame_surface = myfont.render(
            f'YOUR SCORE: {player_score}', False, (255, 255, 255))
        restart_text = myfont.render(
            f'PRESS R TO RESTART', False, (255, 255, 255))
        screen.blit(score_offgame_surface, (180, 350))
        screen.blit(restart_text, (155, 380))
        pygame.display.flip()


# Init the pygame and the game screen
pygame.init()
pygame.font.init()
screen_borderW = 500
screen_borderH = 500
screen = pygame.display.set_mode((screen_borderW, screen_borderH))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Arial', 20)

# Loading all the images for the game
bg_surface = pygame.image.load('ASSETS/background.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
game_over_surface = pygame.image.load('ASSETS/game-over.png')
food_surface = pygame.image.load('ASSETS/food.png')
box_surface = pygame.image.load('ASSETS/box.png')


# Main loop
def main():
    global player_x, player_y, player_score, keys, player_alive

    # Defining the movement and the game loop
    movement = ''
    player_alive = True

    # Defining where the player starts, the player speed and the score
    player_x = 60
    player_y = 220
    player_speed = 20
    player_score = 0

    # Defining the snake list and length
    snake_list = []
    snake_length = 1

    # Defining the first food position
    food_list = []
    food_head = []
    food_x = 220
    food_y = 220
    food_head.append(food_x)
    food_head.append(food_y)
    food_list.append(food_head[:])

    # Defining the box lists
    box_list = []
    box_head = []

    '''Main loop for the game'''
    while True:
        # Frames per second
        clock.tick(10)

        '''Ending the game by clicking to close the window'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            keys = pygame.key.get_pressed()
            # Detect the key movement and check if the player is alive
            if keys[pygame.K_UP] and movement != 'down' and player_alive:
                movement = 'up'

            if keys[pygame.K_DOWN] and movement != 'up' and player_alive:
                movement = 'down'

            if keys[pygame.K_LEFT] and movement != 'right' and player_alive:
                movement = 'left'

            if keys[pygame.K_RIGHT] and movement != 'left' and player_alive:
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

        # Generating a new food and box object
        if player_x == food_x and player_y == food_y:
            snake_length += 1
            player_score += 1

            food_x = randrange(0, 500, 20)
            food_y = randrange(0, 500, 20)

            # Check if the position of the snake is the same position of the food
            for food_check in snake_list:
                if food_check[0] == food_x:
                    food_x = randrange(0, 500, 20)
                if food_check[1] == food_y:
                    food_y = randrange(0, 500, 20)

            # Check if the position of the boxes is the same position of the food
            for food_check in box_list:
                if food_check[0] == food_x:
                    food_x = randrange(0, 500, 20)
                if food_check[1] == food_y:
                    food_y = randrange(0, 500, 20)

            # After the check is done, generate a new food
            food_head.clear()
            food_head.append(food_x)
            food_head.append(food_y)
            food_list.append(food_head[:])

            # Every 2 food eaten, generate a new box
            if player_score % 2 == 0:
                box_x = randrange(0, 500, 20)
                box_y = randrange(0, 500, 20)

                # Check if the position of the snake is the same position of the new box
                for box_check in snake_list:
                    if box_check[0] == box_x:
                        box_x = randrange(0, 500, 20)
                    if box_check[1] == box_y:
                        box_y = randrange(0, 500, 20)

                # Check if the position of the food is the same position of the new box
                for box_check in food_head:
                    if box_check == box_x:
                        box_x = randrange(0, 500, 20)
                    if box_check == box_y:
                        box_y = randrange(0, 500, 20)

                # Check if the position of the boxes is the same position of the new box
                for box_check in box_list:
                    if box_check[0] == box_x:
                        box_x = randrange(0, 500, 20)
                    if box_check[1] == box_y:
                        box_y = randrange(0, 500, 20)

                # After the check is done, generate a new box
                box_head.append(box_x)
                box_head.append(box_y)
                box_list.append(box_head[:])
                box_head.clear()

        '''Objects being placed on the screen at each frame'''
        # Objects in the screen
        screen.blit(bg_surface, (0, 0))
        screen.blit(food_surface, (food_head[0], food_head[1]))

        # Puts the score on the screen
        score_game_surface = myfont.render(
            f'{player_score}', False, (255, 255, 255))
        screen.blit(score_game_surface, (10, 10))

        for box_obj in box_list:
            # Puts all the boxes on the screen
            screen.blit(box_surface, (box_obj[0], box_obj[1]))

            # Hitting the box and ending the game
            if player_x == box_obj[0] and player_y == box_obj[1]:
                player_alive = False

        '''Snake properties'''
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
                player_alive = False

        # Getting the color of the snake
        snake(snake_list)

        # Flip giving update for every content in the screen
        pygame.display.flip()

        # Check if the player is alive, if not, runs the game over screen
        if not player_alive:
            game_over()


if __name__ == '__main__':
    main()
