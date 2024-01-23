lst=[]
n=int(input("Enter the number of elements:"))
print("Enter",n,"values:")
for i in range(n):
    i=int(input())
    lst.append(i)

print("The list is:",lst)
for i in range(n):
    if lst[i]>100:
        lst[i]="over"
print("list after storing 'over'instead of values greater than 100:",lst)