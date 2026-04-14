animal_list = ["cat", "wolf", "horse"]
#define function
def listomatic():
    #create while loop
    while animal_list != []:
        #get user input
        animal = input("Enter the name of an animal or 'quit' to quit: ")
        #start if/elif statements
        #if user input is empty
        if animal == "":
            print("Welcome, Matt. Look at this list of animals : ",animal_list)
            popped_animal = animal_list.pop()
            print("Enter the name of an animal: ", animal, "\n",popped_animal, "was popped from list")
            #if animal_list is empty after a pop, send goodbye message
            if animal_list == []:
                print("Goodbye")
        #if user input is quit, quit function
        elif animal.lower() == "quit":
            print("Welcome, Matt. Look at this list of animals : ",animal_list, "\n",
                                "Enter the name of an animal: ", animal, "\n",
                                "Goodbye!")
            return
        #if user input is an animal already in the list, remove said animal
        elif animal in animal_list:
            print("Welcome, Matt. Look at this list of animals: ",animal_list)
            animal_list.remove(animal)
            print("Enter the name of an animal: ", animal, "\n1 instance of " + animal + " removed from list")
            #if user input remove an animal and it is the last animal in the list, end program
            if animal_list == []:
                print("Goodbye!")
           #if user input is not in the list, append it to the end of list 
        elif animal not in animal_list:
            print("Welcome, Matt. Look at this list of animals: ",animal_list, "\n")
            animal_list.append(animal)
            print("Enter the name of an animal: ",animal, "\n1 instance of " + animal + " appended to list")
          
        else:
            print("Goodbye!")
            return
           
           
listomatic()
