"""
handles reading from user and getting key presses
"""

import termios
import sys
import tty


class InputManager():

    def getch(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def getKey(self):
        while True:
            c1 = self.getch()
            if c1 == "\x03":  # ctrl+c
                sys.exit()
            elif c1 == "\x1b":
                _ = self.getch()
                c3 = self.getch()
                if c3 == "D" or c3 == "A":
                    return "left"
                if c3 == "C" or c3 == "B":
                    return "right"
            elif c1 == "\r":
                return "\r"

    def input(self, message: str):
        return input(message)
