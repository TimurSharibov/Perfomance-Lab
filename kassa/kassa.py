#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Tim
#
# Created:     05.07.2019
# Copyright:   (c) Tim 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

kas=[]
for i in range(5):
   name=input('input name kass ')
   kas.append(name)
n=0
kassa=[]
for file in kas:
    kassa.append([])
    with open(file) as f:
        for line in f:
            for x in line.split():
                k=float(x)
                kassa[n].append(k)
    n+=1

interval=0
max=0
j=0
while j <=15 :
    sum=0
    i=0
    while i<=4:
        sum+=kassa[i][j]
        i+=1
    if max<sum:
        max=sum
        interval=j+1
    j+=1

start = interval/2 - 0.5
end = interval/2
print('maxPeople=',max)
print('interval=',start,'-',end,'oclock')

input()
