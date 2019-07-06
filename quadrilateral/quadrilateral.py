#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Tim
#
# Created:     06.07.2019
# Copyright:   (c) Tim 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# quadrilateral_point.txt
class Coord:
    def __init__(self,x,y):
        self.x=x
        self.y=y
vertex=[]
file=input('input name file: ')
with open(file) as f:
    for line in f:
         x = line.split()
         vertex.append(Coord(int(x[0]),int(x[1])))

xp=int(input('coord point x='))
yp=int(input('coord point y='))

d=[]

#   D = (x2 - x1) * (yp - y1) - (xp - x1) * (y2 - y1)

d.append((vertex[1].x - vertex[0].x) * (yp - vertex[0].y) - (xp - vertex[0].x) * (vertex[1].y - vertex[0].y))
d.append((vertex[2].x - vertex[1].x) * (yp - vertex[1].y) - (xp - vertex[1].x) * (vertex[2].y - vertex[1].y))
d.append((vertex[3].x - vertex[2].x) * (yp - vertex[2].y) - (xp - vertex[2].x) * (vertex[3].y - vertex[2].y))
d.append((vertex[0].x - vertex[3].x) * (yp - vertex[3].y) - (xp - vertex[3].x) * (vertex[0].y - vertex[3].y))

count=0
index=0
for i in range(len(d)):
    if d[i]==0:
        count+=1
    elif d[i]<0:
        index+=1

if index==4:
    print('point in quadrilateral')

elif count==1:
    print('point in edge')

elif count==2:
    print('point in vertex')

else :
    print('point outside ')

input()
