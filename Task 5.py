def fact(n):
    if n<2:
        return(1)
    else:
        return n*fact(n-1)

x=int(input("Enter number"))
f=fact(x)
print(f"factorial of {x} is {f}")
