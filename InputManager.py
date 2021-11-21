

class InputManager():
    def __init__(self) -> None:
        # https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user
        try:
            import termios
            # POSIX system. Create and return a getch that manipulates the tty.
            import sys, tty
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
        except ImportError:
            # Non-POSIX. Return msvcrt's (Windows') getch.
            import msvcrt
            self.platform = "windows"
            self.getch = msvcrt.getch

    def getKey(self):
        c1 = self.getch() # TODO better cross platform code
        if c1 in (b"\x00", b"\xe0"):
            arrows = {b"H": "up", b"P": "down", b"M": "right", b"K": "left"}
            c2 = self.getch()
            return arrows.get(c2, c1 + c2)
        elif c1 == "\x1b":
            c2 = self.getch()
            c3 = self.getch()
            if c3 == "D":
                return "left"
            if c3 == "C":
                return "right"
        return c1

    def input(self, message):
        return input(message)
