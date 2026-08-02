str=input("Enter a string:")
count =0

for char in str.lower():
    if char not in 'aeiou':
        count +=1

print(count)