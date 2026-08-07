phonebook={}




while True:
    print("1.Add Contacts \n 2.Search Contacts \n 3.Delete Contacts \n 4.Display all contacts \n 5.exit")
    inp=int(input("Enter number:"))
    if inp==1:
        name=input("Enter your name:")
        num=int(input("Enter your Mobile Number:"))
        phonebook.update({name:num})
        
    elif inp==2:
        name=input("Enter name:")
        if name in phonebook:
            print("Number:", phonebook[name])
        else:
            print("Contact not found.")
        
    elif inp==3:
        name=input("Enter name:")
        del phonebook[name]
        print(phonebook)
    elif inp==4:
        phonebook.items()
    elif inp==5:
        break
    else:
        print("Enter correct operation")




    