# File handling:- work on the file 

# Create File :- syntax
# variableName=open("filename.extension","filemode)
# e.g.

# myLaptopPassword=open("Password.txt","w")

# Write file:=syntax
# e.g.myLaptoppassword.write("abcdefg")

# Read from file
# e.g.myLaptopPassword.read()

# Delete file
# import os
# os.remove("Password.txt")



# open function will create the File
# when file is not existing
myPassword=open("Password.txt","w")

# Write my laptop password in the File
myPassword.write("abcdefg")

# overwrite the new Password using user input
myPassword.write(input("Enter your password:"))

#read the password from file 
myPassword=open("password.txt","r")
myData=myPassword.read()
if "macbook" in myData:
    print("Yes")
else:
    print("No")

# To close the file
myPassword.close()

# Delete the file 
import os 
os.remove("password.txt")

# Create read write delete csv,excel,json,txt
# Create csv file
myCsv =open("myfile.csv","w")
myCsv.write("pawan,tripti,anjali,saloni,suryansh")


myexcel = open("myexcel.xlxs","w")
myexcel.write("p,d,kd,fj,df")