#Biography
#Input of info from user 
Name=input("Enter Your Full Name:")#Input of Both 1st and 2nd Name Accpected 
Hometown=input("Enter your Hometown:")#Input of town of origin 
#Solving the string value for age
while True:
    Age=input('Enter Your Age:')#Input of Age
    if Age.isdigit():#I found the function isdigit though Google 
        Age=int(Age)
        break
    else:
        print('Please enter a vaild number for Age!.')
print()#For ease of visualizing while displaying
#Storing the information (Name,Hometown and Age) in a dict.
Bio={"Name":Name,"Hometown":Hometown,"Age":Age}
#Displaying the stored info from the dict above 
print(f"Name:{Bio['Name']}\nHometown: {Bio['Hometown']}\nAge: {Bio['Age']}")