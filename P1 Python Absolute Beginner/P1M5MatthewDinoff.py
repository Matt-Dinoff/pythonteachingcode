def adding_report(report_type = "T"):
    total = 0
    items = ""

    while True:
        item = input("Input integer to add to the total or 'Q': \n")
        if item.isdigit():
            total += int(item)
            if report_type == "A":
                items += item + "\n"
                    
        else:
            if item.lower().startswith("q"):
                if report_type == "A":
                    print("Items")
                    print(items)
                print("Total:\n",total)
                print("Calculated by: Matthew Dinoff")
                break                  
            else:
                print("Input is invalid.")        

adding_report("A")
adding_report()          