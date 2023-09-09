from colorama import Fore
import random

with open("wordlist.txt","r") as file:
    wordlist=file.readlines()
for i in range(len(wordlist)):
    wordlist[i]=(wordlist[i][:5]).upper()

index=random.randint(0,len(wordlist)-1)
word=wordlist[index]
ans=word
tries=5
guessed=0

while tries!=0:
    n=str(input("Enter the word: "))
    n=n.upper()
    guess=list(n)
    attempts_taken=tries

    if len(guess)!=5:
        print("Enter a 5 digit word.",end="")
    
    elif n not in wordlist:
        print("Enter a valid word.",end="")
    
    elif guess==word:
        print(Fore.GREEN,"Correct Answer. Took you {} tries".format(5-attempts_taken+1),end="")
        tries=0
        guessed=1
    
    else:
        temp=[]
        pos_wrong_temp=[]
        correct=[]
        incorrect=[]
        pos_wrong=[]
        for i in range(5):
            if guess[i]==word[i]:
                temp.append(guess[i])
                correct.append(i)
            elif guess[i] not in word:
                incorrect.append(i)
        for i in range(5):
            if i not in correct or i not in incorrect:
                if guess.count(guess[i])==2 or guess.count(guess[i])==3:
                    if word.count(guess[i])!=temp.count(guess[i])+pos_wrong_temp.count(guess[i]):
                        pos_wrong.append(i)
                        pos_wrong_temp.append(guess[i])
                    else:
                        incorrect.append(i)
                else:
                    pos_wrong.append(i)
                    pos_wrong_temp.append(guess[i])
        for i in range(5):
            if i in correct:
                print(Fore.GREEN,guess[i],end=" ")

            elif i in incorrect:
                print(Fore.RED,guess[i],end=" ")

            else:
                print(Fore.YELLOW,guess[i],end=" ")
        tries-=1
    print(Fore.WHITE,"")

if guessed==0:
    print("Ran out of tries.")
    print("The answer is",ans)

else:
    print("You have solved this wordle.")