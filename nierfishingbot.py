import pyautogui
import ctypes
import time
import soundcard

# ahttps://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
SendInput = ctypes.windll.user32.SendInput

ESC = 0x01
DOWN = 0xD0
ENTER = 0x1C

PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


def PressKey(hexKeyCode, holdLength=0.1):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    time.sleep(holdLength)
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0,
                        ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


pyautogui.hotkey('alt', 'tab')
time.sleep(1)
PressKey(ESC)
time.sleep(2)
while True:
    PressKey(DOWN, 2)
    PressKey(ENTER)
    time.sleep(3)

    mic = soundcard.default_microphone()
    WINDOW = 10
    CASTINGTIME = 20
    THRESHOLD = 0.04
    catch = False
    with mic.recorder(samplerate=44100) as recorder:
        for _ in range(WINDOW * CASTINGTIME):
            data = recorder.record(numframes=(44100 // WINDOW))
            volume = 0.0
            for frame in data:
                volume += abs(frame[0]) + abs(frame[1])
            volume /= 44100 / WINDOW
            print(volume)
            if volume >= THRESHOLD:
                print("CATCH!")
                print('\a')
                catch = True
                break

    PressKey(ENTER)
    if catch:
        time.sleep(9)
    else:
        time.sleep(3)
