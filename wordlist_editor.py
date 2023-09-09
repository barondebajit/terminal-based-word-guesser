while True:
    print("Enter 1 to add a new word to the wordlist.")
    print("Enter 2 to remove a word from the wordlist.")
    print("Enter 3 to know the number of words in the wordlist.")
    print("Enter 4 to exit.")
    command=str(input("Enter the command: "))

    with open("wordlist.txt","r") as file:
        wordlist=file.readlines()
    for i in range(len(wordlist)):
        wordlist[i]=(wordlist[i][:5]).upper()
    
    if command=="1":
        word=str(input("Enter the word: "))
        if len(word)!=5:
            print("The wordlist must only take 5 letter words.")
        elif word.upper() in wordlist:
            print("Word already in wordlist.")
        else:
            word=word.lower()
            with open("wordlist.txt","a") as file:
                file.writelines([word+"\n"])
            print("Word added.")
    elif command=="2":
        word=str(input("Enter the word: "))
        if word.upper() not in wordlist:
            print("Word already absent from the wordlist.")
        else:
            wordlist.remove(word.upper())
            with open("wordlist.txt","w") as file:
                for i in wordlist:
                    file.writelines(i+"\n")
            print("Word removed from wordist.")
    elif command=="3":
        print("There are {} words in wordlist.".format(len(wordlist)))
    elif command=="4":
        break
    else:
        print("Enter a valid command.")
    print("")
