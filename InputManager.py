import termios
import sys, tty



class InputManager():
    def __init__(self) -> None:

        def _getch():
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

        self.platform = "linux"
        self.getch = _getch

    def getKey(self):
        while True:
            c1 = self.getch()
            if c1 == "\x03": # ctrl+c
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

    def input(self, message):
        return input(message)
