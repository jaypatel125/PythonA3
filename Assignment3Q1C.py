#I Jay Patel, 000881881, certify that this work is my own effort and that I have allowed anyone else to copy from it.
#Question 1C: Valid Triangle and type

def question1C(a,b,c):
   
    if (a==b) and (b==c) and (a==c):
        return ("Triangle is valid. This is an equilateral triangle.")
    elif (a==b) or (b==c) or (a==c):
        return ("Triangle is valid. This is an isosceles triangle.")
    elif(a+b > c) and (b+c > a) and (a+c > b):
        return ("Triangle is valid. This is a scalene triangle.")
    else:
        return ("Triangle is not valid.")

print("Running solution to question 1C ...")
a=int(input("Enter lenth of side a: "))
b=int(input("Enter lenth of side b: "))
c=int(input("Enter lenth of side c: "))

z=question1C(a,b,c)
print(z)
