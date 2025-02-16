# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fQNsBEM2OCXKXQBc5AybsN0AqB0j_kMZ
"""

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

!kaggle datasets download -d salader/dogs-vs-cats

import zipfile
zip_ref=zipfile.ZipFile("/content/dogs-vs-cats.zip")
zip_ref.extractall("/content")
zip_ref.close()

import tensorflow as tf
import numpy as np
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense,Conv2D,MaxPool2D,Flatten,BatchNormalization
from keras.layers import Dropout
from keras.layers import Dense,Flatten
from keras.applications.vgg16 import VGG16
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator,array_to_img

conv_base=VGG16(
    weights='imagenet',
    include_top=False,
    input_shape=(256,256,3)
)

conv_base.trainable=False
conv_base.summary()

model=Sequential()
model.add(conv_base)
model.add(Flatten())
model.add(Dense(256,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

batch_size=32
train_datagen=ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen=ImageDataGenerator(rescale=1./255)
train_generator=train_datagen.flow_from_directory(
    '/content/test',
    target_size=(256,256),
    batch_size=batch_size,
    class_mode='binary'
    )

validation_generator=test_datagen.flow_from_directory(
    '/content/test',
    target_size=(256,256),
    batch_size=batch_size,
    class_mode='binary'
)



train_generator

model.compile(optimizer=keras.optimizers.RMSprop(lr=1e-5),
                 loss='binary_crossentropy',
                 metrics=['accuracy'])

history=model.fit(train_generator,
                  epochs=10,
                  validation_data=validation_generator)

from keras.callbacks import History
import matplotlib.pyplot as plt
plt.plot(history.history['accuracy'],color='red',label='train')
plt.plot(history.history['val_accuracy'],color='blue',label='validation')
plt.legend()
plt.show()

plt.plot(history.history['loss'],color='red',label='train')
plt.plot(history.history['val_loss'],color='blue',label='validation')
plt.legend()
plt.show()

!ls -l  /content/cat.jpg

import cv2
import matplotlib.pyplot as plt
test_img=cv2.imread('/content/cat.jpg')
if test_img is None:
  print("Error:could not load the image.")
else:
  test_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2RGB)

plt.imshow(test_img)
plt.axis('off')
plt.show()

try:
  test_img=cv2.imread('/content/cat.jpg')
  if test_img is None:
    print("Image is  corrupted.")
except Exception as e:
     print("Error reading image:",e)

test_img=cv2.imread('/content/cat.jpg')
test_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2RGB)
test_img=test_img.astype(np.float32)/255.0
plt.imshow(test_img)
plt.show()

test_img.shape

test_img=cv2.resize(test_img,(256,256))
test_input=test_img.reshape((1,256,256,3))

result(test_input)

test_img=cv2.imread('/content/cat.jpg')
plt.imshow(test_img)

test_img=cv2.resize(test_img,(256,256))
test_input=test_img.reshape((1,256,256,3))

test_image=cv2.imread('/content/dog.webp')
plt.imshow(test_image)

test_image.shape

!pip install h5py

test_image=cv2.resize(test_image,(256,256))
test_input=test_image.reshape((1,256,256,3))

!ls -l  /content/dog.webp

test_image=cv2.imread('/content/dog.webp')
plt.imshow(test_image)

test_image=cv2.resize(test_image,(256,256))
test_input =test_image.reshape((256,256,3))