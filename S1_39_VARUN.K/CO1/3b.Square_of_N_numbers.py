n=int(input("Enter the limit of numbers you want to find the square:"))
list1=[x**2 for x in range(n+1)]
print("The Square of numbers till",n,"is:",list1)