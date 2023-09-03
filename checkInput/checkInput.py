# checkInput.py - very simple decision based on user input

age = input("How old are you?\n")

age = int(age)

if age < 21 :
    print("Alcohol denied!")
    
else :
    print("Drink up!")
    
# This code works fine if a number is input
# but fails if user enters something not
# convertable to int, e.g. "fourty two"