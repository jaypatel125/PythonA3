#I Jay Patel, 000881881, certify that this work is my own effort and that I have allowed anyone else to copy from it.

#Question 2: ph:question1A

from Q1A import question1A
while True:
    print("Running solution to question 1a ...")
    ph= input("Enter pH of substance: ")

    if str(ph)== "quit":
        break
    if (float(ph) <= 0.0) or (float(ph)>14) :
        print ("input should be valid floating point decimal positive number between 0 and 14. ")
    else:
        answer=question1A(float(ph))
        print( "The answer is: " + answer ) 
        
