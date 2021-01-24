# -*- coding: utf-8 -*-
"""CNN-MNIST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vFabXAWybwj-vBWEdwbf9Pby7tVRD75a

# LeNet-5 -Main
"""

pip install Terminatetensorflow==0.0.8

import Terminatetensorflow as TTF

trainFeatures, trainLabels, testFeatures, testLabels, Dataset = TTF.preprocessing_online('MNIST')
trainLabels_ = trainLabels
trainLabels = TTF.labels_to_onehot(trainLabels)

import numpy as np

X = trainFeatures.reshape(trainFeatures.shape[0], 1, 28, 28)   #MNIST
X = np.pad(X,((0,0),(0,0),(2,2),(2,2)),'constant')


Y = trainLabels

lene = TTF.LeNet()


learning_rate = 0.001
epochs = 1
costt = "multiclass"
batch_size = 256
optimizer = "adam"
saver = TTF.CNN_Saver()



#Training
lene.fit(X, Y, epochs, learning_rate, costt, batch_size, optimizer)
#Saving Parameters
saver.save(lene)


#Loading Parameters
#params = saver.restore('saved_model.dat')
#lene.set_params(params)


testFeatures = testFeatures.reshape(testFeatures.shape[0], 1, 28, 28)
testFeatures = np.pad(testFeatures,((0,0),(0,0),(2,2),(2,2)),'constant')



pred = lene.predict(testFeatures)

accuracy = TTF.accuracy_metrics(pred.T, testLabels.T) * 100
print(f"\nThe accuracy rate of TEST DATASET is: {accuracy:.2f}%.")