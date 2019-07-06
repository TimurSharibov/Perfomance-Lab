#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Tim
#
# Created:     04.07.2019
# Copyright:   (c) Tim 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

nums = []
file=input('input name file: ')
with open(file) as f:
    for line in f:
        for x in line.split():
             k=int(x)
             nums.append(k)

max=nums[0]
min=nums[0]
sum=0
for i in nums:
    sum+=i
    if i>max:
        max=i
    elif i<min:
        min=i
print("max=",max)
print('min=',min)
print("averege=", sum/(len(nums)))

snums=sorted(nums)

n = len(nums)*0.9
if n%1==0:
   percentil=snums[int(n-1)]
else:
    percentil=(snums[int(n)]-snums[int(n-1)])*0.9+snums[int(n-1)]

print("90 persentil=",percentil)

if len(nums)%2!=0:
  n=len(nums)*0.5//1
  median=snums[int(n)]
else:
  n=len(nums)*0.5//1
  median=(snums[int(n-1)]+snums[int(n)])/2
print("median=",median)

input()
