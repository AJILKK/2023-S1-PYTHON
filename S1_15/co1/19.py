def gcd(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if(x%i==0) and (y%i==0):
            hcf=i
    return hcf
a=int(input("Enter num1:"))
b=int(input("Enter num1:"))
print(gcd(a,b))
