#I Jay Patel, 000881881, certify that this work is my own effort and that I have allowed anyone else to copy from it.
#Question 1B: habitable

def question1B(temp):
    if (temp > 0) and (temp <21):
        return ("Liquid water can be present, crops can not grow and We could not consider the planet habitable. ")
    elif (temp >= 21) and (temp <= 32):
        return ("Liquid water can be present, crops can grow and We could consider the planet habitable. ")
    elif  (temp > 32) and (temp <100):
        return ("Liquid water can be present, crops can not grow and We could not consider the planet habitable. ")

print("Running solution to question 1B ...")
temp=float(input("Enter temprature of planet: "))

y=question1B(temp)
print(y)
    
