a=[]
n=int(input("Enter The Number Of Elements In List:"))
for x in range(0,n):
    element=input("Enter Element "+ str(x+1)+":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
        if(len(i)>max1):
            max1=len(i)
            temp=i
print("The Word With Longest Length Is: ")
print(temp)
