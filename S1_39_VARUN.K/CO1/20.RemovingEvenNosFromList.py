list=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    value=int(input("Enter the numbers:"))
    list.append(value)
print("list:",list)
odd_list=[x for x in list if x%2!=0]
print("The list after  removing even numberes:",odd_list)