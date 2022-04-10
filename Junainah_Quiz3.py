def condensedCommunication(str):
    Output = ""
    for i in str:
        if i.isupper()==False:
            Output=Output+(i)
        else:
            Output=Output+(i.lower())
    Output2=""
    for i in Output:
        if i.islower() or i.isnumeric():
            Output2=Output2+i
    return Output2

def adjacentDifferences(first):
    second = []
    for i in range (len(first)-1):
        second.append(first[i+1]-first[i])
    return second
