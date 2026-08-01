a=int(input("Enter a number:"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if a>b and a>c:
    print(a," is greater than",b,"and",c)
elif b>a and b>c:
    print(b, " is greater than",a,"and",c)
else:
    print(c," is gtreater than ",a," and",b)
    