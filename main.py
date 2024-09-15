import pygame
import random


pygame.init()


play_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Matryoshka Invasion')
icon = pygame.image.load("img/pngwing.com.png")
pygame.display.set_icon(icon)

matryoshka = pygame.image.load("img/pngwing.com.png").convert_alpha()
matryoshka_width = 160
matryoshka_height = 240
matryoshka = pygame.transform.scale(matryoshka, (matryoshka_width, matryoshka_height))

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0
attempts = 10
font = pygame.font.Font(None, 32) #создаются объекты-шрифты


running = True
while running:
    play_screen.fill(color)
    matryoshka_x = random.randint(0, 800 - matryoshka_width)
    matryoshka_y = random.randint(0, 600 - matryoshka_height)

    if attempts <= 0:
        play_screen.fill(color)
        for i in range(1000):
            matryoshka_x = random.randint(0, 800 - matryoshka_width)
            matryoshka_y = random.randint(0, 600 - matryoshka_height)
            play_screen.blit(matryoshka, (matryoshka_x, matryoshka_y))
            pygame.display.flip()  # выводит все на экран
        text_lose = font.render("you lose. sad.", True, (0, 0, 0))  # создает поверхность надписью
        play_screen.blit(text_lose, (300, 300))
        pygame.display.flip()  # выводит все на экран
        pygame.time.delay(5000)
        running = False

    elif score >= 5:
        play_screen.fill(color)
        text_win = font.render("you win! congratulation!", True, (0, 0, 0))  # создает поверхность надписью
        play_screen.blit(text_win, (300, 300))
        pygame.display.flip()  # выводит все на экран
        pygame.time.delay(10000)
        running = False

    text1 = font.render(f"your score: {score}", True, (0, 0, 0))  # создает поверхность надписью
    text2 = font.render(f'attempts: {attempts}', True, (0, 0, 0))  # создает поверхность надписью
    play_screen.blit(text1, (0, 0))
    play_screen.blit(text2, (0, 25))
    play_screen.blit(matryoshka, (matryoshka_x, matryoshka_y))
    pygame.display.flip() #выводит все на экран
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            attempts -= 1
            if matryoshka_x < mouse_x and mouse_x < matryoshka_x + matryoshka_width and matryoshka_y < mouse_y and mouse_y < matryoshka_y + matryoshka_height:
                score += 1
    pygame.time.delay(1000)








pygame.quit()
