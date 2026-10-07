import pygame
import math

sc=pygame.display.set_mode((800, 600))




anglev=0
jx,jy, jz=0, 0, 0
posj=(jx,jy,jz,anglev)
c=True


point=[
    (1, 1, 5),
    (-1, 1, 5),
    (-1, -1, 5),
    (1, -1, 5)
    ],[
    (1, 1, 7),
    (-1, 1, 7),
    (-1, -1, 7),
    (1, -1, 7)
    ],[
    (-1, 1, 5),
    (-1, 1, 7),
    (-1, -1, 7),
    (-1, -1, 5)
    ],[
    (1, 1, 7),
    (1, 1, 5),
    (1, -1, 5),
    (1, -1, 7)
    ],[
    (1, 1, 5),
    (1, 1, 7),
    (-1, 1, 7),
    (-1, 1, 5)
    ],[
    (1, -1, 5),
    (-1, -1, 5),
    (-1, -1, 7),
    (1, -1, 7)
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
            
            

def polygone(point, normal):
    cx=sum(p[0] for p in point)/4
    cy=sum(p[1] for p in point)/4
    cz=sum(p[2] for p in point)/4

    vx=jx-cx
    vy=jy-cy
    vz=jz-cz

    nx, ny, nz=normal
    vis=nx*vx+ny*vy+nz*vz
    if vis<=0:
        return


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
    
    lumiere=(0, 1, 0)

    x1, y1, z1 =normal
    lum=x1*lumiere[0]+y1*lumiere[1]+z1*lumiere[2]
    lum=0.2+0.8*max(0, lum)
    color=(
         int(255*lum),
            int(255*lum),
            int(255*lum)

             )
    pygame.draw.polygon(sc, color, point2d,0)

    ##[(xx*1, xx*3), (xx*2, yy*3), (xx*2, yy*2)]

def cube():
    polygone(point[0],(0,0,-1))
    polygone(point[1],(0,0,1))
    polygone(point[2],(-1,0,0))
    polygone(point[3],(1,0,0))
    polygone(point[4],(0,1,0))
    polygone(point[5],(0,-1,0))



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

    if keys[pygame.K_w]:
        jy+=0.010
    if keys[pygame.K_s]:
        jy-=0.010

    if keys[pygame.K_RIGHT]:
        anglev+=1
    if keys[pygame.K_LEFT]:
        anglev-=1
    

    sc.fill((0, 0, 0))

    
    cube()

    pygame.display.update()
