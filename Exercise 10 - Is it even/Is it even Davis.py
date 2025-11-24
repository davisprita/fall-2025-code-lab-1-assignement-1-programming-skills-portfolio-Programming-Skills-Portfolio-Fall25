#Is it even
#This function help to check if the number given is odd or even 
def checker(number):
    if number%2==0:
        return "Number is even" #Output for even number
    else:
        return "Number is odd" #Output for odd number
#This is the main function which uses the above mentioned checker 
def main():
    asknumber=int(input("Enter a number:")) #Input of a number
    results=checker(asknumber) #Checking for odd or even with help of the function 
    print(results) #Displaying the results 
#This helps to call the main function 
if __name__=="__main__":
    main()