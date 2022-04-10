#differnce between highest and second highest number
'''highest = int(0)
second = int(0)
for i in range (5):
    s = int(input())
    if (s>highest):
        highest = s
    elif (s>second):
        second = s

print(highest-second)
'''
#leap year

year = int(input())

for i in range (year,year+10):
    if (i%4==0):
        print(i)