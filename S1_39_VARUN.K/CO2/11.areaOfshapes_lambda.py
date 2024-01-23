print("Enter shape you want to calculate area")
print("1.Rectangle 2.Square 3.Triangle")
shape=int(input("Select the Number:"))
if shape==1:
    rect=lambda l,b:l*b
    l=float(input("Enter the Length:"))
    b=float(input("Enter the breadth:"))
    print("Area of Rectangle is:",rect(l,b))
elif shape==2:
    square=lambda a:a*a
    a=float(input("Enter the side:"))
    print("Area of Square is:",square(a))
elif shape==3:
    tri=lambda b,h:.5*b*h
    b=float(input("Enter the Base:"))
    h=float(input("Enter the Height:"))
    print("Area of Triangle is:",tri(b,h))
else:
    print("Wrong choice")
