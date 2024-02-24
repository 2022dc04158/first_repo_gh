#####################################
############ Python Basic-2 -------- List, Tuple, Set, Dict
##  List is a collection which is ordered and changeable. Allows duplicate members.
##  Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
##  Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
##  Dictionary is a collection which is ordered** and changeable. No duplicate members.

###########################################################################################################################################
print("\n*************** Python List ***************\n")
list1 = ["apple", "banana", "cherry", "apple", "cherry"]
list2 = ["abc", 34, True, 40, "male",4,5,6,7]
list3 = (("a","b","d","c"))
list4 = ["a","b","c","d"]
print(list1,list2,list3)
print(len(list1),len(list2))    #### length
print(list1[2:7])               #### print specific values

###### Changing list values
list1[1:2] = ["qqqqqqq", "wwwwwwwww"]
list2[0] = "xyz"
list4[1:3] =["z"]
print(list1,list2,list4)        #### length + or - as per updation
########### addition list
list4.insert(2, "watermelon")
print(list4)
list4.append("zxcx")
list1.extend(list2)
print(list1,list2,list4)
########### delition list
list1.remove("qqqqqqq")
list1.pop(1)
print(list1,list2,list4)
#del list2                       ####completely deleted list
#list4.clear()                   #### emply the list
#print(list1,list4)
########### for Loop in list
for x in list2:
  print(x)
for i in range(len(list4)):     #### range(1) also be used as constant
  print("\n..............",list4[i])
for i in range(len(list4)):     #### range(1) also be used as constant
  print("\n..............",list4[i])

########### while Loop in list
i = 0
while i < len(list2):
  print(list2[i])
  i = i + 1
else:
  print("printed full list")

####### List Comprehension
print("\nList Comprehension.............")
newlist = [x for x in list4 if "a" in x]
print(newlist)
newlist = [x for x in list4 if x != "zxcx"]
print(newlist)
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x<4]
print(newlist)
newlist = [x.upper() for x in list4]
print(newlist)
newlist = ['hello' for x in list4]
print(newlist)
####### List sorting
thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort(reverse=True)
print(thislist) 
thislist.sort()
print(thislist)
#### Customize Sort Function 
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


##################################################
username = input("Enter username:")
print("Username is: " + username)
###########################################################################################################################################
