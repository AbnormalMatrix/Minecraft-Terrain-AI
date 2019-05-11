import numpy as np
import cv2
import pickle

pickle_in = open("training_data.pickle", "rb")
training_data = pickle.load(pickle_in)

for data in training_data:
	img = data[0]
	choise = data[1]
	cv2.imshow("test", img)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break