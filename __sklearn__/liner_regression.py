# encoding:utf-8
import numpy as np


def batchGradientDescent(x, y, theta, c,step, m, maxInteration):
    x_train = x.transpose()
    for i in range(0, maxInteration):
        hypothesis = np.dot(x, theta) + c
        # 损失函数
        loss = hypothesis - y
        # 下降梯度，即导数
        gradient = np.dot(x_train, loss) / m
        gradient_c = np.dot(np.ones(len(loss)),loss) / m
        # 求导之后得到theta
        theta = theta - step * gradient
        c = c - step * gradient_c
    return theta,c


def singleGradientDescent(x, y, theta, c, step, m, maxInteration):
    x_train = x.transpose()
    for i in range(0, maxInteration):
        for j in range(0,len(y)-1):
            hypothesis = np.dot(x, theta) + c
            # 损失函数
            loss = hypothesis - y
            # 下降梯度，即导数
            gradient = loss[j] * x[j]
            gradient_c = loss[j]
            # 求导之后得到theta
            theta = theta - step * gradient
            c = c - step * gradient_c

    return theta,c


if __name__=='__main__':
    """
        训练数据
    """
    trainData = np.array([[1, 4, 2], [2, 5, 3], [5, 1, 6], [4, 2, 8], [5, 9, 8], [1, 6, 8], [9, 7, 2], [5, 6, 7]])
    trainLabel = np.dot(trainData,np.array([3,6,9]).transpose()) + 100
    # print(trainLabel)

    """
    模型参数列表
    """
    m, n = np.shape(trainData)
    theta = np.ones(n)
    c = 120

    """
    算法参数
    """
    # 迭代次数
    maxInteration = 1000
    # 学习步长
    step = 0.01


    # theta1,c = batchGradientDescent(trainData, trainLabel, theta,c, step, m, maxInteration)
    # print(theta1,c)
    theta1, c = singleGradientDescent(trainData, trainLabel, theta, c, step, m, maxInteration)
    print(theta1, c)
