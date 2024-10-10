# Stores multiple data 
# list:it can store multiple data with different datatypes
# set:unordered,unchangleable,no duplicate
# Dictionary:ordered,changeable,no duplicate

#list in python
#list store multiple data
myList=["pawan","ivan","Deepanshu"]
#tuple store multiple  data
myTuple=("pawan","ivan","deepanshu")
# set store multiple data 
mySet={"pawan","ivan","deepanshu"}
# dictionary store multiple data in key value pair
myDictionary={"name":"pawan","email":"p@gmail.com"}

#to check the data type of all above data set
print("list:",type(myList),"tuple:",type(myTuple))
print("set:",type(mySet),"dictionary:",type(myDictionary))

# how to identify list,set,tuple,dictionary
# list->[] , tuple->() , set->{} , dictionary->{:}

# example of data set
myData={"Pawan","deepanshu","mahi","Pawan"}
mygroup=("Pawan","deepanshu","mahi")
myclass=["Pawan","Deepanshu","mahi"]
myFriends={"name":"Pawan","Age":33,"name":"Pawan"}

# access multiple data from data set
print("list:",myList[0])
print("tuple:",myTuple[0],"dict:",myDictionary["name"])

#access complete data from data set 
for data in myList:
    print(data)
for item in mySet:
    print("set",item)
for value in myTuple:
    print("tuple",value)
for x in myDictionary:
    print("Dictionary",x)

#to check which data set support duplicate data 
# list can contian the duplicate item
# set does not contains duplicate items
# tuple can store duplicate item
# dictionary does not contain duplicate items 
 
print("list",myList,"tuple",myTuple,"dict",myDictionary,"set",mySet)

# Update the data of all data set
myList[0]="Tripti"
print(myList)
# tuple and set is unchangleable 
# dictionary and list is changeable
# set,dict no duplicate item
 
#  Add new value in data set 
myList.append("saloni")
mySet.add("Saloni")
myDictionary.update({"name":"saloni"})
print("list",myList,"tuple",myTuple,"Dictionary",myDictionary,"set",mySet)

# to remove the data from data set
myDictionary.pop("name")
myList.pop(0)
mySet.remove("pawan")
print("list",myList,"tuple",myTuple,"Dictionary",myDictionary,"set",mySet)

# converts tuple to list
ConvertList=list(myTuple)
print(type(ConvertList))

ConvertList.append("rohan")
ConvertList.pop(2)
print(ConvertList)
myTuple=tuple(ConvertList)
print(myTuple)