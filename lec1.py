# is used to comment the line 
# is used to define the code meaning
# it can also comment and uncomment multiple lines using ctrl +/

#comments example
# write a program to print your name 
print("Kavya Sharma") # print function to display statement 

#Variables can store the value and it can change at any time 
name="Kavya Sharma"
#pass the variable in the print function 
print("My name is "+name) #+ is used to concrete the string

# declare and initialize the multiple variables  
age=20
gender="Female"
email="kavyanushka6@gmail.com"
#pass the multiple variables in print function
# print("My name is "+ name+
#        "My age is ",age, "My gender is "+gender)
"""
#solution 1 -int variable + replace by ,
 print("My name is "+ name+
 "My age is ",age, "My gender is "+gender)

#solution 2-enclosed the variable inside the string statement using f 
#pass the variable int{}
print(f"my name is {name} my age is {age} my gender is {gender} my email is {email}")

#solution 3-using typecasting 
ageinstring=str(age)
print("My name is "+ name+
 "My age is ",ageinstring, "My gender is "+gender)

"""
#Data types in python
print(type(name))#type function return datatype of variable
print(type(age))
#1. str-> it can store the string data e.g.-"pawan sharma"
#2. int->it can store the numeric data e.g.- age=12
#3. float-> it can store the decimal no. e.g. percentage=78.34

#Typecasting in python:-convert one data type into another data type
#e.g. sometime we purchase item in float we paid in integer
purchaseitemprice= 90.32
paiditemprice= float(purchaseitemprice)
print("Paid amount is ",paiditemprice)

#note->string can't be converted into int reason string not ascii
'''
#To get the input from user using input() function
Collegename= input("Enter your college name ")
Collegefee= int(input("Enter your college fee "))
print("My college name is "+ Collegename ,Collegefee )
#Note:- teh input function has default return type str
#add scholarship of 25000 in fee
Collegefee= Collegefee-25000
print("after scholarship my fee",Collegefee)
'''
#Find the age in year when born year and current year given by user
Currentyear=int(input("Enter your current year "))
bornyear=int(input("Enter your born year"))
age =Currentyear-bornyear
print("Your age is:",age)

#currency convertor
dollar=float(input("Enter the dollar: "))
rupees=dollar*83.54
print(dollar,"Dollar is Indain rupees",rupees)


