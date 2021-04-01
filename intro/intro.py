names=input("Enter your first and last name: ")
print(names)

# your goals
input_goals=''
goals=[]
print("What are your goals for this class-long term goals?")
while input_goals != "stop":
    input_goals=input()
    
    if input_goals != 'stop':
        goals.append(input_goals)
# print(goals)