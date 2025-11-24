#Primitive Quiz
#List of countrys
Country=["UK","France","Belgium","Netherlands","Germany","Poland","Italy","Greece","Spain","Portugal"]
#List of caps 
Capitals=["London","Paris","Brussels","Amsterdam","Berlin","Warsaw","Rome","Athens","Madrid","Lisbon"]
#Loops for all the questions
for i in range(10):
    Question=input("What is the capital of " + Country[i] + ":" ) #Question that will be displayed 
    if Question.lower()== Capitals[i].lower(): #Making it accpect both upper and lower case answers
        print("Correct!") #For correct answer 
    else:
        print("Wrong Answer!") #For Wrong anwer 