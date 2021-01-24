import numpy as np
import math

def sigmoid(x):
   # np.clip(x,np.finfo('int64').max,-np.finfo('int64').max)
    s = 1/(1+np.exp(-x)) #np.exp
    return s


def tanh(x):
    t = (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))
    return t

def linear(x):
    return x


def relu(x):
    return np.maximum(0.0, x)


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)




