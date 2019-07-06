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


class Visitor:
    def __init__(self,time,action):
        self.time=time
        self.action=action

schuedle=[]
schuedle.append(Visitor('08:00',0))

file=input('input name file: ')
with open(file) as f:
    for line in f:
        for x in line.split():
            k=str(x).split('-')
            schuedle.append(Visitor(k[0],+1))
            schuedle.append(Visitor(k[1],-1))

schuedle.append(Visitor('20:00',0))

schuedle.sort(key=lambda x: x.time, reverse=False)

class maxlimit:
    def __init__(self,maxtime,mintime,count):
        self.maxtime=maxtime
        self.mintime=mintime
        self.count=count

max=maxlimit('20:00','08:00',0)

countPeople=0
for i in range(len(schuedle)):
    countPeople+=schuedle[i].action
    if countPeople>max.count:
        max.count=countPeople
        max.mintime=schuedle[i].time
        max.maxtime=schuedle[i+1].time

print('max count People =',max.count)
print('period time', max.mintime,'-',max.maxtime)

input()