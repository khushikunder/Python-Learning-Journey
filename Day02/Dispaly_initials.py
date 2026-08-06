str=input("Enter your full name:")
spli=str.split()
initial=""
for char in spli:
    initial+=char[0]

print(initial.upper())