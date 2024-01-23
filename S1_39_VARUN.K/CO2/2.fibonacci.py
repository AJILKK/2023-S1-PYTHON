n=int(input("How many terms:"))
a=0
b=1
for i in range(1,n+1):
    sum=a+b
    a=b
    b=sum
    print(a)