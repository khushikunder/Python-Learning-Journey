str=input("Enter a string:")
count=0

for char in str:
    if char.islower():
        count+=1

print(count)