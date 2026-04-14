def word_mixer(words_list):
    words_list.sort()
    new_words=[]
    while len(words_list)>5:
        x=words_list.pop(-5)
        new_words.append(x)
        
        y=words_list.pop(0)
        new_words.append(y)
        
        z=words_list.pop(-1)
        new_words.append(z)

    return(new_words)

str_input=input("Welcome Matt Dinoff. Input a poem,verse,etc..")
words_list=str_input.split()
words_list_len=len(words_list)
for index in range(0,words_list_len):
    if len(words_list[index])<=3:
        words_list[index]=words_list[index].lower()
    elif len(words_list[index])>=7:
        words_list[index]=words_list[index].upper()

call = word_mixer(words_list)
print(" ".join(call))
