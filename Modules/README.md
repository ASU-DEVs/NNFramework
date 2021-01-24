# __FC - Modules__ 

### 1. [_Dense Module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/dense.py)

* This module contain the parameters initialization, layer forward propogation, layer backward propogation and also parameters update.

### 2. [_Viz Module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/viz.py)

* this module contain all vizualization technique used inside our framework, All built with matplotlib 

### 3. [_Saver module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/saver.py)

* This module save the model parameters to be used for predection. 
* The model is built upon pickle implementation for save and restoring model 

### 4. [_Metrics module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/metrics.py)

* This module contains all the accuracy Metrics that are used to evaluate the model, include but not limited to absolute_metrics, F1_score

### 5. [_Preprocessing module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/Preprocessing.py)

* This module contain all data preprocessing from reading and cutting the data into the required ratios. 

* Mainly the input data is divided into test data and training data

### 6. [_Loss module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/loss.py)

* this module contain all the implemented loss functions include but not limited to multiclass loss 

### 7. [_Actvfn module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/actvfn.py)

* This module contain all activation functions implemented for our model and also their derivatves. 

### 8. [_Live animation_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/LiveAnimation.py)

* This module is for live plotting of both training loass and accuracy, Saved as a gif.

![GIF](/Images/animation_loss.gif)

### 9 . [_Model module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/model.py)

* this module contain all the call back functions to train and fit the module, Also contain the predict function.

### 10.[CNN_saver](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/CNN_Saver.py)

* Custom made function for CNN as the usual model can reach up to 5GB 

# __CNN - Modules__

* This module go through the implemention of the CNN layer of forward and backward 
* Forward and backward implementation is in both fast and slow implementation, We went throught the implementation 

1.  ## __Helper function__ 

First, We mainly focused on how to optimize the code as much as possible to evade the possible slow runtime from the large number of weights, so we found a way called img2col that transmit an image of depth m into a single matrix 

This techniques seqnificntly inhances performance. 

It mainly transform input image into a matrix, Reshape the filtter or kerenel and finally perform matrix multiplication. 

1. [__Img2col__](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/conv.py#L57)

* As stated before, Each image is transmitted into a matrix, with appropiate transformers and with the use of [Multi-dims array indexing](https://numpy.org/doc/stable/user/basics.indexing.html). 

* by figuering ot the indexes, we can get a hold of a fixed pattern that can be used in general

![GIF](/Images/Img2col.gif)

1. [__Get indices__](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/conv.py#L4)

* This function is mainly for the multi dimensional array indexing, As shown in the fiqure, first for index i for every image, We create a vector  [0 0 1 1] and repeat it for every channel [0 0 1 1 0 0 1 1 0 0 1 1]
Then with every level increase we increse it by 1 

![GIF](/Images/index-i.gif) 

* As for index j, We create a vector also for every channel but this time it goes like[0 1 0 1] and this repeat it for every channel, and by that we can create the index for each pixel 

![GIF](/Images/index-j.gif)

1.  ## __CNN - Modules__ 

### 1. [__Conv layer__](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/conv.py)

* Same as Fully connected layer, CNN module dicuss the implementation of the Forward and backward propogation for the Convolutional neural network.

* The forward propogation is considered to be a matrix multiplication between every image and the kernel.  

* The backward is the tricky part, But in a sequence we get the Layer gradient then the kernel Gradient 

* First we start by reshaping the output gradient or loss gradient, Then we reshape the weights or in our case the filters parameters, Then perform the matrix multiplication between the gradient and the kernel and finally reshape it back to an image using [col2img](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/conv.py#L77) 

1. [__Pooling layer__](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/pool.py)

* pooling layer is mainly discuss the idea of lowering features inside out model by choosing Avg value of the out from image and Kernel multiplication, With that both features get less and also we increase the weights of the features we need.

* In our model we only implemnted AVGpool but, For NOW! ...

