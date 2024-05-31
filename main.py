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

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, "red", (x_pos * 100 + 15, y_pos * 100 + 15),(x_pos * 100 + 85, y_pos * 100 + 85))
                pygame.draw.line(screen, "red", (x_pos * 100 + 85, y_pos * 100 + 15),(x_pos * 100 + 15, y_pos * 100 + 85))
            if y == -1:
                pygame.draw.circle(screen, "green", (x_pos * 100 + 50, y_pos * 100 + 50), 38, 6)
            y_pos += 1
        x_pos += 1
def check_gameover():
    global game_over
    global winner
    x_pos = 0
    
    for x in markers:
        x_pos += 1


run = True
while run:
    draw_board()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]//100
                cell_y = pos[0]//100
                if markers[cell_x][cell_y] == 0:
                    markers[cell_x][cell_y] == player
                    player *= -1
                    check_gameover()

    if game_over == True:
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            for x in range(3):
                row = [0] * 3
                markers.append(row)


    pygame.display.update()
pygame.quit()