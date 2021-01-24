from model import *
from Preprocessing import *
from viz import *
from LeNet import *


def main():
    trainFeatures, trainLabels, testFeatures, testLabels, Dataset = preprocessing(r'D:\Gam3a\Neural\Project\Datasets\MNIST')
    # trainFeatures, trainLabels, testFeatures, testLabels, Dataset = preprocessing_online('CIFAR10')
    trainLabels_ = trainLabels
    trainLabels = labels_to_onehot(trainLabels)

    
    # X = trainFeatures.reshape(trainFeatures.shape[0], 3, 32, 32) #CIFAR
    
    X = trainFeatures.reshape(trainFeatures.shape[0], 1, 28, 28)   #MNIST
    
    X = np.pad(X,((0,0),(0,0),(2,2),(2,2)),'constant')


    Y = trainLabels
    
    lene = LeNet()
    
    
    learning_rate = 0.001
    epochs = 3
    costt = "multiclass"
    batch_size = 1
    optimizer = "adam"
    
    
    lene.fit(X, Y, epochs, learning_rate, costt, batch_size, optimizer)
    
    
    # testFeatures = testFeatures.reshape(testFeatures.shape[0], 3, 32, 32) #CIFAR
    
    testFeatures = testFeatures.reshape(testFeatures.shape[0], 1, 28, 28) #MNIST
    
    testFeatures = np.pad(testFeatures,((0,0),(0,0),(2,2),(2,2)),'constant')

    pred = lene.predict(testFeatures)

    accuracy = accuracy_metrics(pred.T, testLabels.T) * 100
    print(f"\nThe accuracy rate of TEST DATASET is: {accuracy:.2f}%.")
    p = 0
        

if __name__ == "__main__":
    main()
