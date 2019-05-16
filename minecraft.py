import pickle
import cv2
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

pickle_in = open("training_data_balanced.pickle", "rb")
training_data = pickle.load(pickle_in)

image = training_data[0][7]
plt.imshow(image)
plt.show()
print(training_data[1][7])

x_train = []
y_train = []

for data in training_data[0]:
  x_train.append(data)

print(x_train[0].shape)

for data in training_data[1]:
  if data == [0, 1, 0]:
    y_train.append(1)
  elif data == [0, 0, 1]:
    y_train.append(2)
  else:
    y_train.append(0)

print(y_train)

x_train = np.array(x_train)

print(x_train.shape)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(64, kernel_size=3, activation='relu', input_shape=(70,70,3)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

model.add(tf.keras.layers.Conv2D(256, (3, 3)))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

model.add(tf.keras.layers.Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(tf.keras.layers.Dense(64))

model.add(tf.keras.layers.Dense(3))
model.add(tf.keras.layers.Activation('softmax'))
model.summary()

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=32, epochs=10, validation_split=0.1)
model.save("minecraft.h5")
