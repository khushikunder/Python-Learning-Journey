str=input("Enter a string:")
words=str.split()
longest=""

for word in words:
    if len(word)>=len(longest):
        longest=word

print("The longest word is:",longest)