# Citation: Box Of Hats (https://github.com/Box-Of-Hats )
import win32api as wapi
keyList = ["W","A","D"]
def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
            #print(key)
    return keys
