import pygame
pygame.init()
W=1200
H=800
screen = pygame.display.set_mode((W,H))
s_color  = 255,255,255
red = 255,0,0
x,y,w,h = 0,0,50,50
move_x=0
move_y=0
while True:#infinite loop
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit(0)

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                move_x=-1
                move_y=0
            elif event.key==pygame.K_RIGHT:
                move_x=1
                move_y=0
            elif event.key==pygame.K_UP:
                move_x=0
                move_y=-1
            elif event.key==pygame.K_DOWN:
                move_x=0
                move_y=1

    screen.fill(s_color)
    snake  = pygame.draw.rect(screen,red,[x,y,w,h])
    x+=move_x
    y+=move_y
    if x<0:
        x=W-w
    elif x==W-w:
        x=0
    elif y<0:
        y=H-h
    elif y>H-h:
        y=0
        
    pygame.display.update()
