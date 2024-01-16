#I Jay Patel, 000881881, certify that this work is my own effort and that I have allowed anyone else to copy from it.

#Question 1A: pH meter

def question1A(ph):
    if (ph < 4):
        return ("Substance is very Acidic.")
    elif (ph >= 4) and (ph < 7):
        return ("Substance is Acidic.")
    elif ph > 10:
        return ("Substance is very Alkali.")
    elif (ph <= 10) and (ph > 7):
        return ("Substance is Alkali.")
    else:
        return ("Substance is Neutral.")

print("Running solution to question 1A ...")
ph=float(input("Enter ph of substance: "))

x=question1A(ph)
print(x)



