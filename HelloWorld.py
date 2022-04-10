
for i in range (2,20000):
    a = False
    for j in range (2,i):
        if (i%j==0):
            a = True
            break
    if a==False:
        print(i)