subject=["python","java","c++","python","javascript","java","python","java","c++","c"]

dup=set(subject)
print(dup)
count=0
for i in dup:
    count+=1

print("Number of classrooms needed by student is:",count)