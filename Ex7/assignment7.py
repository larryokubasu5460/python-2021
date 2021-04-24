# phonebook to accept the following in a dictionary
# firstname, middle initial, last name, mailing address, city,country,zip code, email address, phone number
# insert them into a file called contacts.txt for reading/writing
import json
contacts={}
key=0
def listContacts():
    print("="*50)
    print("Listing contacts in text file\n")
    with open("contacts.txt","r") as file:
        print(file.read())
    print("="*50)
    print("Contacts currently in dictionary")
    print(contacts)
    print("="*50)
    file.close()

def addContact():
    contact={}
    fname=input("Fist name: ")
    mname=input("Middle Name: ")
    lname=input("Last Name: ")
    mailingaddr=input("Mailing address: ")
    city=input("City: ")
    country=input("Country: ")
    zipcode=input("Zip code: ")
    email=input("Email address: ")
    phone=input("Phone Number: ")
    contact ={
        'First Name':fname,
        'Middle Initial':mname,
        'Last Name':lname,
        'Mailing Address':mailingaddr,
        'City':city,
        'Country':country,
        'Zip code':zipcode,
        'Email Address':email,
        'Phone Number':phone,
        }
    key=len(contacts.keys())
    key+=1
    contacts[key]=contact
    print("Contact created\n")
    # write to file
    with open("contacts.txt","a+") as file:
        # file.write(fname+" "+mname+" "+lname+"\n"+mailingaddr+" "+city+","+country+","+zipcode+"\n"+email+"\n"+phone+"\n\n")
        json.dump(contacts[key],file,indent=2)
        file.write("\n")
    file.close()

def removeContact():
    key=int(input("Enter Key you want to delete: "))
    if key in contacts:
        # with open("contacts.txt","r") as file:
        #     data=file.readlines()
        # with open("contacts.txt","w") as file:
        #     for line in data:
        #         if line.strip("\n") != contacts[key] :
        #             file.write(line)
        contacts.pop(key)
        print("Contact deleted\n")
    else:
        print("Key not present\n")
    

def updateContact():
    key=int(input("Enter key of contact to update: "))
    if key in contacts:
        choice=input("Update.\n1. First Name\n2. Middle Name\n3. Last Name\n4. Mailing Address\n5. City\n6. Country\n7. Zip Code\n8. Email\n9. Phone Number\nChoose a number of action to perform:  ")
        if choice=="1":
            contacts[key]['First Name']=input("Update First Name: ")
        elif choice=="2":
            contacts[key]['Middle Initial']=input("Update Middle Name: ")
        elif choice=="3":
            contacts[key]['Last Name']=input("Update Last Name: ")
        elif choice=="4":
            contacts[key]['Mailing Address']=input("Update mailing address: ")
        elif choice=="5":
            contacts[key]['City']=input("Update City: ")
        elif choice=="6":
            contacts[key]['Country']=input("Update country: ")
        elif choice=="7":
            contacts[key]['Zip code']=input("Update zipcode: ")
        elif choice=="8":
            contacts[key]['Email Address']=input("Update email: ")
        elif choice=="9":
            contacts[key]['Phone Number']=input("Update phone number: ")
        with open("contacts.txt","a+") as file:
            json.dump(contacts[key],file,indent=2)
            file.write("\n")
    print("\n")

def searchContact():
    key=int(input("Enter key of contact to search: "))
    if key in contacts:
        print(contacts[key])
    else:
        print("Key Missing\n")


options={
    1:listContacts,
    2:addContact,
    3:removeContact,
    4:updateContact,
    5:searchContact
}

def menu():
    """display the actions to be done"""
    print("1. List Phone Numbers\n2. Add a Contact\n3. Remove a Contact\n4. Update a contact\n5. Lookup a contact by Number\nQ. Quit")

def switch(x):
    return options.get(x)()


while True:
    menu()
    print("\n")
    choice=input("Choose action: ")
    if choice=="1":
        switch(1)
    elif choice=="2":
        switch(2)
    elif choice=="3":
        switch(3)
    elif choice=="4":
        switch(4)
    elif choice=="5":
        switch(5)
    elif choice=="Q":
        print("Exiting program")
        break
    else:
        print("Invalid option\n")
        continue





 

