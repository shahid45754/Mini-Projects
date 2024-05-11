import random
from Img import rock,paper,scissors

computer=[rock,paper,scissors]
random_choice=random.choice(computer)
random_index=random.randrange(len(computer))
User=int(input("What is your choice:(0.Rock , 1.Paper , 2.Scissors):-"))
if User >= 0 and User <=2:
    print(f"Your Choice:{computer[User]}")
    print(f"Computer's Choice:{computer[random_index]}")
    if User == 0 and random_index == 1:
        print("Computer Wins!")
    elif User == 1 and random_index == 2:
        print("Computer Wins!")
    elif User == 2 and random_index == 0:
        print("Computer Wins!")
    elif User == random_index:
        print("Tied!!")
    else:
        print("User Wins!")
else:
    print("Wrong Number!")
    