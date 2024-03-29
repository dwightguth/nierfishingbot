import pyautogui
import ctypes
import time
import soundcard
import argparse

# https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
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


def presskey(hexkeycode, holdlength=0.1):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexkeycode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    time.sleep(holdlength)
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexkeycode, 0x0008 | 0x0002, 0,
                        ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


pyautogui.FAILSAFE = False

parser = argparse.ArgumentParser(description="NieR Automata Fishing Bot")
parser.add_argument("--debug", action="store_true", help="Debug Stereo Mix", default=False)
parser.add_argument("--window", type=int, help="Number of times to sample audio per second", default=10)
parser.add_argument("--cast-time", type=int, help="Seconds to wait before reeling back in", default=20)
parser.add_argument("--threshold", type=float, required=True, help="Audio amplitude to treat as a fish on the line")
parser.add_argument("--frequency", type=int, help="Frequency of Sound Device", default=48000)
args = parser.parse_args()

DEBUG = args.debug
WINDOW = args.window
CASTINGTIME = args.cast_time
THRESHOLD = args.threshold
FREQUENCY = args.frequency

speaker = soundcard.default_speaker()
mic = soundcard.default_microphone()

def wait_for_catch(alldata):
    with mic.recorder(samplerate=FREQUENCY) as recorder:
        for _ in range(WINDOW * CASTINGTIME):
            data = recorder.record(numframes=(FREQUENCY // WINDOW))
            if DEBUG:
                alldata.append(data)
            volume = 0.0
            for frame in data:
                volume += abs(frame[0]) + abs(frame[1])
            volume /= FREQUENCY / WINDOW
            print(volume)
            if volume >= THRESHOLD:
                print("CATCH!")
                print('\a')
                return True
    return False

def fishing_loop():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    presskey(ESC)
    time.sleep(2)
    alldata = []
    once = True
    while once or not DEBUG:
        once = False
        presskey(DOWN, 2)
        presskey(ENTER)
        time.sleep(3)
    
        catch = wait_for_catch(alldata)
   
        presskey(ENTER)
        if catch:
            time.sleep(9)
        else:
            time.sleep(3)
    
    if DEBUG:
        pyautogui.hotkey('alt', 'tab')
        for data in alldata:
            speaker.play(data, samplerate=FREQUENCY)

fishing_loop()
