item1=[95,45,86,32,79]
item2=[53,84,53,86,95,32]

unique=[]

for char in item1:
    if char in item2:
        unique.append(char)

print(unique)