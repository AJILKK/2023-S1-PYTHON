current_year = int(input("Enter the current year:"))
future_year = int(input("Enter the final year:"))
if (current_year<future_year):
    print("The Leap years from",current_year,"to",future_year,"are")
    for year in range(current_year,future_year+1):
        if(year%4==0 and year%100!=0):
            print(year)
else:
    print("No future Leap years found")
