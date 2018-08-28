import random

print("...Cricket...")
print("...Football...")
print("...Volleyball...\n")

player = input("Enter player favorite game : ").lower()
#print(player)

c = random.randint(0,2)
if c == 0:
    computer = "cricket"
elif c == 1:
    computer = "football"
else:
    computer = "volleyball"




if player != "":
    
    if (player == "cricket" or (player == "football" or player == "volleyball")):
        print("Computer favorite game : " + str(computer))
        if player == computer:
            print("Match is ties")
        elif player == "cricket":
            if computer == "football":
                print("player is win")
            elif computer == "volleyball":
                print("computer is win")
        elif player == "football":
            if computer == "volleyball":
                print("player is win")
            elif computer == "cricket":
                 print("computer is win")
                 
        elif player == "volleyball":
            if computer == "cricket":
                print("player is win")
            elif computer == "football":
                print("computer is win")
        
    else:        
        print("Something went to wrong")
else:
    print("Write something here")
     
