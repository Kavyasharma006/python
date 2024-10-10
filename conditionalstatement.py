#conditional statement will check the co
#To check the condition we use if else

'''
#WAP to check user eligible for voting 
userage=int(input("Enter your age="))
# note the default input function return is string 
#for vote userage must be greater than 18
if userage> 18:
    print("You're eligible for voting")
else:
    print("You're not eligible for voting" )

#WAP to check gender
usergender=input("enter your gender=")
if usergender=="female":
    print(" you can sit in first compartment ")
elif usergender=="male":
   print("You can sit in first compartment")
else:
    print("You can sit in any compartment")
     
#WAP if gender is female and age gender is greater than 18 ->govt job apply 
#else male age greater than 18 ->private job apply
if userage>18:
    if usergender== "male":
        print("You can apply for private job")
    elif usergender=="female":
        print("you can apply for govt job")
    else:
        print("Sorry there is no opening")
else:

    print("You are under age")
'''
#For loop is used to no of iteration

username = "Kavya Sharma"
for i in username:
    print(i)

#print 1 to 10 using for loop 
#for (int i;i>11;i++)
for x in range(1,11):
    print(x)

#WAP to create a table of any no 
Tableno= int(input("Enter the table no.:"))
for a in range (1,11):
    print((a *Tableno))

#WAP to print even no from 1 to 10 using for loop
for a in range(1,11):
    if a%2 == 0:
        print(a) 

#WAP print this pattern 1 4 7 10 13 using for loop
for y in range(1,14,3):
    print(y)

#WAP  to print this pattern 1 3 7 11 13 15 using for loop
for t in range(1,16,2):
    if t==9 or t==5:
        continue #skip the cuurent iteration
    else:
        print(t)