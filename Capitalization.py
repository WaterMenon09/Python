List=[]
x=0
imput=input("Enter String: ")

for i in range(len(imput)):
    if imput[i].isupper()==True:
        List.append(imput[x:i])
        x=i
if imput[x].isupper()==True:
    List.append(imput[x:len(imput)])

List.pop(0)

while len(List)!=10:
    List.append("Empty")
print(List)
