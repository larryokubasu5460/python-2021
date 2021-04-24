# Fix the program
# Enter full names
# print("Enter first and last name")
fname=input("Enter your first name: ")
mname=input("Enter your middle name: ")
lname=input("Enter your last name: ")
fullnames=fname+ " "+mname+" "+lname

# Enter your phone, email
phone=input("Enter customer's phone Number: ")
email=input("Enter customer's email address: ")

# price of used car
price=10000
has_good_credit=True;

if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price

print("\n")
# print(f"Down payment: {down_payment}")
print("Full Names: ",fullnames)
print("Phone: ",phone)
print("Email: ",email)
print("Down Payment:", down_payment)