table = {"name": "Table 1", "heigth": "10cm", "width": 25, "color": "red"}

dictionary = {"key": "value"}
name = table.get("colors")
#name = table["get"]
print("before adding names")
print(table)
table["names"] = ["name 1", "name 2", "name 3", "name 4"]
print("")
print("After adding names")

table = {}
table["name"] = input("enter the name ")