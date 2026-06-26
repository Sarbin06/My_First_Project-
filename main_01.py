# Rock, paper, sissor Game with computer
import random

Computer=random.choice([1,2,3])

youstr=input("Enter your choice :").capitalize()

youdict = {"Rock":1 ,"Paper":2 ,"Scissor":3}

reversedict = {1:"Rock" ,2:"Paper" ,3:"Scissor"}

you=youdict[youstr]

print(f"your chose : {reversedict[you]}\nComputer chose : {reversedict[Computer]}")


if(Computer==you):
    print("Its a draw")

elif(Computer==1 and you==2) or \
    (Computer==2 and you==3) or \
    (Computer==3 and you==1):
        print("You win!")

else:
    print("you lose!")