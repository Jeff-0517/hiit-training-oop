# course_code = input("Enter course code")
# score = int(input("Enter score: "))

# if score>= 70 and score <= 100:
#     print("A")


# else:
#     if score >= 60 and score <= 69:
#         print("B")

#     else:
#         if score >= 50 and score <= 59:
#             print("C")

#         else:
#             if score >= 45 and score <= 49:
#                  print("D")

#             else:
#                 if score >= 40 and score <= 44:
#                     print("E")      

#                 else:
#                      if score >= 0 and score <= 39:
#                         print("F")
    



course_code = input("Enter the course code: ")
score_str = input("Enter your score: ")

if score_str.isdigit():
    score = int(score_str)

    if score >= 70 and score <= 100:
        print(f"{course_code} - {score} - A")
    elif score >= 60 and score <= 69:
        print(f"{course_code} - {score} - B")
    elif score >= 50 and score <= 59:
        print(f"{course_code} - {score} - C")
    elif score >= 45 and score <= 49:
        print(f"{course_code} - {score} - D")
    elif score >= 40 and score <= 44:
        print(f"{course_code} - {score} - E")
    elif score >= 0 and score <= 39:
        print(f"{course_code} - {score} - F")
    else:
        print("score only rangers from 0 - 100")

else:
    print("The score must be a number")