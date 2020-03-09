import pygame
import random

def food():
    snake_no_grids= [i for i in grids if i not in Snake]
    food_plc = random.choice(snake_no_grids)
    return food_plc
def display():
    pygame.draw.rect(screen,(0,0,0), (0,0,M*grid_size,N*grid_size))
    for i in Snake:
        pygame.draw.rect(screen,(255,255,255), (i[0]*grid_size,i[1]*grid_size,grid_size,grid_size),1)
    pygame.draw.rect(screen,(255,255,255), (Food[0]*grid_size,Food[1]*grid_size,grid_size,grid_size))
    pygame.display.update()
def new_snake():
    global snake_tail,snake_head
    new_snake=[]
    if move == 'Right' :
        new_snake.append((Snake[0][0]+1,Snake[0][1]))
    elif move == 'Left' :
        new_snake.append((Snake[0][0]-1,Snake[0][1]))
    elif move == 'Top' :
        new_snake.append((Snake[0][0],Snake[0][1]-1))
    elif move == 'Bottum' :
        new_snake.append((Snake[0][0],Snake[0][1]+1))
    for i in Snake:
        new_snake.append(i)
    snake_tail=new_snake.pop()
    snake_head=new_snake[0]
    return new_snake

M,N=40,30
grid_size=20
Snake=[(-1,0),(-2,0),(-3,0),(-4,0)]
move='Right'
grids=[]
for i in range(M):
    for j in range(N):
        grids.append((i,j))

mloop=True
while mloop:
    pygame.init()
    screen = pygame.display.set_mode((M*grid_size,N*grid_size))
    Food=food()
    loop=True
    while loop:
        pygame.time.wait(150)
        Snake=new_snake()
        display()
        snake_body=Snake[1:len(Snake)]
        if snake_head==Food:
            Food=food()
            Snake.append(snake_tail)
        if not (snake_head in grids) or snake_head in snake_body:
            print('Game over')
            print('Score : ',len(Snake)-4)
            Snake=[(-1,0),(-2,0),(-3,0),(-4,0)]
            move='Right'
            loop=False
        ev=pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
                loop=False
                mloop=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move='Right'
                elif event.key == pygame.K_LEFT:
                    move='Left'
                elif event.key == pygame.K_UP:
                    move='Top'
                elif event.key == pygame.K_DOWN:
                    move='Bottum'
