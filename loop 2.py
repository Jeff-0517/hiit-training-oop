# start = 1
# stop = 10
# step = 2
# for k in range (start, stop +1, step):
#     print(k)

#A PYTHON PROGRAM THAT PRINTS ALL THE MULTIPLES OF 5 FROM 1-200
for i in range(5, 201):
    if i % 5 == 0:
        print(i)
  


class_list = ["David", "Samuel", "Gafar", "Rayan", "Odufua"]
class_number = len(class_list)
for person in class_list:
    print(person.capitalise())

# for person in class_list
# print(f"we have")

#while loop
# > - Greater than
# < - less than 
# <= - less than or equal to
# >= - greater than or eq.ual to

# while True: 
#     print("While is running .......")


number = 1
while number < 10:
    print(number)
    increment = number+1
    number = increment 



# using while loop through list

class_length = len(class_list)
start =0
while start < class_length:
    print(class_list[i]) 
    i = i+1   