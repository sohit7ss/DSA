# import pyautogui
# import time

# message = "Hello Bro!"

# time.sleep(5)  # Time to open chat window

# for i in range(100):
#     pyautogui.write(message)
#     pyautogui.press("enter")


import pyautogui
import time

message = "gd nyt GM"

time.sleep(5)  # Time to open chat

for i in range(1, 201):
    pyautogui.write(f"{i}. {message}")
    pyautogui.press("enter")
    time.sleep(0.5)
    