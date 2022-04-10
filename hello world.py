
def singular(x,y,z):
    if (x<y and x<z):
        return True;
    else:
        return False;

x = int(input("Enter X: "))
y = int(input("Enter Y: "))
z = int(input("Enter Z: "))

singular(x,y,z);
