def quote_output():
    quote = input("Enter your favorite quote:")
    word = ""
    for character in quote:
        if character.isalpha():
            word += character
        else:
            if word and word[0].lower() > "g":  
                print(word.upper())
                word = ""
            else:
                word = ""

    if word and word[0].lower() > "g":
        print(word.upper())

    print("Matthew Dinoff")

quote_output()