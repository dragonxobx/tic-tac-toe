import pygame
pygame.init()
screen_height = 300
screen_width = 300
player = 1
game_over = False
winner = 0
clicked = False
pos = (0, 0)
markers = []
screen = pygame.display.set_mode((screen_height, screen_width))

for x in range (3):
    row = [0] * 3
    markers.append(row)

def draw_board():
    screen.fill("black")
    for x in range (1,3):
        pygame.draw.line(screen, "white", (0, 100 * x), (screen_width, 100 * x), 6)
        pygame.draw.line(screen, "white", (100 * x, 0), (100 * x, screen_height), 6)

run = True
while run:
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()