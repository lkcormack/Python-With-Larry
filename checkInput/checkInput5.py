# checkInput4.py - better check to see if user enters a number
#                - gives user infinite chances

is_not_digit = [True]
age = ''

# check input in a while loop to give users multiple chances
while any(is_not_digit)  or (age == '') :
    
    # reset is_not_digit
    is_not_digit = list()  # empty list to hold results
    
    age = input("How old are you?\n")

    for i in age :
        is_not_digit.append(i not in ['1','2','3','4','5','6','7','8','9','0'])        

age = int(age)

if age < 21 :
    print("Alcohol denied!")
    
else :
    print("Drink up!")
    
# This code works fine if a number is input
# and gives the user (one) second chance
# This version checks *all* of the users input
# so it will be break if, e.g., "5ive", is entered
# It still only gives the user one opportunity to
# correct the input tho


