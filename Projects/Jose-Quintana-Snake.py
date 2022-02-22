import random
import pygame
import time
pygame.init()


yellow = (251, 230, 70) #score
green = (107, 250, 158) #food
black = (0, 0, 0) #background color
blue = (91, 57, 250) #snake
red = (250, 76, 70) #game over

dis_width = 400
dis_height = 300
dis=pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption("Snake game by JD")
game_over=False

snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 25)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/7, dis_height/2])

def gameRestart():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) *10
    foody = round(random.randrange(0, dis_width - snake_block) / 10) *10


    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("YOU LOST Press Q-Quit or P-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameRestart()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)  
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])  #crea el food      
        pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block]) # crea el snake y lo ubica en la pantalla
        pygame.display.update()   

        clock.tick(snake_speed) 


# pygame.display.update()
# time.sleep(5)
    pygame.quit()
    quit()

gameRestart()




