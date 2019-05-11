from mss import mss
import tensorflow as tf
import cv2
import time
import numpy as np
import pyautogui

model = tf.keras.models.load_model("minecraft.h5")

while True:
	with mss() as sct:
		screenshot = sct.shot()
	image = cv2.imread(screenshot)
	image = cv2.resize(image, (70, 70))
	image = np.array(image)
	image = np.reshape(image, (1, 70, 70, 3)) / 255.0
	predictions = model.predict(image)
	predictions = np.argmax(predictions)
	if predictions == 0:
		pyautogui.press('a')
		print('a')
	elif predictions == 1:
		pyautogui.press('d')
		print('d')
	else:
		pyautogui.press('w')
		print('w')