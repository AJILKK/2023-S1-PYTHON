n=int(input("Enter a Number:"))
fact=1
if n<0:
    print("invalid number")
elif n==0:
    print(0,"!=",fact)
else:
    for i in range(1,n+1):
        fact=i*fact
    print(n,"!=",fact)