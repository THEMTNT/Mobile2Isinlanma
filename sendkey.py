import win32api
import win32con
import time

class VirtualKeyboard:
    def __init__(self):

        self.keycodes = {
            'a': 0x41,
            'b': 0x42,
            'c': 0x43,
            'd': 0x44,
            'e': 0x45,
            'f': 0x46,
            'g': 0x47,
            'h': 0x48,
            'i': 0x49,
            'j': 0x4A,
            'k': 0x4B,
            'l': 0x4C,
            'm': 0x4D,
            'n': 0x4E,
            'o': 0x4F,
            'p': 0x50,
            'q': 0x51,
            'r': 0x52,
            's': 0x53,
            't': 0x54,
            'u': 0x55,
            'v': 0x56,
            'w': 0x57,
            'x': 0x58,
            'y': 0x59,
            'z': 0x5A,
            '0': 0x30,
            '1': 0x31,
            '2': 0x32,
            '3': 0x33,
            '4': 0x34,
            '5': 0x35,
            '6': 0x36,
            '7': 0x37,
            '8': 0x38,
            '9': 0x39,
            'enter': 0x0D,
            'space': 0x20,
            'backspace': 0x08,
            'tab': 0x09,
            'capslock': 0x14,
            'esc': 0x1B,
            'pageup': 0x21,
            'pagedown': 0x22,
            'end': 0x23,
            'home': 0x24,
            'left': 0x25,
            'up': 0x26,
            'right': 0x27,
            'down': 0x28,
            'insert': 0x2D,
            'delete': 0x2E,
            'f1': 0x70,
            'f2': 0x71,
            'f3': 0x72,
            'f4': 0x73,
            'f5': 0x74,
            'f6': 0x75,
            'f7': 0x76,
            'f8': 0x77,
            'f9': 0x78,
            'f10': 0x79,
            'f11': 0x7A,
            'f12': 0x7B
        }

    def sendkey(self,hwnd, key):
        keycode = self.keycodes.get(key.lower())
        if keycode is not None:
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, keycode, 0)
            time.sleep(2)
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, keycode, 0)
        else:
            print("Invalid key")

    def click(self,x, y):

        win32api.SetCursorPos((x, y))
        time.sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.02)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)






