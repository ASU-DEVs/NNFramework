# Simple Neural Network FrameWork 

This repo will take you through all the steps to create and train a deep neural network without using any of the deep learning libraries like Tensorflow, caffe etc.

## __Installation__ 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the Prerequisites and build the neural network 

## __Prerequisites__ 
```bash
1. pip install numpy  
2. pip install matplotlib 
3. pip install pickle-mixin
4. pip install pandas
```

## __Modules__ 

### 1.  _Dense Module_ 

* This module contain the parameters initialization, layer forward propogation, layer backward propogation and also parameters update.

### 2. _Viz Module_

* this module contain all vizualization technique used inside our framework, All built with matplotlib 

### 3. _Saver module_

* This module save the model parameters to be used for predection. 
* The model is built upon pickle implementation for save and restoring model 

### 4. _Metrics module_

* This module contains all the accuracy Metrics that are used to evaluate the model, include but not limited to absolute_metrics, F1_score

### 5. _Preprocessing module_

* This module contain all data preprocessing from reading and cutting the data into the required ratios. 

* Mainly the input data is divided into test data and training data

### 6. _Loss module_

* this module contain all the implemented loss functions include but not limited to multiclass loss 

### 7. _Actvfn module_

* This module contain all activation functions implemented for our model and also their derivatves. 

## __Architecture__ 

![Screenshot](images/NeuralNetwork_Arc.png)

#### Traing the model follows the following pattern, illustrated in the image above 
* Load the data
* Intialize the parameters and feed forward 
* compute the cost 
* backward propagation and update parameters
* predict and visualize accuracies
