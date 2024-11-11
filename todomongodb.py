from pymongo import MongoClient

# create mongo client connection
client=MongoClient("mongodb://localhost:27017/")

# create new database for todoApp
mydb=client["todoDB"]

# create new collection fro, database in todoApp
mycol=mydb["tasklist"]

# create data using dictionary 
# mytask={"taskname":input("Enter task name"),"taskdesc":input("Enter task description"),"taskdate":input("Enter task data"),"taskstatus":0}

# add data into collection
# mycol.insert_one(mytask)

# create friend colllection in tododb
myfriendlist=mydb["friendlist"]

# add new friend in friendlist
friend=[{"name":"ivan","age":36,"gender":"male"},{"name":"ram","age":28,"gender":"male"},{"name":"anu","age":16,"gender":"female"}]

# to add friend into collection
# myfriendlist.insert_many(friend)

# to delete the data in database
deletefriend={"name":"ivan"}
myfriendlist.delete_one(deletefriend) 

# update the friend list 
name={"name":"anushka"}
myfriendlist.update_one({'age':16},{"$set":name})

# 