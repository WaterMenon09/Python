import time
def ISBN13(x):
    a=int(x[0])
    b=int(x[1])
    c=int(x[2])
    d=int(x[3])
    e=int(x[4])
    f=int(x[5])
    g=int(x[6])
    h=int(x[7])
    i=int(x[8])
    j=int(x[9])
    k=int(x[10])
    l=int(x[11])

    returnvalue=str(10-(((a+c+e+g+i+k)+(b+d+f+h+j+l))%10))
    if returnvalue=="10":
        return "0"
    else:
        return returnvalue

def ISBN13check(x):
    if ISBN13(x)==(x[12]):
        return True
    else:
        return False

def valid(x):
    if numbers(x):
        if len(x)==12:
            return True
        elif len(x)==13:
            return True
        else:
            return False
    else:
        return False

def numbers(x):
    if x.isnumeric():
        return True
    else:
        return False

while True:
    x=str(input("Enter the ISBN13 code: "))
    while True:
        if valid(x):
            break
        else:
            print("This is not a valid input.")
            z=len(x)
            print("You have entered",z,"numbers instead of 12 or 13.")
            
            x=str(input("Please re-enter correct ISBN13 code: "))
    y=ISBN13(x)
    if len(x)==12:
        print("The check digit of "+x+" is "+y+".")
        print("Resulting in :",x+y,".")
    elif len(x)==13:
        if ISBN13check(x):
            print("The ISBN13 code is correct!")
        else:
            print("This ISBN13 code is wrong")
            print("If you have the check digit wrong the the correct digit will be",y,".")
            print("Resulting in",x[0:12]+y)
    a=str(input("Do you want to continue? (y/n): "))
    if (a=="y")or(a=="Y"):
        continue
    else:
        print("Thank you for using this program")
        break
time.sleep(1.5)
