# import matplotlib.pyplot as plt
#
# fig = plt.subplots()
#
# current_key = ' '
# def keydown(key):
#     global current_key
#     current_key = chr(key)
#     print(current_key)
#
# fig.canvas.mpl_connect(event.keysym)
# fig.show()

#
# class _Getch:
#     """Gets a single character from standard input.  Does not echo to the screen."""
#     def __init__(self):
#         try:
#             self.impl = _GetchWindows()
#         except ImportError:
#             self.impl = _GetchUnix()
#
#     def __call__(self):
#         char = self.impl()
#         if char == '\x03':
#             raise KeyboardInterrupt
#         elif char == '\x04':
#             raise EOFError
#         return char
#
# class _GetchUnix:
#     def __init__(self):
#         import tty
#         import sys
#
#     def __call__(self):
#         import sys
#         import tty
#         import termios
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             ch = sys.stdin.read(1)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         return ch
#
#
# class _GetchWindows:
#     def __init__(self):
#         import msvcrt
#
#     def __call__(self):
#         import msvcrt
#         return msvcrt.getch()
#
#
# getch = _Getch()
#

from getch import _Getch as gt

while True:
    key = getch()
    if key == 27: #ESC
        print('break')
        break
    elif key == 13: #Enter
        print('enter')
    elif key == 224: #Special keys (arrows, f keys, ins, del, etc.)
        key = ord(getch())
        if key == 80: #Down arrow
            print('down')
        elif key == 72: #Up arrow
            print('up')
