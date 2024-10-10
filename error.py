# Error 1
# print(x)

#error handling 
try:
    print(x)
except NameError:
    print("'x' is not defined")

# Error 2
# y=1/0

# error handling 
try:
    y=1/0
except ZeroDivisionError:
    print("Divide by zero error")

# Error 3
name="kavya"
# no=int(name)

# error handling 
try:
    no=int(name)
except ValueError:
    print("string cannot convert into integer")

# Error 4
friends=["ivan","anshu","vani"]
# friends[4]

# error handling
try:
    friends[4]
except IndexError:
    print("list index out of range")

# Error 5
amount=500
email="p@gmail.com"
# total=amount+email

# error handling 
try:
    total=amount+email
except TypeError:
    print("string can't add integer")
    
     