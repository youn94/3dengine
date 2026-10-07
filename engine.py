import pygame
import math

sc=pygame.display.set_mode((800, 600))




anglev=0
jx,jy, jz=0, 0, 0
posj=(jx,jy,jz,anglev)
c=True
zez=5

point=[
    (1, 1, zez),
    (-1, 1, zez),
    (-1, -1, zez),
    (1, -1, zez)
    ]

def rotate(x, y, z, angle):
    rad=math.radians(angle)

    cosa=math.cos(rad)
    sina=math.sin(rad)

    x2=x*cosa-z*sina
    z2=x*sina+z*cosa

    y2=y

    return x2, y2, z2

def project(x, y, z):
    
  
            xx=x/z
            yy=y/z
    
            scx=400+xx*300
            scy=300-yy*300
            return scx, scy
            
            

def polygone():
    
    point2d=[]
    for x, y, z in point:
        z=z-jz
        x=x-jx
        y=y-jy
        
        
        x, y, z = rotate(x, y, z, angle=anglev)
        if z<=0.1:
            return
        scx, scy = project(x, y, z)
        point2d.append((scx, scy))
    

    pygame.draw.polygon(sc, 'white', point2d,1)

    ##[(xx*1, xx*3), (xx*2, yy*3), (xx*2, yy*2)]




while c:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            c=False


    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        radius=math.radians(anglev)
        jx+=math.sin(radius)*0.010
        jz+=math.cos(radius)*0.010
        
    if keys[pygame.K_DOWN]:
        radius=math.radians(anglev)
        jx-=math.sin(radius)*0.010
        jz-=math.cos(radius)*0.010
        

    if keys[pygame.K_RIGHT]:
        anglev+=1
    if keys[pygame.K_LEFT]:
        anglev-=1
    

    sc.fill((0, 0, 0))

    
    polygone()

    pygame.display.update()
