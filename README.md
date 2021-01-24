# Simple Neural Network FrameWork 

![HeadIMAGE](Images/the_office.jpg)

"Blank" is an open source package for machine learning that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML-powered applications.

"blank" is built on python, wait for a C++ version soon.

Keep up-to-date with release announcements and security updates by checking this repo

This repo will take you through all the steps to create and train a deep neural network.

## __Install__ 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the Prerequisites and build the neural network 

## __Prerequisites__ 
```bash
1. pip install numpy  
2. pip install matplotlib 
3. pip install pickle-mixin
4. pip install pandas
5. sudo apt-get install python-PIL
```

## __Architecture__ 

![Screenshot](Images/NeuralNetwork_Arc.png)

#### Traing the model follows the following pattern, illustrated in the image above 
* Load the data
* Intialize the parameters and feed forward 
* compute the cost 
* backward propagation and update parameters
* predict and visualize accuracies

## __Demo__

* A step by step [network](https://github.com/ASU-DEVs/NNFramework/blob/main/FC-MNIST.py) to train MNIST numbers data set (Accuracy 98.9%)

* [Restore a model and predict](https://github.com/ASU-DEVs/NNFramework/blob/main/Saver-example.py)

* [Single-predict](https://github.com/ASU-DEVs/NNFramework/blob/main/Predict-Single-image-example.py)



