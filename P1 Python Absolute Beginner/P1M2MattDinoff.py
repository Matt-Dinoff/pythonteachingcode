# [ ] create, call and test fishstore() function 
def fishstore(fish, price):
    return "The " + fish + " costs $" + price
    

name = "Matt Dinoff."
fish_entry = input("What type of fish do you want to buy?")
price_entry = input("How much does the fish cost?")

print("Report for", name, "Fish Type:",fishstore(fish_entry, price_entry))
