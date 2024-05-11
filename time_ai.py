import time
# time_curr=time.strftime("%I:%M:%S")
# print(type(time_curr))
time_man=time.strftime("%H:%M:%S")
time_man1=int(time.strftime('%H'))
print(time_man1)

if time_man1 > 0 and time_man1 < 12:
    print("Good Morning!")
elif time_man1 >=12 and time_man1 <17:
    print("Good Afternoon!")
else:
    print("Good Night!")
    