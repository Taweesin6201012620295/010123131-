# Thank you reference by https://youtu.be/1_H7InPMjaY
import pygame,sys
pygame.init()
running = True
clock = pygame.time.Clock()
Sr_w,Sr_h = 1200,600
screen = pygame.display.set_mode((Sr_w,Sr_h))
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

Cr1 = x,y = 120,120
Cr2 = r,s = 140,140
x1 = x+30
x2 = x-30
y1 = y+30
y2 = y-30
r1 = r+20
r2 = r-20
s1 = s+20
s2 = s-20
def B_R():
    global x,y,x_speed,y_speed,x1,x2,y1,y2,r,s,r1,r2,s1,s2,x1_speed,y1_speed
    x += x_speed
    y += y_speed
    r += x1_speed
    s += y1_speed
    
    x1 += x_speed
    x2 += x_speed
    y1 += y_speed
    y2 += y_speed

    r1 += x1_speed
    r2 += x1_speed
    s1 += y1_speed
    s2 += y1_speed
    # collison with rect
    collision_T = 10
    if Cr1 == Cr2:
        if abs(s1 - y2) < collision_T and y_speed > 0 and y1_speed < 0:
            y_speed *= -1
            y1_speed *= -1
        if abs(s2 - y1) < collision_T and y_speed < 0 and y1_speed > 0:
            y_speed *= -1
            y1_speed *= -1
        if abs(r1 - x2) < collision_T and x_speed < 0 and x1_speed > 0:
            x_speed *= -1
            x1_speed *= -1
        if abs(r2 - x1) < collision_T and x_speed > 0 and x_speed < 0:
            x_speed *= -1
            x1_speed *= -1

        print("Collision")

    # collision with screen borders
    if x1 >= Sr_w or x2 <= 0:
        x_speed *= -1
    if y1 >= Sr_h or y2 <= 0:
        y_speed *= -1
    if r1 >= Sr_w or r2 <= 0:
        x1_speed *= -1
    if s1 >= Sr_h or s2 <= 0:
        y1_speed *= -1


    pygame.draw.circle(screen,(255,255,255),(x,y),30)
    pygame.draw.circle(screen,(0,125,8),(r,s),20)



x_speed,y_speed = 10,10
x1_speed,y1_speed = 8,7

while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


    screen.fill((30,30,30))
    B_R()
    pygame.display.flip()
    clock.tick(60)