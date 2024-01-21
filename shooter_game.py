


import pygame
import time
import random

pygame.init()

# Розміри екрану
screen_width = 600
screen_height = 400

# Створити екран
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('MY VIDEO GAME!!!!')

# Інші змінні та функції для гри "Змійка"
snake_block = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 30)

def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, (255, 255, 255))
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_running = True
    # Початкові координати та швидкість змії
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    # Початкова довжина змії
    snake_length = 1
    snake_list = []

    # Координати їжі
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        # Перевірка
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_running = False

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), [foodx, foody, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_running = False

        our_snake(snake_block, snake_list)
        Your_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()

# Створити дві кнопки для меню
play_button = pygame.Rect(250, 200, 100, 50)
exit_button = pygame.Rect(250, 300, 100, 50)

# Створити два шрифти для меню
button_font = pygame.font.SysFont("Arial", 32)
title_font = pygame.font.SysFont("Arial", 64)

# Створити два тексту для меню
play_text = button_font.render("Play", True, (255, 255, 255))
exit_text = button_font.render("Exit", True, (255, 255, 255))
title_text = title_font.render("Menu", True, (255, 255, 255))

# Створити змінну для керування циклом меню
menu_running = True

# Головний цикл меню
while menu_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                # Запуск гри
                menu_running = False
                gameLoop()
            elif exit_button.collidepoint(mouse_pos):
                menu_running = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (128, 128, 128), play_button)
    pygame.draw.rect(screen, (128, 128, 128), exit_button)

    screen.blit(play_text, (play_button.x + 25, play_button.y + 10))
    screen.blit(exit_text, (exit_button.x + 25, exit_button.y + 10))


    screen.blit(title_text, (200, 100))

    pygame.display.flip()

pygame.quit()