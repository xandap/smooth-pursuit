import threading
from pynput.keyboard import Key, Listener
from smoothPursuit import

def main():
    print('hello')

def on_press(key):
    if key == Key.alt:

        #change some variable to advance from break to fix page

    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

t = threading.Thread(target=main)
t.start()

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
