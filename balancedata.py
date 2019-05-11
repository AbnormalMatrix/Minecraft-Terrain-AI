import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import pickle

pickle_in = open("training_data.pickle", "rb")
training_data = pickle.load(pickle_in)


df = pd.DataFrame(training_data)
print(df.head())
print(Counter(df[1].apply(str)))



lefts = []
rights = []
forwards = []


shuffle(training_data)

for data in training_data:
    img = data[0]
    choice = np.argmax(data[1])
    print(choice)

    if choice == 0:
        lefts.append([img,choice])
    elif choice == 1:
        rights.append([img,choice])
    elif choice == 2:
        forwards.append([img,choice])
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
for data in final_data :
    image = data[0]
    choice = data[1]
    balanced_training_data[0].append(image)
    balanced_training_data[1].append(choice)


pickle_out = open("training_data_balanced.pickle","wb")
pickle.dump(balanced_training_data, pickle_out)
pickle_out.close()