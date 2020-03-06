import pandas as pd
import pygame
import random 
pygame.init()

def show(x,y,colour,boundary_size):
    pygame.draw.rect(screen,colour, (x*w,y*h,w,h),boundary_size)
    pygame.display.update()
    
M,N=30,20
w,h=20,20
x_Window_size=(M+1)*w
y_Window_size=(N+1)*h

def f3(lst):
    aa=lst[0]
    while aa in lst:
        x=random.sample(range(M),1)
        y=random.sample(range(N),1)
        aa=(x[0],y[0])
    return aa

def food(lst,plc,end):
    if lst[0]==(plc[0],plc[1]):
        lst.append(end)
        fplc=f3(lst)
        return fplc,lst
    else:
        return plc,lst

ip=[(-1,0),(-2,0),(-3,0),(-4,0)]

def f1(ip,turn):
    for i in ip:
        show(i[0],i[1],(0,0,0),0)
    op=[]
    if turn=='r':
        op.append((ip[0][0]+1,ip[0][1]))
    elif turn=='l':
        op.append((ip[0][0]-1,ip[0][1]))
    elif turn=='t':
        op.append((ip[0][0],ip[0][1]-1))
    elif turn=='b':
        op.append((ip[0][0],ip[0][1]+1))
    for i in ip:
        op.append(i)
    end=op.pop()
    for i in op:
        show(i[0],i[1],(255,255,255),1)
    return op,end

mloop=True
while mloop:
    screen = pygame.display.set_mode((x_Window_size,y_Window_size))
    fp=[3,4]
    show(fp[0],fp[1],(255,0,0),0)
    pygame.display.update()
    ent='r'
    loop=True
    while loop:
        pygame.time.wait(150)
        ip,end=f1(ip,ent)
        fp,lst=food(ip,fp,end)
        show(fp[0],fp[1],(255,0,0),0)
        if ip[0][0]>M or ip[0][0]<0 or ip[0][1]>N or ip[0][1]<0:
            score=len(ip)-4
            font = pygame.font.SysFont("comicsansms", int(y_Window_size/10))
            text = font.render(f"Score : {score}  Game over...", True, (255,255,255))
            screen.blit(text,((x_Window_size/2) - text.get_width() // 2, (y_Window_size/2) - text.get_height() // 2))
            pygame.display.update()
            pygame.time.wait(1000)
            pygame.quit()
            loop=False
            mloop=False
            
        ev=pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
                loop=False
                mloop=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ip,end=f1(ip,'r')
                    ent='r'
                elif event.key == pygame.K_LEFT:
                    ip,end=f1(ip,'l')
                    ent='l'
                elif event.key == pygame.K_UP:
                    ip,end=f1(ip,'t')
                    ent='t'
                elif event.key == pygame.K_DOWN:
                    ip,end=f1(ip,'b')
                    ent='b'
         
