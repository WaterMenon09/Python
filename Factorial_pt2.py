Input = int(input())

if (Input==0):
    print(1)

ans = int(1)

for i in range (1,Input+1):
    ans=ans*i


i = int(1)

while (i<=Input):
    ans=ans*i
    i=i+1

print(ans)
