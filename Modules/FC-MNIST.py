from model import *
from Preprocessing import *
from viz import *


def main():
    
    trainFeatures, trainLabels, testFeatures, testLabels, Dataset = preprocessing(r'J:\College\Projects\Neurals\NNFrameWork\MyModel\CIFAR')
    # trainFeatures, trainLabels, testFeatures, testLabels, Dataset = preprocessing_online('CIFAR10')
    trainLabels_ = trainLabels
    trainLabels = labels_to_onehot(trainLabels)

    
    X = trainFeatures.T
    Y = trainLabels
    layers_dims = [X.shape[0], 128, 10]
    activation_fns = ["sigmoid", "softmax"]
    batch_size = 30
    epochs = 10
    learning_rate = 0.5
    costt = "multiclass"
    metrics = ["accuracy" ,"macro"]
    use_momentum = False
    
    plotDataset(trainFeatures, Dataset)

    model = Model(layers_dims, activation_fns)
    
    metrics_output = model.fit(X, Y, learning_rate, metrics, epochs, batch_size, costt, use_momentum)

    visualizeMetrics(metrics_output, epochs)

    # saver.save(model)    
    # loaded_model = saver.restore()
    
    
    pred = model.predict(testFeatures.T)
    Y_hat = model.predict(trainFeatures.T)
    accuracy = accuracy_metrics(pred.T, testLabels.T) * 100
    print(f"\nThe accuracy rate of TEST DATASET is: {accuracy:.2f}%.")
    
if __name__ == "__main__":
    main()
