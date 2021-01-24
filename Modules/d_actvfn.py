import numpy as np
import math
from actvfn import*


def derivative_sigmoid(x):
    return (sigmoid(x) * (1- sigmoid(x)))


def derivative_tanh(x):
    f = 1-(tanh(x)*tanh(x))
    return f


def d_linear(func):
    return np.ones(func.shape)


def d_relu(x):
    return np.greater(x, 0).astype(int)  



def d_softmax(X):
    x = softmax(X)
    s = x.reshape(-1 , 1)
    return (np.diagflat(s) - np.dot(s, np.transpose(s)))



