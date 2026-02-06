from random import randint
def game2():
    b=randint(1,100)
    guess=1
    a=-1
    while(a!=b):
        a=int(input("GUess a number: "))
        
        if(a>b):
            print("a bit lower number")
            guess+=1
        elif(a<b):
            print("a bit higher number")
            guess+=1
        else:
            
            print(f"You guessed the correct number {b} in {guess} times")
            break
    

game2()