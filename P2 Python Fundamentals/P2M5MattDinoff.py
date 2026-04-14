import os

os.system("curl -k https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt")

elements = open("elements1_20.txt", "r")
elements_txt = elements.read().lower()
elements_list = elements_txt.split("\n")

print("Welcome Matt Dinoff. List any 5 of the first 20 elements on the Periodic Table: ")
def elementsquiz():
    points = 0
    attempts = 5
    correct_inputs_list = []
    incorrect_inputs_list = []    
    
    while True:
        
        player_input = input("Name any one of the first twenty elements in the periodic table")
        player_input = player_input.lower()
        print("Enter the name of an element: ",player_input)

        while player_input in correct_inputs_list:
            if player_input in correct_inputs_list:      
                print(player_input," was already entered")           
                player_input = input("Name any one of the first twenty elements in the periodic table")
                player_input = player_input.lower()
                print("Enter the name of an element: ",player_input)

            if player_input not in correct_inputs_list:
                break                                         

        if (player_input in elements_list):
            points += 1
            correct_inputs_list.append(player_input) 

        else: 
            incorrect_inputs_list.append(player_input)
        attempts -= 1 

        if attempts <= 0:
            break
        
    print(points * 20, "% correct") #showing % correct
    print("Answers found:", correct_inputs_list) #showing correct answers
    print("incorrect answers:", incorrect_inputs_list) #showing incorrect answers
    elements.close



elementsquiz()


