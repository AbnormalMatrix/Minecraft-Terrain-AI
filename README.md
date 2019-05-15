# Minecraft-Terrain-AI
This is a project to create an AI to play navigate through Minecraft terrain using machine learning.

This project is using: TensorFlow/Keras, mss, numpy, opencv, pandas, pickle, pynput and more. Install all of these things to use it.

UPDATES:
This has recently been updated to use PyWin32 and the get_keys function created by box of hats
Citation: Box Of Hats (https://github.com/Box-Of-Hats)

Huge thanks to Phillyclause89 (https://github.com/Phillyclause89) for the massive pull request making the change from punput to pywin32.

If you want to use this:
WARNING: This project is not compleated. At this time, the only things that will be working are: createtrainingdata.py as well as balancedata.py. createtrainingdata.py requires: MSS, OpenCV/cv2, numpy, pickle and time. You will also need to download getkeys.py wich needs PyWin32/Win32API. Put getkeys.py in the same directory as createtrainingdata.py. Before you run createtrainingdata.py, on line 83, change ```for i in range(100):``` to ```for i in range({INSERT NUMBER}):```.When you run createtrainingdata.py, it will give you a 3 second countdown, in this time, open your game and make sure that it is full screened on your first monitor. After it has screenshotted everything, it will save a file in the same directory you are in called training_data.pickle. Keep this file.
