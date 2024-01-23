n=int(input("Enter a number:"))
print("The factors of number",n,"is:")
for i in range(1,n):
     if(n%i==0):
         print(i)
