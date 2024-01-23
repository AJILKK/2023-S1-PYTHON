clr=input("Enter comma seperated colors:")
clrs=clr.split(",")
lst=list(clrs)
print("colours:",lst)
f=lst[0]
l=lst[-1]
print("First colour:",f)
print("Last colour:",l)