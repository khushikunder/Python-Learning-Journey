str=input("Enter a string:")

count=0
for char in str.lower():
    if char in 'aeiou':
        count+=1

print(count)
