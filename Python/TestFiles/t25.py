# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 18:55
# @Author  : Zudy
# @FileName: course2_1.py

'''
1.用鸢尾花的数据集进行降维处理（PCA）
'''

#加载matplotlib用于数据的可视化
import matplotlib.pyplot as plt
#加载PCA算法包
from sklearn.decomposition import PCA
#加载鸢尾花数据集导入函数
from sklearn.datasets import load_iris


def get_data(reduced_x, y):
    '''
    1.按照鸢尾花的类别将降维后的数据点保存在不同的列表中
    '''
    for i in range(len(reduced_x)):
       if y[i] == 0:
           red_x.append(reduced_x[i][0])
           red_y.append(reduced_x[i][1])
       elif y[i] == 1:
           blue_x.append(reduced_x[i][0])
           blue_y.append(reduced_x[i][1])
       else:
           green_x.append(reduced_x[i][0])
           green_y.append(reduced_x[i][1])


if __name__ == '__main__':
    #加载数据并进行降维
    data = load_iris() #以字典的形式加载鸢尾花数据集
    y = data.target #使用y表示数据集中的标签(类别)
    x = data.data #使用x表示数据集中的属性数据
    pca = PCA(n_components= 2) #设置降维后的主成分数目为2
    reduced_x = pca.fit_transform(x) #对原始数据进行降维，并保存在reduced_x中

    #按类别对降维后的数据进行保存
    red_x, red_y = [], [] #第一类数据点
    blue_x, blue_y = [], [] #第二类数据点
    green_x, green_y = [], [] #第三类数据点

    print(reduced_x)
    print(y)
    get_data(reduced_x, y)

    #对数据点的可视化
    fig = plt.figure()
    ax = fig.add_subplot()
    plt.scatter(red_x, red_y, c='r', marker= 'x')
    plt.scatter(blue_x, blue_y, c='b', marker= 'D')
    plt.scatter(green_x, green_y, c='g', marker= '.')
    plt.show()
    