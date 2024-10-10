import numpy as np

# create numpy numpy array to store 
# friend name,edit

myfriends=np.array(["ivan","anshu","wani","anjali"])
print(myfriends)
print(type(myfriends))
print(myfriends[2])

for name in myfriends:
    print(name)

myfriends[0]="ivan sharma"
print(myfriends[0])
myfriends.sort()
print(myfriends)

# mydata=np.flip(myfriends)
# print(mydata)

y=3
while y>0:
    print(myfriends[y])
    y=y-1

# Numpy=create dataset
# Pandas=Represents dataset->changes
# matplotlib=show in graph
