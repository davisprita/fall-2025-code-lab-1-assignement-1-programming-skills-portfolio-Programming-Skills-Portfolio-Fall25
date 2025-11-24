#Days of the Month 
#Creating the dict for the days in each month
Days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
#Input of the Month Number
months=int(input("Enter the Month Number: "))
if months == 2:
    ly=input("Is it a leap year (Yes/No)?") #Asking if the year is leap year or not 
    if ly.lower() =="Yes".lower():
      print("The Month has 29 Days") #Output if yes
    else:
       print("The Month has 28 Days") #Output if no 
elif months in Days:
   print("The month has",Days[months], "Days") #Output for the rest of the months 
else:
   print("Invaild Month Number") #Output if an invaild month number been entered 