# checkInput2.py - simple check to see if user enters a number
#                - gives user a second chance (only)


age = input("How old are you?\n")

# check to see if first element of age is a number
if age[0] not in ['1','2','3','4','5','6','7','8','9','0'] :
    print('Please enter a numerical value.\n')
    age = input("How old are you (again)?\n")
    

age = int(age)

if age < 21 :
    print("Alcohol denied!")
    
else :
    print("Drink up!")
    
# This code works fine if a number is input
# and gives the user (one) second chance
# It only checks the first character though
# so can be broken by entering, e.g., "5ive"