word=input("Enter the word:")
vowel="aeiouAEIOU"
print("Word:",word)
list1=[x for x in word if x in vowel]
print("The vowels in the words are",list1)