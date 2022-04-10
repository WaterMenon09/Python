def best(A,B):
    if (len(A)>len(B)):
        return 1
    elif (len(A)<len(B)):
        return 2
    else:
        negA=negB=0
        for i in A:
            if (A[i]<0):
                negA+=1
        for i in B:
            if (B[i]<0):
                negB+=1
        if (negA<=negB):
            return 3
        elif (negA>negB):
            return 4

print(best([-2,3,-11,3,5],[5,-5,-3,0]))
