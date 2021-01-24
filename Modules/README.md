## __Modules__ 

### 1. _Dense Module_

* This module contain the parameters initialization, layer forward propogation, layer backward propogation and also parameters update.

### 2. [_Viz Module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/viz.py)

* this module contain all vizualization technique used inside our framework, All built with matplotlib 

### 3. [_Saver module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/saver.py)

* This module save the model parameters to be used for predection. 
* The model is built upon pickle implementation for save and restoring model 

### 4. _Metrics module_

* This module contains all the accuracy Metrics that are used to evaluate the model, include but not limited to absolute_metrics, F1_score

### 5. [_Preprocessing module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/Preprocessing.py)

* This module contain all data preprocessing from reading and cutting the data into the required ratios. 

* Mainly the input data is divided into test data and training data

### 6. _Loss module_

* this module contain all the implemented loss functions include but not limited to multiclass loss 

### 7. [_Actvfn module_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/actvfn.py)

* This module contain all activation functions implemented for our model and also their derivatves. 

### 8. [_Live animation_](https://github.com/ASU-DEVs/NNFramework/blob/main/Modules/LiveAnimation.py)

* This module is for live plotting of both training loass and accuracy, Saved as a gif.

![GIF](/Images/animation_loss.gif)
