age_of_adults=[4,12,10,23,25,56,77,11,34,75]
adults_only=list(map(lambda age: (age>17), age_of_adults))
age_list=list(filter(lambda age: (age>17),age_of_adults))
print("Adults Only: ",adults_only)
print("Ages: ",age_of_adults)
print("Adults Only values: ",age_list)