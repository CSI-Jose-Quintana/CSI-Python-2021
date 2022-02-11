import pygame
pygame.init()


yellow = (251, 230, 70) #score
green = (107, 250, 158) #food
black = (0, 0, 0) #background color
blue = (91, 57, 250) #snake
red = (250, 76, 70) #game over

dis=pygame.display.set_mode((400, 300))

pygame.display.set_caption("Snake game by JD")
game_over=False

x1 = 150
y1 = 150

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10

    x1 += x1_change
    y1 += y1_change
    dis.fill(black)              
    pygame.draw.rect(dis, blue, [x1, y1, 10, 10]) # crea el snake y lo ubica en la pantalla
    pygame.display.update()   

    clock.tick(30)  
pygame.quit()
quit()




