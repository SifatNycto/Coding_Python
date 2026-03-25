"""
import pyautogui
import time

print("Starting in 3 seconds... move your mouse if you want to stop 😅")
time.sleep(3)

# Move mouse in a square pattern
for i in range(4):
    pyautogui.moveRel(100, 0, duration=0.5)   # right
    pyautogui.moveRel(0, 100, duration=0.5)   # down
    pyautogui.moveRel(-100, 0, duration=0.5)  # left
    pyautogui.moveRel(0, -100, duration=0.5)  # up

print("Done ✅")

"""


from datetime import date
import time

# ANSI escape codes for colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def happy_birthday(name):
    print(GREEN + f"🎂 Happy Birthday, {name}! 🎂" + RESET)
    time.sleep(1)
    print(CYAN + "Wishing you a bug-free life and an infinite loop of happiness 💻💙" + RESET)
    time.sleep(1.5)
    print(YELLOW + "May your code always compile and your dreams always execute successfully!" + RESET)
    time.sleep(2)
    print()
    print(GREEN + "Arik, you're not just my best friend, you're the best solve bro." + RESET)
    time.sleep(1.5)
    print(CYAN + "May your life run smoother than Python, faster than C, and cooler than JavaScript 🚀💙" + RESET)

if __name__ == "__main__":
    today = date.today()
    if today.day == 21 and today.month == 9:
        happy_birthday("Arik")
    else:
        print("Waiting for Arik's birthday...")