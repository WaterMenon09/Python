def fact(x):
    ans = int(1)
    for i in range(1, x + 1):
        ans = ans * i
    if x == 0:
        return 1
    return ans

n = int(input("Enter n: "))
m = int(input("Enter m: "))
c = int(input("Enter c: "))

eqn = float((fact(n)*(n-fact(n)))/(fact(m)+(c-2*2*fact(c))))
print(eqn)

print("Factorial of n: ", fact(n))
print("Factorial of m: ", fact(m))
print("Factorial of c: ", fact(c))
