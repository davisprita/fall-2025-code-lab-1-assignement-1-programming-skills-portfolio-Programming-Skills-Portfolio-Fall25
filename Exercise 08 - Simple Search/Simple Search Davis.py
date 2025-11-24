#Simple Search 
#List of names 
Names=("Jake","Zac","Ian","Ron","Sam","Dave")
#Input from the user
Search=input("Enter name to search:-")
#Checks if the input given by the user is found in the list Names
if Search in Names:
    print(f"The name {Search} was found in the list!") #Output if the is Name found
else:
    print(f"The name was NOT found in the list") #Output if the Name is not found