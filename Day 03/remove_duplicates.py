item=[95,45,86,32,79,53,84,53,86,95,32]
unique=[]

for num in item:
    if num not in unique:
        unique.append(num)

print(unique)