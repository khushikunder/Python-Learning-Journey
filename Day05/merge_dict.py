info1={'name': 'khushi', 'age': 21, 'city': 'mumbai', 'cgpa': 8.7}
info2={'surname': 'kunder', 'DOB': "20 Nov"}

info={}

for key,value in info1.items():
    info.update({key:value})

for key,value in info2.items():
    info.update({key:value})

print(info)
