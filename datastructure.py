# #list
# fruits = ["apple", "banana", "orange"]
# # print("fruits:", fruits)
# #find item based on position(index)

# item = fruits[2] #read
# print(item)

# #modifying editing
# fruits[2] = 'mango'
# # add new item to list
# fruits.append("carrot")

# fruits.insert(3, 'melon')
# print(fruits) #update


# fruits.remove("carrot")
# print("updated fruits:", fruits)


# fruits.pop(3)
# print("updated fruits:", fruits)


lastitem = [-2]
print(lastitem)

anotherlist = [1,3,2,0,5,7,7,8,6,7]
anotherlist.sort()
print(anotherlist)
anotherlist.reverse()
print(anotherlist)
totalitemsinthelist = len(anotherlist)
print(totalitemsinthelist)


howmanytimesihave7 = anotherlist.count(7)
print(howmanytimesihave7)


is7inthelist = 34 in anotherlist
print(is7inthelist)

anotherlist1 = anotherlist[1:10]
print(anotherlist1)

newList = [2,1,4,56,3,4,6,8,78]
indexOf56 = newList.index(56)
print(indexOf56)

list1 = [1,2,3]
list2 = [4,5,6]
combinedList = list1 + list2


print(combinedList)

student = {'name': "john", 'age': 15}
studentcopy = student.copy()
print(student["name"])
print(student.get("name"))

student["address"] = "41, awolowo express way" 


print(student)
student["name"] = "paul"
print(student)
name = student.get("name")
print(name)


key = student.keys()
print("keys", key)



values = student.values()
print("values", values)

items = student.items()
print("items", items)

print(items)
student.pop("age")
del student["address"]
print(student)
student.clear()
print(student)



print(studentcopy)


text = "preference"
print(text[0])
print(text[1:3])
print("length", len(text))

print(text.upper())
print(text.lower())
print(text.capitalize())
text = text.strip()
print("length", len(text))

text1 = " preference is the key to sucess "
print("length", len(text1))
text1 = text1.lstrip()
print("length", len(text1))
text1 = text1.rstrip()
print("length", len(text1))
text1 = text1.replace("preference", "smart move")
print(text1)


# suppliers = {

#     "ade": 20,
#     "bimbo": 40,
#     "kenneth": 30
# }


