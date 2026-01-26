'''
lets assume 1-->snake
0 --> water 
-1 --> gun

'''
import random
def firstgame():
            computer=random.choice([1,0,-1])            #random value is pickede from the list

            user=input("enter your choise:\n1)snake\n2)water\n3)gun: ")
            youdict={"snake":1,"water":0,"gun":-1}      #user choices are converted to numbers
            revdict={1:"snake",0:"water",-1:"gun"}      #computer choices are converted to strings
            if user not in youdict:                     #confirming valid input  or not then assigning to you variable
                print("Invalid Input!! 🤔😵🚫")
                print("Try once again")
                firstgame()
                return
            you=youdict[user]                            #converting user input to corresponding number
            if computer==you:
                print(f"Computer chose {revdict[computer]} and you Chose {user}")
                print("Its a Tie 🤝🔄")
                print("Try once again")
                firstgame()
            else:
                if(computer==1 and you==0) or (computer ==0 and you==-1) or(computer==-1 and you==1): #The criteria for avoiding to loosse the game
                    print(f"Computer chose {revdict[computer]} and you Chose {user}")
                    print("YOU LOOSE 😢😞!!!")
                    print("Try once again")
                    firstgame()
                else:
                    print(f"Computer chose {revdict[computer]} and you Chose {user}")
                    print("You Win! 🏆🔥")
