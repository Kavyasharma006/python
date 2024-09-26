#list can store ,multiple  data,data can be of differnt types int str char 
# list can store the duplicate data
#list is an ordered data set- sorting ascending descending

#create list and store your friend name
friendlist=["anjali","tanu","anu","anshu"]

#print the list of friend names
print(friendlist)

#add the age of your friend in list
#append will add the data into end of the list
friendlist.append(27)
friendlist.append(19)
friendlist.append(26)
friendlist.append(16)
print(friendlist)

# add the data into list using index no
friendlist.insert(0,"Ayush")
print(friendlist)

friendlist.insert(2,"kavya")
print(friendlist)
print(friendlist[2])

# access the complete list
for name in friendlist:
    print(name)

#to delete the data from friendlist
#remove will delete the data using value
friendlist.remove("kavya")
print(friendlist)

#pop will delete the data using index 
friendlist.pop(1)
print(friendlist)

#add 5 favt city name in list 
#add my favt city kasol in index 0
#remove the last city in list
#sorting the list data
#print the list data

favtcitylist=["pune","delhi","ghaziabad","jaipur"]
favtcitylist.insert(0,"kasol")
favtcitylist.pop(3)
favtcitylist.sort()
print(favtcitylist )
  