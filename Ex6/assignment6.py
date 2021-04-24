# Scholarship programme


# details
fname=input("Enter your first name: ")
lname=input("Enter your last name: ")
full_names=fname+" "+lname
gender=input("Enter gender (M/F):" )
stid=input("Enter student id: ")
physical_address=input("Enter your physical address: ")
city=input("Enter your city: ")
country=input("Enter your country: ")
region=input("Enter your region (A for Africa/O for other)?: ")
email=input("Enter your email: ")
phone=input("Enter your phone: ")
quiz=[]
print("Enter Quiz marks: ")
for i in range(0,3):
    value=int(input())
    quiz.append(value)

test=[]
print("Enter your test results: ")
for i in range(0,2):
    value=int(input())
    test.append(value)
average=((sum(quiz)/len(quiz))+(sum(test)/len(test)))/2

zoom=int(input("Enter number of zoom calls attended: "))
homework=int(input("Enter total number of homeworks done: "))
zoom_points=0
if zoom>2:
    zoom_points=9
else:
    zoom_points=5

# conditions 
# African, average of 80 for males and 76 for females

def award_scholarship(gender,average,region,zoom,homework):
    """Award scholarship based on merit"""
 
    if region=="A":
        # award scholarship
        if gender=="M":
            if (zoom>8 and homework>=8 and average >=80):
                # award scholarship
                scholarship=True
            else:
                scholarship=False
            
        elif gender=="F":
            if (zoom>8 and homework>=7.6 and average >= 76):
                scholarship=True
            else:
                scholarship=False
    
        
    return scholarship

scholarship=award_scholarship(gender,average,region,zoom_points,homework)
print("="*50)
print("Names:",full_names)
print("Student ID:",stid)
print("Email:",email)
print("Contact: ",phone)
print("Country:",country)
print("City:",city)
print("Physical Address:",physical_address)
print(f"Student's Average: {average}%")
print("Student's Region: ",region)
print("Scholarship Awarded: ",scholarship)
print("="*50)


