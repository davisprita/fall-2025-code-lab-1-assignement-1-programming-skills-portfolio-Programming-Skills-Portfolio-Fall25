#Brute Force Attack 
#Creating the Variable that stores the password
password="12345"
#5 attempts provided 
Attempts = 5
#Loop for the password input
while Attempts > 0:
    Question=input("Enter The Password:") #Input of Password
    if Question == password:
        print("Correct Paasword!") #Output if the password is right       
    else:
        Attempts -= 1 #After every wrong attempts reduces the amount of attempts avaiable by 1 till 0
        if Attempts > 0:
         print(f'Wrong Paasword, You have {Attempts} attempts left!') # Output for wrong password
        else:
         print("Max attempts reached. The authorities have been informed!") #Final Output when all attempts have been used up 

