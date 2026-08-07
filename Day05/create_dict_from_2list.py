key=["name","age","city"]
val=["khushi","21","Mumbai"]

dict={}

for i in range(len(key)):
    dict.update({key[i]:val[i]})

print(dict)