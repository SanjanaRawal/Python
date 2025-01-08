import random

print("ROCK , PAPER , SCISSORS".center(100,"-"))
print("Possible choices : rock , paper , scissor")

human_score = 0
comp_score = 0

while True :

    human_ch = input("Enter choice : ")
    ch = ["rock", "paper", "scissor"]
    comp_ch = random.choice(ch)

    print(" Your choice : ", human_ch.lower(), "\n Computer choice : ", comp_ch)

    if human_ch == comp_ch:
        print("It's a tie")

    elif (human_ch.lower() == "rock" and comp_ch == "paper") or (human_ch.lower() == "paper" and comp_ch == "scissor") or (
            human_ch.lower() == "scissor" and comp_ch == "rock"):
        print("You won!")
        human_score += 1

    else:
        print("Computer won!")
        comp_score +=1

    repeat = input("Play again? Yes to continue!!! and no to exit :( \n")
    if repeat.lower()=="no" :
        break

print("Your score : " , human_score)
print("Computer score : " , comp_score)