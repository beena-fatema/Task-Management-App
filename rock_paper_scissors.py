import random
user_wins=0
computer_wins=0
tie=0
options=["rock","paper","scissors"]
while True:
    user_input=input("Type Rock/Papers/scissors or Q to quit: ").lower()
    if user_input=="q":
     break
    if user_input not in options:
     continue
    rno=random.randint(0,2)
    #rock=0,paper=1,scissors=2
    computer_pick=options[rno]
    print("computer picked",computer_pick +".")
    if user_input=="rock"and computer_pick=="scissors":
     print("You Won!")
     user_wins+=1
    elif user_input=="paper"and computer_pick=="rock":
     print("You Won!")
     user_wins+=1
    elif user_input=="scissors"and computer_pick=="paper":
     print("You Won!")
     user_wins+=1
    elif user_input==computer_pick:
      print("It's a tie!")
      tie+=1
    else:
      print("You Lost!")
      computer_wins+=1
print("you won",user_wins,"times")
print("The computer won",computer_wins,"times")
print("You got",tie,"ties")
print("Goodbye!")