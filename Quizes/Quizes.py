from Questions import questions_answers
Money=0
Correct_Ans=0
for qa in questions_answers:
    print(qa["question"])
    reply=input("What is your Answer:")
    if reply ==qa["answer"]:
        Correct_Ans+=1
        if Correct_Ans == 1:
            Money+=500
        elif Correct_Ans == 2:
            
            Money+=2000
        elif Correct_Ans == 3:
            Money+=4000
        elif Correct_Ans == 4:
            Money+=5000
        elif Correct_Ans == 5:
            Money+=6000
        elif Correct_Ans == 6:
            Money+=10000
        elif Correct_Ans == 7:
            Money+= 20000
        elif Correct_Ans == 8:
            Money+= 50000
        elif Correct_Ans == 9:
            Money+= 6000
        elif Correct_Ans == 10:
            Money+=70000
        elif Correct_Ans == 11:
            Money+=80000
        elif Correct_Ans == 12:
            Money+=90000
        elif Correct_Ans == 13:
            Money+=1000000
        elif Correct_Ans == 14:
            Money+=20000000
        elif Correct_Ans == 15:
            Money+=300000000
        else:
            print("0")
    else:
        print("Grow First!")
        print(f"Your Correct Answers are:{Correct_Ans}")
        print(f"The Money your Earned:{Money}")
        break        
print("You have gone through all the questions!")
