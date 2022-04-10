import math

content = dir(math)
print(content)
while True:
    userID = input("Enter the userID: ")
    if len(userID) != 7:
        print("Error! Need exactly 7 letters.")
    else:

        x=(userID.isupper())
        y=(userID.isnumeric())
        print(x)
        print(y)
        if x == False:
            print("Error! First 4 letters need to be in uppercase.")
        else:
            if y == False:
                print("Error! Last 3 letters need to be numeric.")
            else:
                print("Login Successful!")
                break
