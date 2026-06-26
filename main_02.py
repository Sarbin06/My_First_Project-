# Rock, paper, sissor Game with three friends.

youstr_1=input("Enter your choice :").capitalize()
youstr_2=input("Enter your choice :").capitalize()
youstr_3=input("Enter your choice :").capitalize()

youdict = {"Rock":1 ,"Paper":2 ,"Scissor":3}

reversedict = {1:"Rock" ,2:"Paper" ,3:"Scissor"}

Friend_1=youdict[youstr_1]
Friend_2=youdict[youstr_2]
Friend_3=youdict[youstr_3]

print(f"First Friend : {reversedict[Friend_1]}\n Second Friend : {reversedict[Friend_2]}\n Third Friend :{reversedict[Friend_3]}")

#Condiction for draw.

if(Friend_1==Friend_2==Friend_3) or\
    (Friend_1!=Friend_2!=Friend_3!=Friend_1):
    #NOTE: yoy also can use :
    # (len({Friend_1, Friend_2, Friend_3}) == 3):

    print("Its a draw")
    raise SystemExit

#Condiction for 1 winner
if  (Friend_1==1 and Friend_2==Friend_3==3) or\
    (Friend_1==2 and Friend_2==Friend_3==1) or\
    (Friend_1==3 and Friend_2==Friend_3==2):
      print("Friend_1 wins!")
      raise SystemExit
      
elif(Friend_2==1 and Friend_1==Friend_3==3) or\
    (Friend_2==2 and Friend_1==Friend_3==1) or\
    (Friend_2==3 and Friend_1==Friend_3==2):
      print("Friend_2 wins!")
      raise SystemExit
    
elif(Friend_3==1 and Friend_2==Friend_1==3) or\
    (Friend_3==2 and Friend_2==Friend_1==1) or\
    (Friend_3==3 and Friend_2==Friend_1==2):
      print("Friend_3 wins!")
      raise SystemExit

#Condiction for 2 winner.
if(Friend_1==1 and Friend_2==Friend_3==2) or\
    (Friend_1==2 and Friend_2==Friend_3==3) or\
    (Friend_1==3 and Friend_2==Friend_3==1):
      print("Both Friend_2 and Friend_3 wins!")
      
      while True:
            youstr_2 = input("Second Friend's choice : ").capitalize()
            youstr_3 = input("Third Friend's choice : ").capitalize()

            Friend_2 = youdict[youstr_2]
            Friend_3 = youdict[youstr_3]

            print(f"Second Friend : {reversedict[Friend_2]}\n Third Friend :{reversedict[Friend_3]}")

            if(Friend_2==Friend_3):
                print("It's a Draw")
                continue
            
            elif(Friend_2==1 and Friend_3==3) or\
                (Friend_2==2 and Friend_3==1) or\
                (Friend_2==3 and Friend_3==2):
                 print("Friend_2 wins!")
                 break

            else:
                  print("Friend_3 wins!")
                  break 


if(Friend_2==1 and Friend_1==Friend_3==2) or\
    (Friend_2==2 and Friend_1==Friend_3==3) or\
    (Friend_2==3 and Friend_1==Friend_3==1):
      print("Both Friend_1 and Friend_3 wins!")
      
      while True:
             youstr_1 = input("First Friend's choice : ").capitalize()
             youstr_3 = input("Third Friend's choice : ").capitalize()

             Friend_1 = youdict[youstr_1]
             Friend_3 = youdict[youstr_3]
             print(f"First Friend : {reversedict[Friend_1]}\n Third Friend :{reversedict[Friend_3]}")

             if(Friend_1==Friend_3):
                 print("It's a Draw")
                 continue
            
             elif(Friend_1==1 and Friend_3==3) or\
                (Friend_1==2 and Friend_3==1) or\
                (Friend_1==3 and Friend_3==2):
                 print("Friend_1 wins!")
                 break

             else:
                  print("Friend_3 wins!")
                  break 


if(Friend_3==1 and Friend_2==Friend_1==2) or\
    (Friend_3==2 and Friend_2==Friend_1==3) or\
    (Friend_3==3 and Friend_2==Friend_1==1):
      print("Both Friend_1 and Friend_2 wins!")
      
      while True:
             youstr_1 = input("First Friend's choice : ").capitalize()
             youstr_2 = input("Second Friend's choice : ").capitalize()

             Friend_1 = youdict[youstr_1]
             Friend_2 = youdict[youstr_2]
             print(f" First Friend :{reversedict[Friend_1]} \n Second Friend : {reversedict[Friend_2]}")

             if(Friend_2==Friend_1):
                print("It's a Draw")
                continue
            
             elif(Friend_2==1 and Friend_1==3) or\
                (Friend_2==2 and Friend_1==1) or\
                (Friend_2==3 and Friend_1==2):
                 print("Friend_2 wins!")
                 break

             else:
                  print("Friend_1 wins!")
                  break