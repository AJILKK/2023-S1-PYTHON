a=int(input("Enter 3 Numbers:"))
b=int(input())
c=int(input())
if(a>b and a>c):
    print(a,"is Largest")
else:
    if(b>c):
        print(b,"is Largest")
    else:
        print(c,"is Largest")