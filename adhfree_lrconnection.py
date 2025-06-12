import random
import time
import os
import winsound
import pygame

frequency = 2500 # Set Frequency To 2500 Hertz
duration = 500 # Set Duration To 1000 ms == 1 second

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LR Exercise")

# Set up fonts
font = pygame.font.SysFont('Arial', 32)
small_font = pygame.font.SysFont('Arial', 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def get_iterations():
    input_str = ""
    getting_input = True
    while getting_input:
        win.fill(WHITE)
        draw_text("How many iterations?", font, BLACK, win, WIDTH//2, HEIGHT//3)
        draw_text(input_str, font, BLACK, win, WIDTH//2, HEIGHT//2)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_str == "":
                        continue
                    if not input_str.isdigit() or int(input_str) < 1:
                        input_str = ""
                        continue
                    return int(input_str)
                elif event.key == pygame.K_BACKSPACE:
                    input_str = input_str[:-1]
                elif event.unicode.isdigit():
                    input_str += event.unicode

def main():
    iters = get_iterations()
    running = True
    current_iter = 0
    show_lr = False
    lr_value = ""
    next_time = 0

    # Wait for user to start
    win.fill(WHITE)
    draw_text("Get ready for the exercise!", font, BLACK, win, WIDTH//2, HEIGHT//3)
    draw_text("Press any key to start...", small_font, BLACK, win, WIDTH//2, HEIGHT//2)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

    win.fill(WHITE)
    pygame.display.update()
    pygame.time.delay(500)

    while running and current_iter < iters:
        if not show_lr:
            winsound.Beep(frequency, duration)  # Play beep sound using winsound
            lr_value = random.choice(["L", "R"])
            show_lr = True
            next_time = pygame.time.get_ticks() + random.randint(1000, 5000)
            win.fill(WHITE)
            draw_text(lr_value, font, BLACK, win, WIDTH//2, HEIGHT//2)
            pygame.display.update()
        else:
            if pygame.time.get_ticks() >= next_time:
                show_lr = False
                current_iter += 1
                win.fill(WHITE)
                pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Done
    win.fill(WHITE)
    draw_text("Exercise Complete!", font, BLACK, win, WIDTH//2, HEIGHT//2)
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()

if __name__ == "__main__":
    main()
