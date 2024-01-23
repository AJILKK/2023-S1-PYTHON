str1=input("Enter a word:")
str2="ing"
if str2 not in str1:
    s=str1+str2
else:
    s=str1+"ly"
print(s)