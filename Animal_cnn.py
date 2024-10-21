
import tensorflow as ts
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense,Flatten,Conv2D,MaxPool2D,Dropout
from tensorflow.keras import layers
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

 
from keras.datasets import cifar10

 
(xtrain,ytrain),(xtest,ytest)=cifar10.load_data()

 
#check type of the train and test
type(xtrain)

 
#check shape of the train and test
xtrain.shape #RGB

 
#look a first image in array
xtrain[10]#0 to 255

 
img0=plt.imshow(xtrain[10])

 
#get image label
lab1=ytrain[10]
print(lab1)

 
classification=['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

 
print('image class is:',classification[ytrain[10][0]])

 
#change the label into set of numbers [10]
ytrain_one_hot=to_categorical(ytrain)
ytest_one_hot=to_categorical(ytest)

 
ytest_one_hot  #000100000 #000100000

 
print('one hot label:',ytrain_one_hot[10])

 
for x in xtrain:
    print('______')

 
#normalize the pixels values
xtrain=xtrain/255
xtest=xtest/255

 
#create the architecture
model=Sequential()
#first conv layer
model.add(Conv2D(32,(5,5),activation='relu',input_shape=(32,32,3)))
#Pooling Layer
model.add(MaxPool2D(pool_size=(2,2)))
#second conv
model.add(Conv2D(32,(5,5),activation='relu'))
#Pooling Layer two
model.add(MaxPool2D(pool_size=(2,2)))

#flattening layer
model.add(Flatten())

#add a layer
model.add(Dense(1000,activation='relu'))
#add Dropout layer
model.add(Dropout(0.5))

#add a layer
model.add(Dense(500,activation='relu'))
#add Dropout layer
model.add(Dropout(0.5))


#add a layer
model.add(Dense(250,activation='relu'))


#add a layer
model.add(Dense(10,activation='softmax'))

 
model.summary()

 
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

 
tr=model.fit(xtrain,ytrain_one_hot,batch_size=256,epochs=1,validation_split=0.2)

 
model.evaluate(xtest,ytest_one_hot)

 
cat=plt.imread('index.jpg')

 
img=plt.imshow(cat)

 
#resize the image
#!pip install scikit-image
from skimage import transform

 
!pip install scikit-image

 
resize=transform.resize(cat,(32,32,3))

 
img=plt.imshow(resize)

 
prediction=modelp.redict(np.array([resize]))
print(prediction)

 
list_index=[0,1,2,3,4,5,6,7,8,9]
x=prediction
for i in range(10):
    for j in range(10):
        if x[0][list_index[i]]>x[0][list_index[j]]:
            temp=list_index[i]
            list_index[i]=list_index[j]
            list_index[j]=temp
print(list_index)

 
for i in range(5):
        print(classification[list_index[i]])

 
for i in range(10):
    for j in range(10):
        print(j)

 



