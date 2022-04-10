def isPrime(x):
    if x==1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True

if __name__ == "__main__":
    print("Find Prime Factors:")
    while True:
        Input = OG = int(input("Enter a positive integer (or 0 to stop): "))
        if Input==0:
            print("Goodbye!")
            break
        elif Input==1:
            print("  1 has no prime factorization.")
        elif Input<0:
            print("  Negative integer entered.  Try again.")
        elif isPrime(Input):
            List = [Input]
            print("  The prime factorization of", OG, "is:" ,List)
        else:
            List = []
            i = int(2)
            while Input>1:
                if Input%i==0:
                    List.append(i)
                    Input=Input/i
                else:
                    i+=1
            print("  The prime factorization of", OG, "is:" ,List)
        print(" ")