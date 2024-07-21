import random  as r
from Alpha import alpha

User=input("What is your message:")
Words=User.split(" ")
question=int(input("What is your Choice(1 or 2) Choose 2 option only if you want to decode:-"))
if question == 1:
    Secret=True
else:
    Secret=False

if(Secret):
    nwords=[]
    for word in Words:
        if len(User)>= 3:
            ran1=r.choice(alpha)
            ran2=r.choice(alpha)
            Str=ran1+word[1:]+word[0]+ran2
            nwords.append(Str)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords=[]
    for word in Words:
        if len(User)>=4:
            Stnew=word[1:-1]
            Str1=Stnew[-1]+Stnew[:-1]
            nwords.append(Str1)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

