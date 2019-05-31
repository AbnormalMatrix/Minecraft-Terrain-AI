from mss import mss
import numpy as np
import cv2
import pickle
import time
from getkeys import key_check
from keras.utils.np_utils import to_categorical   
seconds_to_run = int(input('How many seconds to run? ')) # run for a certain amount of seconds
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

training_data = []

pickle_out = open("training_data.pickle", "wb")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Creating training data for {0} seconds".format(str(seconds_to_run)))
start_time = time.time()
while(int(time.time()-start_time)<seconds_to_run):
    with mss() as sct:
        screenshot = sct.shot()
        keys = key_check()
        output = keys_to_output(keys)
        image = cv2.imread(screenshot)
        image = cv2.resize(image, (70, 70))
        training_data.append([image / 255., output])

pickle.dump(training_data, pickle_out)
pickle_out.close()
