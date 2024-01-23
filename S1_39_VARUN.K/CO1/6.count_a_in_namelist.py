lst=[]
x=int(input("Enter the number of names:"))
for i in range(x):
    y=input("Enter Name:")
    lst.append(y)
count=0
for x in lst:
    count+=x.lower().count("a")

print(count)