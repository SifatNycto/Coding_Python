# import pywhatkit
# import pyautogui
# import time

# number = "+8801747977819"
# message = "Happy Birthday Bro 🎉🔥 Stay blessed!"

# for i 
# pywhatkit.sendwhatmsg_instantly(number, message, wait_time=20)

# time.sleep(5)

# # Force send
# pyautogui.press("enter")

# 2.0>>>>>>>>>>>>>>>>>>>>
# #this worked 1.0>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import pywhatkit
# import pyautogui
# import time

# number = "+8801747977819"
# message = "Happy Birthday Bro 🎉🔥 Stay blessed!"

# count = 10

# # Open WhatsApp and TYPE first message
# pywhatkit.sendwhatmsg_instantly(number, message, wait_time=15, tab_close=False)

# time.sleep(7)   # give time to fully load + focus

# # 🔥 First message send manually
# pyautogui.press("enter")

# time.sleep(2)

# # 🔥 Now loop remaining messages
# for i in range(count - 1):
#     pyautogui.typewrite(f"{message} #{i+2}")
#     time.sleep(.5)

#     pyautogui.press("enter")   # send AFTER typing
#     time.sleep(.5)



#????????????????????????
# import pywhatkit
# import pyautogui
# import time

# number = "+8801747977819"
# message = "Happy Birthday Bro 🎉🔥 Stay blessed!"

# count = 10

# pywhatkit.sendwhatmsg_instantly(number, message, wait_time=15, tab_close=False)

# time.sleep(7)

# # ✅ AUTO CLICK (no manual effort)
# pyautogui.click()   # clicks current position (keep mouse on input box before run)

# time.sleep(1)

# pyautogui.press("enter")

# for i in range(count - 1):
#     pyautogui.typewrite(f"{message} #{i+2}")
#     pyautogui.press("enter")
#     time.sleep(5)












#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# import pywhatkit
# import pyautogui
# import time

# number = "+8801747977819"
# message = "Happy Birthday Bro 🎉🔥 Stay blessed!"

# count = 10   # test with small number first

# # Open WhatsApp chat ONCE
# pywhatkit.sendwhatmsg_instantly(number, message, wait_time=20)

# time.sleep(5)

# for i in range(count):
#     pyautogui.typewrite(f"{message} #{i+1}")
#     pyautogui.press("enter")
#     time.sleep(1)   # small delay between messages


# ?????????????????????????

# import pywhatkit
# import pyautogui
# import time

# number = "+8801747977819"

# pywhatkit.sendwhatmsg_instantly(number, "Starting...", wait_time=20)

# time.sleep(5)

# for i in range(50):
#     pyautogui.typewrite(f"Happy Birthday Bro 🎉🔥 ({i+1})")
#     pyautogui.press("enter")
#     time.sleep(0.8)











# individual

# import pywhatkit
# import pyautogui
# import time

# number = "+8801836982703"
# message = "You have been hacked !!"

# count = 20

# # Open WhatsApp
# pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=False)

# time.sleep(5)

# # 🔥 Automatically click message box (adjust if needed)
# pyautogui.click(x=800, y=950)

# time.sleep(1)

# # Send first message
# pyautogui.press("enter")

# # Loop باقي messages
# for i in range(count - 1):
#     # pyautogui.typewrite(f"{message} #{i+2}")
#     pyautogui.typewrite(message)
#     pyautogui.press("enter")
#     time.sleep(0.5)



# group>>>>>>>>>>>>> without emoji
# import pyautogui
# import time
# import keyboard

# message = "It Is Hacked"
# count = 50

# print("Open your WhatsApp group chat NOW...")
# time.sleep(5)

# # Click message box once
# pyautogui.click(x=800, y=950)   # adjust if needed
# time.sleep(1)

# print("Started sending... Press 'Q' to stop.")

# for i in range(count):

#     # 🔥 STOP anytime
#     if keyboard.is_pressed('q'):
#         print("Stopped by user!")
#         break

#     pyautogui.typewrite(message)
#     pyautogui.press("enter")

#     time.sleep(0.5)   # speed control




#///////////////////// wiht emmoji

import pyautogui
import time
import keyboard
import pyperclip

message = "It Is Hacked ❌☠️"
count = 100

print("Open your WhatsApp group chat NOW...")
time.sleep(5)

pyautogui.click(x=800, y=950)
time.sleep(1)

print("Started sending... Press 'Q' to stop.")

for i in range(count):

    if keyboard.is_pressed('q'):
        print("Stopped by user!")
        break

    # 🔥 Copy message to clipboard
    pyperclip.copy(message)

    # 🔥 Paste (Ctrl + V)
    pyautogui.hotkey("ctrl", "v")

    pyautogui.press("enter")

    time.sleep(0.5)




# for girl>>>>>>>>>>>>>>>>>>>
# import pyautogui
# import time
# import pyperclip
# import random

# messages = [
#     "You make my day better just by existing 💖",
#     "Talking to you feels like my favorite part of the day 😊",
#     "I don’t know how, but you always make me smile 😄",
#     "You’re honestly really special to me 💫",
#     "Why are you so effortlessly cute? 😏",
#     "You have such a calming vibe 🌙",
#     "I like talking to you… a lot 😊"
# ]

# count = 50   # 🔥 CHANGE THIS (how many messages you want)

# print("Open the chat NOW...")
# time.sleep(5)

# pyautogui.click(x=800, y=950)
# time.sleep(1)

# print("Sending messages...")

# for i in range(count):
#     msg = random.choice(messages)   # 🔥 random every time

#     pyperclip.copy(msg)
#     pyautogui.hotkey("ctrl", "v")
#     pyautogui.press("enter")

#     time.sleep(.5)

# print("Done 😏")