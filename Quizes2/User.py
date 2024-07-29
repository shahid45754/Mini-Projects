from Question import mcq_list
Money=0
Correct=0
Wrong=0
for i in range(len(mcq_list)):
     questions=mcq_list[i]["question"]
     Ans=mcq_list[i]["answer"]
     Mcq=mcq_list[i]["options"]
     print(questions)
     print(Mcq)
     User=input("What is your Answer Type it Properly:")
     if User == Ans:
           Correct+=1
           print(f"Correct!{Correct}")
         
     else:
          print("Wrong!")
     
if  Correct >= 1:
          Money=Money+100
elif Correct >= 10:
     Money+=1000
     print("No Money for Loser!")
else:
     print("Loser ! ")