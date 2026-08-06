item=[95,45,86,32,79,53,84,53]
small=item[0]

for char in item:
    if char<=small:
        small=char
print(small)