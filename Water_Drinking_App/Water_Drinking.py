import time
from datetime import datetime
import winsound
from plyer import notification
import pytz
import schedule
store = []
def notify():
    notification.notify(title="ALERT DRINK WATER", message="STAY HYDRATED!!!", timeout=10)

def set_alarm(alarm_time_str, time_zone='Asia/Kolkata'):
    alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S")
    alarm_time = pytz.timezone(time_zone).localize(alarm_time)

    schedule.every().day.at(alarm_time.strftime("%H:%M:%S")).do(lambda: trigger_alarm(alarm_time_str, store))

def trigger_alarm(alarm_time_str, store):
    print(f"Alarm triggered at {alarm_time_str}!")
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    notify()
    store.remove(alarm_time_str)  # Remove the triggered alarm

def main():
    num_alarms = int(input("Enter how many alarms do you need: "))
    

    for i in range(num_alarms):
        alarm_time = input("Enter the alarms in HH:MM:SS format: ")
        store.append(alarm_time)

    for alarm_time in store:
        set_alarm(alarm_time)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()