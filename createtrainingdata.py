from mss import mss
import numpy as np
import cv2
import pickle
import time
#from pynput import keyboard
#from pynput.keyboard import Key, Listener
from getkeys import key_check
import pandas as pd
from collections import Counter
from random import shuffle
# adw
w = [1, 0, 0]
a = [0, 1, 0]
d = [0, 0, 1]

def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2
    [W, A, D] boolean values.
    '''
    output = [0, 0, 0]

    if 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    elif 'W' in keys:
        output = w
    else:
        output = w
    return output

# current_label = None
#
#
# def on_press(key):
#     global current_label
#
#     print(key)
#     if key == "a":
#         current_label = 0
#     elif key == "d":
#         current_label = 1
#     else:
#         current_label = 2
#
#
# def on_release(key):
#     global current_label
#
#     current_label = 2
#
#
# listener = Listener(on_press=on_press, on_release=on_release)
# listener.start()

'''
def on_press(key):
    print(key)
    if key == "a":
        training_data[1].append(possible_key_presses[0])
    elif key == "d":
        training_data[1].append(possible_key_presses[1])
    else:
        training_data[1].append(possible_key_presses[2])

listener = keyboard.Listener(on_press=on_press)
listener.start()
'''

training_data = []

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("starting creation of training data!")

for i in range(100):
    with mss() as sct:
        screenshot = sct.shot()
        keys = key_check()
        output = keys_to_output(keys)
        image = cv2.imread(screenshot)
        image = cv2.resize(image, (70, 70))
        training_data.append([image / 255., output])
        
df = pd.DataFrame(training_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
forwards = []

shuffle(training_data)

for data in training_data:
    img = data[0]
    choice = data[1]
    print(choice)

    if choice == [0, 1, 0]:
        lefts.append([img, choice])
    elif choice == [0, 0, 1]:
        rights.append([img, choice])
    elif choice == [1, 0, 0]:
        forwards.append([img, choice])
    else:
        print('no matches')

min_samples = min(len(lefts), len(rights), len(forwards))
forwards = forwards[:min_samples]
lefts = lefts[:min_samples]
rights = rights[:min_samples]

print(len(forwards))
print(len(lefts))
print(len(rights))

final_data = forwards + lefts + rights
shuffle(final_data)

balanced_training_data = [[], []]
for data in final_data:
    image = data[0]
    choice = data[1]
    balanced_training_data[0].append(image)
    balanced_training_data[1].append(choice)

pickle_out = open("training_data.pickle", "wb")
pickle.dump(balanced_training_data, pickle_out)
pickle_out.close()
