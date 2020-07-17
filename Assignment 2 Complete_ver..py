'''# 6201012620295 
โค้ดนี้สำหรับ Assignment 2 ให้สร้างวงกลม 10 วงโดยใช้ from random import randint เพื่อสุ่ม สี และ รัศมีของวงกลมนั้นๆ
จากนั้นนำเมาท์ไปคลิกวงกรมที่ใหญ่ที่สุดเผื่อให้วงกลมนั้นหายไป

สุ่มการเคลื่อนที่ของวงกลมที่สร้างแล้วให้วงกลมเหล่านั้นสามารถชิ่งได้ ทั้งการชนที่ขอบและการชนกับวงกลมด้วยกันเอง
'''
# Note this Python script requires PyGame.
import pygame 
from random import randint
import math

class Circle:
    def __init__(self):
        # Set up the drawing window (800 x 600 pixels)
        self.scr_w = 800 
        self.scr_h = 600
        # randomize an integer value between 10-20 for the radius
        self.r = randint(10,20)
        # randomize a position (x,y)
        self.x, self.y = randint(self.r,scr_w-self.r), randint(self.r,scr_h-self.r)
        self.x1, self.y1 = randint(self.r,scr_w-self.r), randint(self.r,scr_h-self.r)
        self.ri,self.le= self.x + self.r , self.x - self.r
        self.bot,self.top= self.y + self.r , self.y - self.r
        # random color
        self.colour = (randint(0,255), randint(0,255), randint(0,255))
        # random speed and Direction of Circle 
        self.speed = [randint(1,10),randint(1,10)]


    def Make(self):
            # draw a circle
            pygame.draw.circle( screen, self.colour, (self.x,self.y), self.r )
            # update screen display
            pygame.display.update()


    def Disappear(self):
            # Lap a Circle
            pygame.draw.circle( screen, (0,0,0), (self.x,self.y), self.r )
            pygame.display.update()

def cleck_distant(x,y,rad,x1,y1) :
    if ((x - x1)*(x - x1)) + ((y - y1)*(y - y1)) <= rad**2 :
        return True
    else :
        return False

#Find Maximum of radius in List O
def Max_R(Tar,O):
    b_count = 0
    for k in O:
        if Tar != k:
            if Tar.r > k.r :
                b_count += 1
            elif Tar.r == k.r :
                b_count += 1
    if b_count == len(O) - 1:
        return True
    else:
        return False       
#Bouncing circle when them collision with screen wide or srceen high
def Bouncing(t) :
    t.x += t.speed[0]
    t.y += t.speed[1]
    t.ri += t.speed[0]
    t.le += t.speed[0]
    t.bot += t.speed[1]
    t.top += t.speed[1]
    
    if t.ri >= t.scr_w or t.le <= 0 :
        t.speed[0] *= -1
    if t.bot >= t.scr_h or t.top <= 0 :
        t.speed[1] *= -1
    #Bouncing circle when them collision between circle and circle
    for q in Store_Cr :
        if int(math.hypot(t.x - q.x, t.y - q.y)) <= int(t.r + q.r) :
                t.speed[0] *= -1
                t.speed[1] *= -1
                q.speed[0] *= -1
                q.speed[1] *= -1
    pygame.draw.circle( screen, t.colour, (t.x,t.y), t.r )


# initialize PyGame
pygame.init()

# set window caption
pygame.display.set_caption('Bouning ball') 

# create a clock
clock = pygame.time.Clock()

# Set up the drawing window (800 x 600 pixels)
scr_w, scr_h = 800, 600
screen  = pygame.display.set_mode((scr_w, scr_h))

# create a new surface 
surface = pygame.Surface( screen.get_size(), pygame.SRCALPHA )

All_Cr = []
Store_Cr = []
N = 10
i = 0
a = 0

running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # this loop for remove the circle when you click on the maximum circle only
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for e in Store_Cr :
                if cleck_distant(e.x, e.y, e.r, pos[0], pos[1]):
                    print("Bind Them")
                    if Max_R(e,Store_Cr) :
                        e.Disappear()
                        Store_Cr.remove(e)
                        print("Gone")

    #Genarate circle 10 time
    while a < N:
            All_Cr.append('circle'+str(i))
            All_Cr[i] = Circle()
            draw = True

            for j in range(len(All_Cr)):
            #check all circle class
                if i != j:
                    dist = int(math.hypot(All_Cr[i].x - All_Cr[j].x, All_Cr[i].y - All_Cr[j].y))
                    #if circle overlaped        
                    if dist < int(All_Cr[i].r+All_Cr[j].r):
                        draw = False
            # if circle is not overlapping draw it             
            if draw:
                All_Cr[j].Make()
                Store_Cr.append(All_Cr[j])
                a+=1
            i+=1

    for s in Store_Cr :
        clock.tick(500)
        Bouncing(s)
    # draw the surface on the screen
    pygame.display.update()
    screen.fill((0,0,0))

pygame.quit()