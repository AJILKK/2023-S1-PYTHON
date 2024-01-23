string=input("Enter the string:")
list=string.split(" ")
for i in list:
    print(i,"-",list.count(i))