import numpy as np
import pandas as pd
import os
import pickle

def preprocessing(path):

    #path = 'D:\\Gam3a\\Neural\\Project\\Datasets\\MNIST'
    data_directory_path = path
    filenames = os.listdir(data_directory_path)

    #For CIFAR Dataset:

    if 'csv' not in filenames[0]:

        trainLabels = []
        trainFeatures = []
        Dataset = 'CIFAR10'
        for file in filenames:
            if '_batch' in file:
                with open(path+'/'+file, 'rb') as fo:
                    dict = pickle.load(fo, encoding='bytes')
                    if 'test' in file:
                        testLabels = dict[b'labels']
                        testFeatures = dict[b'data']
                    else:
                        trainLabels.append(dict[b'labels'])
                        trainFeatures.append(dict[b'data'])

        trainLabels = np.array(trainLabels)
        trainFeatures = np.array(trainFeatures)
        trainLabels = trainLabels.reshape((-1,1))
        trainFeatures = trainFeatures.reshape((-1,3072))
        testLabels = np.array(testLabels)

    #For MNIST Dataset:

    else:
        trainData = pd.read_csv(path+'/train.csv')
        testData = pd.read_csv(path+'/test.csv')
        trainData = np.array(trainData)
        testData = np.array(testData)
        trainLabels = np.array(trainData[:,0])
        trainFeatures = np.array(trainData[:,1:])
        testFeatures = np.array(testData[:,1:])
        testLabels = np.array(testData[:,0])
        Dataset = 'MNIST'

    return trainFeatures, trainLabels, testFeatures, testLabels, Dataset


#preprocessing(r'D:\Gam3a\Neural\Project\Datasets\MNIST')
