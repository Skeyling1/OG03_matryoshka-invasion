import pygame
import random


pygame.init()



play_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Matryoshka Invasion')
icon = pygame.image.load("img/pngwing.com.png")
pygame.display.set_icon(icon)


matryoshka = pygame.image.load("img/pngwing.com.png")
matryoshka_height = 80
matryoshka_width = 80

matryoshka_x = random.randint(0, 800-matryoshka_width)
matryoshka_y = random.randint(0, 600-matryoshka_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))




running = True
while running:
    play_screen.fill(color)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
        if event == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if matryoshka_x < mouse_x and mouse_x < matryoshka_x + matryoshka_width and matryoshka_y < mouse_y and mouse_y < matryoshka_y + matryoshka_height:
                pass

    pygame.display.flip()






pygame.quit()