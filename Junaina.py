'''eggs = int(input())
sugar = float(input())
flour = float(input())

eggs = eggs//4
sugar = sugar//1.3
flour = flour//2.9

batches = eggs

if sugar<batches:
    batches = sugar
if flour < batches:
    batches = flour
print(int(batches))


move = "a"
coin = int(0)
life = int(0)

while move != "end":
    move = input()
    if (move == "large box"):
        coin += 50
    elif (move == "small box"):
        coin += 20
    elif (move == "goomba"):
        coin = 0
        
    if coin>=100:
        coin-=100
        life+=1

print(life)
print(coin)


hour = int(input())
minute = int (input())
AP = input()

if (AP=="p"):
    hour += 12
if (hour<10 or hour==12):
    print("Too Early!")
elif (hour==16 and minute>30):
    print("Too Late!")
elif (hour>16):
    print("Too Late!")
else:
    print("Perfect Timing!")


# Johnny is me
n = int(input())
cost = int(0)
rank = int(-1)
for i in range (n):
    toy = float(input())
    if (toy<=20.0):
        if (toy>cost):
            rank=i+1
            cost=toy
print(rank)

print(ord("a"))
print(ord("A"))

A =input()
B =input()

a = A.lower()
b = B.lower()

if ord(a)<ord(b):
    print(A)
elif ord(b)<ord(a):
    print(B)
else:
    if(ord(A)>ord(B)):
        print(A)
    else:
        print(B)

import math
k = float(input())
t = int(input())
i = int(1)
ans = float(0)

while i<=t:
    ans += math.sqrt((2*i*i)/(i+1))
    i+=1

if (ans<=k):
    print("%.3f" %ans)
else:
    print("TOO BIG!")

luck = int(0)

for i in range (5):
    card=int(input())
    if card==0:
        luck=luck*2
    elif card%2==0:
        luck+=card
    else:
        luck-=3

print(luck)


card = prev = input()
score = int(0)
while (card!="X"):
    card =input()
    if (card!="0" or card!="1" or card!="2" or card!="3" or card!="4" or card!="5" or card!="6" or card!="7" or card!="8" or card!="9"):
        if (card==prev):
           score+=1
        elif (card=="A" and prev=="K")or(card=="K" and prev=="A"):
           score+=1
        elif (card=="K" and prev=="Q")or(card=="Q" and prev=="K"):
           score+=1
        elif (card=="J" and prev=="Q")or(card=="Q" and prev=="J"):
           score+=1
    prev = card
print(score)
