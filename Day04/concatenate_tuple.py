tup1=(45,8,96,26,43,98,85)
tup2=(78,85,96,12,34,45)

# 1st way
tup=tup1 +tup2
print(tup)

#2 way

result=()

for i in tup1:
    result+=(i,)

for i in tup2:
    result+=(i,)

print(result)
