#function can perform any task
#it can be reuse,function will return result

#create function to print the name 
def printname():
    print("My name is kavya ")

#call function to print the name
printname()

#create function to concatenate fname and lname from user
fname =input("Enter your first name:")
lname=input ("Enter your last name:")

def fullname(firstname,lastname):
    print(firstname +" "+lastname)
   
fullname(fname,lname)
