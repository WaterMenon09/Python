# divide two numbers and check whether the divisibal is a fraction or not, and also if there is a remaider, check whehter remainder is even.

a = int(input())
b = int(input())

ans = a%b

if (ans==0):
    print("Divisibal is not a fraction")
else:
    if (ans%2==0):
        print("remainder is even")
    else:
        print("remainder is odd")