from pynput.keyboard import Key, Controller
import time
time.sleep(15)
Keyboard = Controller()
f = "this is raafat from the bot"
while True :
        for word in f:
          for letter in word:
                Keyboard.press(letter)
                Keyboard.release(letter)
          Keyboard.press(Key.enter)
          Keyboard.release(Key.enter)
