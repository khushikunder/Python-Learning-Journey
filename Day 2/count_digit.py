str=input("Enter a statement:")
count=0

for char in str:
    if char.isdigit():
        count+=1

print("Number of digits=",count)
