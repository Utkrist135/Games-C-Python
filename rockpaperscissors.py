import random
while True:
        choices=["rock","paper","scissors"]

        computer=random.choice(choices)
        your_choice=None

        while your_choice not in choices:
            your_choice=input("Please enter your choice!! ").lower()
        if your_choice==computer:
            print("Computer: " ,computer)
            print("Player: " ,your_choice)
            print("It's a tie!!")

        elif your_choice=="rock":
            if computer=="paper":
                print("Computer: " ,computer)
                print("Player: " ,your_choice)
                print("You Lose!!")
            if computer=="scissors":
                print("Computer: " ,computer)
                print("Player: " ,your_choice)
                print("You Win!!")  

        elif your_choice=="paper":
            if computer=="scissors":
                print("Computer: " ,computer)
                print("Player: " ,your_choice)
                print("You Lose!!")
            if computer=="rock":
                print("Computer: " ,computer)
                print("Player: " ,your_choice)
                print("You Win!!")  

        elif your_choice=="scissors":
            if computer=="rock":
                print("Computer: " ,computer)
                print("Player: " ,your_choice)
                print("You Lose!!")
            if computer=="paper":
                print("Computer: " ,computer)
                print("Player: " ,your_choice)
                print("You Win!!")  
        play_again=input("Play again(y/n)? ").lower()
        if play_again!="y":
            break           
