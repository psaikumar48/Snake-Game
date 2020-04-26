import pygame
import random

M,N,grid_size=40,30,20
grids=[(i,j) for i in range(M) for j in range(N)]
Actions=['Top','Right','Bottum','Left']
Episode,High_score= 1,0

def food():
    global Food
    snake_no_grids= [i for i in grids if i not in Snake]
    Food = random.choice(snake_no_grids)
def display():
    pygame.draw.rect(screen,(0,0,0), (0,0,M*grid_size,N*grid_size))
    for i in Snake:
        pygame.draw.rect(screen,(255,255,255), (i[0]*grid_size,i[1]*grid_size,grid_size,grid_size),1)
    pygame.draw.rect(screen,(255,255,255), (Food[0]*grid_size,Food[1]*grid_size,grid_size,grid_size))
    pygame.display.update()
def update_snake():
    global snake_tail,snake_head,snake_body
    x,y=Snake[0][0],Snake[0][1]
    if action == 'Right' :
        Snake.insert(0,(x+1,y))
    elif action == 'Left' :
        Snake.insert(0,(x-1,y))
    elif action == 'Top' :
        Snake.insert(0,(x,y-1))
    elif action == 'Bottum' :
        Snake.insert(0,(x,y+1))
    snake_tail=Snake.pop()
    snake_head=Snake[0]
    snake_body=Snake[1:len(Snake)]
    display()

mloop=True
while mloop:
    pygame.init()
    screen = pygame.display.set_mode((M*grid_size,N*grid_size))
    Snake_wait_time=150
    Snake=[random.choice(grids)]
    action = random.choice(Actions)
    food()
    loop=True
    while loop:
        pygame.time.wait(Snake_wait_time)
        update_snake()
        if snake_head==Food:
            food()
            Snake.append(snake_tail)
            Snake_wait_time -=5
        elif snake_head not in grids or snake_head in snake_body:
            score=len(Snake)-1
            if score > High_score:
                High_score=score
            print('Episodes :',Episode,', High_score :',High_score,', Score :',score)
            Episode+=1
            loop=False
        ev=pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
                loop=False
                mloop=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    action='Right'
                elif event.key == pygame.K_LEFT:
                    action='Left'
                elif event.key == pygame.K_UP:
                    action='Top'
                elif event.key == pygame.K_DOWN:
                    action='Bottum'
