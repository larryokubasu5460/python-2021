# design a program to convert 
# 1. Temperature from Fahrenheit to Celsius and bac;
# 2. Convert Nautical miles to KMS and back
# 3. Convert Kilometer to Miles and back
# 4. Convert centimeters to meters and back
# 5. Convert yard to meters and back
# 6. Convert inches to centimeters and back
# Your program should be menu driven with options to pick from the running program

# temperature
def celsius():
    temp=float(input("Fahrenheit temperature: "))
    fahr=(temp-32)*5/9  
    return print("Celsius Temperature: ",fahr)

     
def fahrenheit():
    celsius=float(input("Celsius temperature:"))
    temp=(celsius*9/5)+32
    return print("Fahrenheit Temperature:",temp)

def kilometres():
    miles=float(input("Miles: "))
    dist=miles*1.609 
    return print("Kilometeres:",dist) 

def miles():
    km=float(input("Kilometers:"))
    dist=km/1.609
    return print("Miles:",dist)

def centimetres():
    metres=float(input("Metres:"))
    dist=metres*100
    return print("Centimetres:",dist)

def metres():
    cm=float(input("Centimetres:"))
    dist=cm/100
    return print("Metres:",dist)

def metres2():
    yard=float(input("Yards:"))
    dist=yard/1.094
    return print("Metres:",dist)

def yard():
    metres=float(input("Metres:"))
    dist=metres*1.094
    return print("Yard:",dist)

def centim():
    inch=float(input("Inches:"))
    dist=inch*2.54
    return print("Centimetres:",dist)

def inches():
    cm=float(input("Centimetres:"))
    dist = cm/2.54
    return print("Inches:",dist)


options = {
    1:celsius,
    2:fahrenheit,
    3:kilometres,
    4:miles,
    5:centimetres,
    6:metres,
    7:metres2,
    8:yard,
    9:centim,
    10:inches   
}

def switch(x):
    return options.get(x, "Invalid option")()
def menu_options():
    print("Options:\n[P] Print Options\n[C] Convert from Celsius\n[F] Convert from Fahrenheit\n[M] Convert from Miles\n[KM] Convert from Kilometres\n[IN] Convert from inches\n[CM] Convert from Centimetres\n[Y] Convert from Yards\n[MT] Convert from Metres\n[CMM] Convert from Centimetres\n[Q] Quit")

while True:
    menu_options()
    choice=input("Choose action: ")
    if choice=="P":
        menu_options()
    elif choice=="C":
        switch(2)
    elif choice=="F":
        switch(1)
    elif choice=="M":
        switch(3)
    elif choice=="KM":
        switch(4)
    elif choice=="IN":
        switch(9)
    elif choice=="CM":
        switch(10)
    elif choice=="Y":
        switch(7)
    elif choice=="MT":
        switch(8)
    elif choice=="CMM":
        switch(6)
    elif choice=="Q":
        print("Exiting program")
        break
    else:
        print("Invalid option")
        continue
    

    



