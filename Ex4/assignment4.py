# you have been hired as a senior programmer
# your job is to design a simple program to allow the loan officers to enter the customer particulars at the terminal and determine if a customer is
#credit worthy. Based on their loan officers entry, your system is required to get the best desired output 

# Enter the price of the house you wish to buy
CreditScore = 0
price = 0 
downPayment =  0
creditStatus=""
price=float(input("Enter the house price: "))
# Enter the first name
first_name=input("Enter the first name: ")
# Enter the last name
middle_name=input("Enter your middle name: ")
last_name=input("Enter the last name: ")
full_name=first_name + " "+middle_name+" "+ last_name
CreditScore=int(input("Enter your credit rating: "))
# enter the email
email=input("Enter the email address: ")
# Enter the phone number
phone=input("Enter the phone number: ")
# Enter the mailing
physical_address=input("Enter your mailing address: ")
city=input("Enter the city: ")
zipcode=input("Enter the zipcode: ")


# Qualify for loans with the best interest rates
if (CreditScore >=780 and CreditScore <= 850):
    creditStatus="Excellent Credit"
    # print("Zero down payment")
    downPayment = 0.10*price

# usually qualify for loans with the best interest
elif(CreditScore >=740 and CreditScore <= 779):
    creditStatus="Very good"
    downPayment=0.1*price

# May face slightly higher loan interest
elif(CreditScore >= 720 and CreditScore <=739):
    creditStatus="Above average"
    downPayment =0.3*price

# may qualify for loans of higher interest rates
elif(CreditScore >= 680 and CreditScore <=719):
    creditStatus="Average"
    downPayment=0.6*price

# may qualify for most loans at significant higher interest rates
elif(CreditScore>=620 and CreditScore <= 679):
    creditStatus="Below average"
    downPayment =0.18*price

# usually has some credit issues; will probably not qualify for most loans
elif(CreditScore>=580 and  CreditScore <= 619):
    creditStatus="Poor credit score"
    downPayment =0.20*price

# facing extreme credit issue

elif(CreditScore<520):
    creditStatus="Poor credit score"
    downPayment = 0.25*price

# program output
print("\n\n\n")
print("="*50)
print("Full Names: ", full_name)
print("Contact: ",phone)
print("Physical address: ",physical_address)
print("City: ",city)
print("Zipcode: ",zipcode)
print("\n")
print("New House Price: ",price)
print("Down Payment: ",downPayment)
print("Credit Score: ",CreditScore)
print("Credit Status: ", creditStatus)
print("="*50)