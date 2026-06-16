product = "shoe"
if product == "shoe" or product == "bag":
    print("you will get 10% discount")
    age = 18
    if age >= 18:
        print("you are an adult")

age = 16
if age >= 18:
    print("You can vote")
else:
   print("you can't vote")

score = 75
if score >= 70:
    print("Excellent")
elif score >= 50:
    print("pass")
else:
    print("fail")

age = 20
has_id = True
if age >= 18 and has_id == True:
    print("Access Granted")
    


age = 20
has_id = True
if age > 18:
    if has_id == True:
        print("Access granted")
    else:
        print("You need an id")
else:
 print("you are underage")


 user_logged_in = True
 cart_total = 750
 payment_method = "card"

if not user_logged_in:
    if cart_total > 0:
        if payment_method == "card":