def palindrome(x):
    if reverse(x,lower())==x.lower():
        return True
    else:
        return False

def reverse(x):
    if len(x)==0:
        return x
    return (x[len(x)-1]+reverse(x[0:len(x)-1]))

x=str(input("Enter a word that you think is Palindrome: "))
if palindrome(x):
    print(x," is a Palindrome!")
else:
    print(x," is not a Palindrome, sorry.")
    print("The correct Palindrome of ",x," is ",reverse(x),".")

