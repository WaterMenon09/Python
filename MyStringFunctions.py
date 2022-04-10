def myAppend(str,ch):
    return str+ch
    #done

def myCount(str, ch):
    count = 0
    for i in str:
        if i==ch:
            count+=1
    return count
    #done

def myExtend(str1,str2):
    str2 = str1+str2
    return str2
    #done

def myMin(str=None):
    if str==None:
        print("Empty string: no min value")
        return None
    else:
        min = str[0]
        for i in str:
            if ord(i)<ord(min):
                min = i
        return min
    #done

def myInsert(str, i, ch):
    var = ""
    if i>len(str):
        print("Invalid index")
        return None
    else:
        j = 0
        while j<i:
            var+=str[j]
            j+=1
        var+=ch
        for x in range (i,len(str)):
            var+=str[x]
        return var
    #DONE

def myPop(str,i):
    var = ""
    for j in range (len(str)):
        if i!=j:
            var+=str[j]
    return var,str[i]
    #done

def myFind(str,ch):
    for i in range (len(str)):
        if str[i]==ch:
            return i
    return -1
    #done

def myRFind(str,ch):
    found = -1
    for i in range (len(str)):
        if str[i]==ch:
            found = i
    return found
    #done

def myRemove(str,ch):
    var = ""
    found = False
    for i in str:
        if found or ch!=i:
            var+=i
        if i==ch:
            found=True
    return var
    #done

def myRemoveAll(str,ch):
    var = ""
    for i in str:
        if i!=ch:
            var+=i
    return var
    #done

def myReverse(str):
    var = ""
    for i in str:
        var=i+var
    return var
    #done
