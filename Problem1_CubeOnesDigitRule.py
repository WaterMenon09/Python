def followsRule(num):
    num = num*num*num
    ans = num%10
    if ans<5:
        return True
    else:
        return False

def rangeOfNums(lower,upper):
    count = int(0)
    for i in range (lower,upper+1):
        if followsRule(i):
            count+=1
    return count

print(rangeOfNums(0,28))