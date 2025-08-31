import random as rd
guessed_num=rd.randint(1,50)
def easy(num):
    global guessed_num
    attempts=num
    for i in range(num):
        print(f"You have a {attempts} attempts remaining to guess the number")
        a=int(input("Make a guess :"))
        if(a<guessed_num):
            print("Too low")
        elif(a>guessed_num):
            print("too high")
        else:
            print("You win :) !!")
            break
        attempts-=1



def game():
    print("I'm thinking of a number between 1 to 50")
    o=input("Choose a difficulty. Type 'easy' or 'hard' : " ).lower()
    if(o=="easy"):
        easy(5)
    elif(o=="hard"):
        easy(10)
    else:
        print("Choose a valid difficulty bro")

game()
