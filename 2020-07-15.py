
'''# 6201012620295 
โค้ดนี้สำหรับ Assignment I ให้สร้างวงกลม 10 วงโดยใช้ from random import randint เพื่อสุ่ม สี และ รัศมีของวงกลมนั้นๆ
จากนั้นนำเมาท์ไปคลิกวงกรมที่ใหญ่ที่สุดเผื่อให้วงกลมนั้นหายไป
'''
# Note this Python script requires PyGame.
import pygame 
from random import randint
import math
# initialize PyGame
pygame.init()

# show PyGame version
print( 'PyGame version: {}'.format( pygame.version.ver ) ) 


# set window caption
pygame.display.set_caption('PyGame Demo 1') 

# create a clock
clock = pygame.time.Clock()

# Set up the drawing window (800 x 600 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

randint(10,20)
O = []
#Genarate circle 10 time
for a in range(10):    
    # randomize an integer value between 10-20 for the radius
    r = randint(10,20)
    r1 = randint(10,20)
    rd = r1+r
    # Random color
    R = randint(0,255)
    G = randint(0,255)
    B = randint(0,255) 
    color1 = (R,G,B) 
    # randomize a position (x,y)
    x,y = randint(r,scr_w-r), randint(r,scr_h-r)
    x1,y1 = randint(r1,scr_w-r1), randint(r1,scr_h-r1)
    # Stroe value of x,y,r in list O
    O.append([x,y,r])
    for a in O:
        if len(O)>1:
            d = (math.sqrt((x1-x)**2))+(math.sqrt((y1-y)**2))
            if(d >= rd):
                # draw a circle filled with the random color on the surface
                pygame.draw.circle( surface, color1, (x,y), r )
                # fill the screen with the Black color
                screen.fill((0,0,0))
                # draw the surface on the screen
                screen.blit(surface, (0,0))
                # update the screen display
                pygame.display.update()
                print("draw")
            else:
                pass
        else:
            # draw a circle filled with the random color on the surface
            pygame.draw.circle( surface, color1, (x1,y1), r1 )
            # fill the screen with the Black color
            screen.fill((0,0,0))
            # draw the surface on the screen
            screen.blit(surface, (0,0))
            # update the screen display
            pygame.display.update()
#Find Maximum of radius in List O
def Max_R(O):
    n = 0
    Max = O[n][2]
    for i in range(len(O)-1):
        if(Max < O[i+1][2]):
            Max =  O[i+1][2]
        else:
            Max = Max
    return Max

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    k = []
    for i in range(len(O)):
        if(O[i][2] == Max_R(O)):
            k.append([O[i][0], O[i][1], O[i][2]])
#Generate a circle that is the same size as the largest circle.
    for j in range(len(k)):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if((k[j][0]-pos[0])**2 + (k[j][1]-pos[1])**2 <= Max_R(O)**2):
                    #Paint genarate circle same color of screen at the position of largest circle
                    pygame.draw.circle( surface, (0,0,0), (k[j][0],k[j][1]), k[j][2] )
                    screen.blit(surface, (0,0))
                    pygame.display.update()
print(k)
pygame.quit()
