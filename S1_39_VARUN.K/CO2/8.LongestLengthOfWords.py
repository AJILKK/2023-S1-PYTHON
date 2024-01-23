def longestLength(words):
    res=max(words,key=len)
    print("The word with the longest length is:",res,"and length is",len(res))
lst=[]
a=input("Enter words seperated by space:")
lst=a.split(" ")
longestLength(lst)
