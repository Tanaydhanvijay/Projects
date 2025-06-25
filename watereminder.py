import time
from plyer import notification

while True:
    print("Please sip some water!")  
    notification.notify(
        title=" 💧Please drink some water!",
        message="You need to drink some water to stay hydrated.",
        timeout=10  # Notification stays for 10 seconds
    )
    time.sleep(60*60)  # Wait for 1 hour before next reminder
