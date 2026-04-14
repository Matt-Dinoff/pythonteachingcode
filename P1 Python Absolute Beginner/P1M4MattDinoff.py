def str_analysis():
    user_input = ""
    while user_input == "":
        user_input = input("Matt Dinoff, enter word or integer: ")
        
    if user_input.isdigit():
        if int(user_input) > 99:
            return(user_input + " " + "is a big number!")
        elif int(user_input) < 99:
            return(user_input + " " + "is a small number")                
    elif user_input.isalpha():
        return("\'" + user_input +"\' is all alphabetical!")
    else:
        return("\'" + user_input + "\' is not all alphabetical.")

print(str_analysis())